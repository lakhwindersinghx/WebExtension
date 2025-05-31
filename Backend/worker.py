# worker.py

import redis
import json
from models.models import EventInput  # Pydantic validation
from db import SessionLocal
from models.db_models import Event  # SQLAlchemy model

r = redis.Redis(host='localhost', port=6379, db=0)

print("Worker started. Waiting for events...")

def store_event(event_data: EventInput):
    db = SessionLocal()
    try:
        db_event = Event(
            tab_url=event_data.tab_url,
            title=event_data.title,
            scroll_depth=event_data.scroll_depth,
            duration_seconds=event_data.duration_seconds,
            category=event_data.category,
            timestamp=event_data.timestamp
        )
        db.add(db_event)
        db.commit()
    except Exception as e:
        print(f"[DB ERROR] {e}")
        db.rollback()
    finally:
        db.close()

while True:
    _, raw = r.brpop("event_queue")  # blocking pop from Redis
    try:
        data = json.loads(raw)
        event = EventInput(**data)   # validate with Pydantic
        store_event(event)           # insert into PostgreSQL
        print(f"Stored event from: {event.tab_url}")
    except Exception as e:
        print(f"Error processing event: {e}")
