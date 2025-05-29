from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import init_db, insert_event, fetch_events
from models import EventInput
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI




app = FastAPI()



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
    insert_event(event)
    return {"status": "success", "message": "Event tracked."}



@app.get("/events")
def get_events():
    return fetch_events()
