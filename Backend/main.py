import redis
import json 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import init_db, insert_event, fetch_events
from models import EventInput
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI




app = FastAPI()

r = redis.Redis(host='localhost', port=6379, db=0)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set to specific origins like ["chrome-extension://<your-extension-id>"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    init_db()

@app.post("/track-event")
async def track_event(event: EventInput):
    print(event.dict())
    event_json = jsonable_encoder(event) #serialising datetime
    r.lpush("event_queue", json.dumps(event_json))  # Push to queue
    # insert_event(event)
    # return {"status": "success", "message": "Event tracked."}
    return {"status": "queued"}



@app.get("/events")
def get_events():
    return fetch_events()
