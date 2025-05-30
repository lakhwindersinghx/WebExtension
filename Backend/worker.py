# worker.py
import redis
import json
import time
from db import insert_event  # Reuse DB insert logic
from models import EventInput

r = redis.Redis(host='localhost', port=6379, db=0)

print("Worker started. Waiting for events...")

while True:
    _, raw = r.brpop("event_queue")  # blocking pop
    try:
        data = json.loads(raw)
        event = EventInput(**data)
        insert_event(event)
        print(f"Processed event: {event.tab_url}")
    except Exception as e:
        print(f"Error processing: {e}")
