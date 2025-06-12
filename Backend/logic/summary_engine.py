from typing import List, Dict
from datetime import datetime

TimeBlock = Dict[str, datetime | str]

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


