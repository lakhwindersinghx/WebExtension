import redis
import json
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from models.models import EventInput, AFKEventOutput, AFKEventInput
from logic.session_builder import build_session_blocks
from logic.summary_engine import summarize_day
from models.db_models import Event,AFKEvent  # SQLAlchemy model
from db import SessionLocal  # SQLAlchemy session
from fastapi import Query
from datetime import date
from datetime import datetime


app = FastAPI()

# Redis setup
r = redis.Redis(host='localhost', port=6379, db=0)

# CORS for browser extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your extension ID
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/track-event")
async def track_event(event: EventInput):
    
    print(f"Received EventInput: {event}")
    try:
        event_json = jsonable_encoder(event)
        r.lpush("event_queue", json.dumps(event_json))  # Push to Redis queue
        return {"status": "queued"}
    except Exception as e:
        print(f"[Error] Could not queue event: {e}")
        raise HTTPException(status_code=500, detail="Failed to queue event")

@app.post("/track-afk")
async def track_afk(event: AFKEventInput):
    db = SessionLocal()
    try:
        db_afk = AFKEvent(state=event.state, timestamp=event.timestamp)
        db.add(db_afk)
        db.commit()
        return {"status": "received", "saved": True}
    except Exception as e:
        print(f"[Error] Failed to store AFK event: {e}")
        raise HTTPException(status_code=500, detail="Failed to save AFK event")
    finally:
        db.close()

@app.get("/events")
def get_events():
    db = SessionLocal()
    try:
        events = db.query(Event).order_by(Event.timestamp.desc()).limit(50).all()
        return [jsonable_encoder(e) for e in events]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch events")
    finally:
        db.close()

@app.get("/afk-events", response_model=list[AFKEventOutput])
def get_afk_events(limit: int = 50):
    db = SessionLocal()
    try:
        events = db.query(AFKEvent).order_by(AFKEvent.timestamp.desc()).limit(limit).all()
        return events  # FastAPI converts this list using .from_orm()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch AFK events")
    finally:
        db.close()

@app.get("/summaries/daily")
def get_daily_summary(user_id: str = Query(...), day: date = Query(...)): #if we did not use date argument, we wouldve had to use date.today (default)
    print(f"Querying for user_id={user_id} and day={day}")
    db = SessionLocal()
    
    try:
        # Pull all events for the user on this day
        events = db.query(Event).filter(
            Event.timestamp >= datetime.combine(day, datetime.min.time()),
            Event.timestamp <= datetime.combine(day, datetime.max.time())
        ).all()

        afk_events = db.query(AFKEvent).filter(
            AFKEvent.timestamp >= datetime.combine(day, datetime.min.time()),
            AFKEvent.timestamp <= datetime.combine(day, datetime.max.time())
        ).all()

        blocks = build_session_blocks(events, afk_events)
        summary = summarize_day(blocks)
        return summary
    except Exception as e:
        print(f"[Summary Error] {e}")
        raise HTTPException(status_code=500, detail="Failed to generate summary")
    finally:
        db.close()

         
