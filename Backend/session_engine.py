from datetime import datetime, timedelta
from typing import List, Literal, Dict
from models.db_models import Event, AFKEvent

# Topic: Datetime range operations Python
TimeBlock = Dict[str, datetime | Literal['active', 'idle', 'break']]


def build_session_blocks(events: List[Event], afk_events: List[AFKEvent]) -> List[TimeBlock]:
    """
    Merge AFK and activity events into a sorted list of time blocks labeled as active, idle, or break.
    """
    # Topic: Interval merging algorithm
    # Sort both lists by timestamp
    events = sorted(events, key=lambda e: e.timestamp)
    afk_events = sorted(afk_events, key=lambda a: a.timestamp)

    blocks = []
    afk_state = None
    afk_pointer = 0
    current_time = None

    for event in events:
        start = event.timestamp
        end = start + timedelta(seconds=event.duration_seconds or 0)  # Topic: Datetime range operations Python

        # Advance through AFK events to find overlaps
        while afk_pointer < len(afk_events) and afk_events[afk_pointer].timestamp <= end:
            afk = afk_events[afk_pointer]

            if afk.state == 'start' and afk.timestamp > start:
                blocks.append({"start": start, "end": afk.timestamp, "type": "active"})
                start = afk.timestamp
            elif afk.state == 'end':
                blocks.append({"start": start, "end": afk.timestamp, "type": "idle"})
                start = afk.timestamp

            afk_pointer += 1

        # Whatever is left after AFK overlap
        if start < end:
            blocks.append({"start": start, "end": end, "type": "active"})

    return blocks


# Example stub for summary endpoint logic
def summarize_day(blocks: List[TimeBlock]) -> Dict:
    total_minutes = 0
    idle_minutes = 0
    streak = 0
    current_streak = 0

    for block in blocks:
        # Topic: Time bucket aggregation Python / Sliding window algorithm explained
        duration = (block["end"] - block["start"]).total_seconds() / 60
        total_minutes += duration

        if block["type"] == "idle":
            idle_minutes += duration
            current_streak = 0  # Reset streak on idle
        else:
            current_streak += duration  # Extend streak
            streak = max(streak, current_streak)  # Track max streak

    return {
        "total_active_minutes": int(total_minutes - idle_minutes),
        "idle_percentage": round((idle_minutes / total_minutes) * 100, 1) if total_minutes > 0 else 0,
        "streak_minutes": int(streak),
        "top_categories": []  # Placeholder: to be added using Event.category counts
    }

# Topic for API layer (not shown here):
# "Flask/FastAPI build REST API"
# "How to return JSON in FastAPI"
# "How to query PostgreSQL by date and user_id"
# "LRU Cache Python" (if summary results are cached per day)
