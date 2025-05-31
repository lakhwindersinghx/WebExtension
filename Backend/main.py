import redis
import json
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from models.models import EventInput
from models.db_models import Event  # SQLAlchemy model
from db import SessionLocal  # SQLAlchemy session

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
    try:
        event_json = jsonable_encoder(event)
        r.lpush("event_queue", json.dumps(event_json))  # Push to Redis queue
        return {"status": "queued"}
    except Exception as e:
        print(f"[Error] Could not queue event: {e}")
        raise HTTPException(status_code=500, detail="Failed to queue event")

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
