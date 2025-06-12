from datetime import datetime, timedelta
from typing import List, Literal, Dict
from models.db_models import Event, AFKEvent

# Topic: Datetime range operations Python

#declaring a return type: list of dicts in format 
#{"start":datetime, "end":datetime, "type":"active/idle/break"}

TimeBlock=Dict[str, datetime | Literal['active', 'idle', 'break']]

#This function definition uses Python type annotations
#The function returns a list of TimeBlock dictionaries. as defined up above
def build_session_blocks(events: List[Event], afk_events: List[AFKEvent])-> List[TimeBlock]:


 #This tells sorted() to sort the list using each elements .timestamp field. 
 #lambda e: defines an anonymous function that takes an event e
 #e.timestamp returns the time the event started"""
 
    events = sorted(events, key=lambda e: e.timestamp)
    afk_events = sorted(afk_events, key=lambda a: a.timestamp)
    
    ResultBlocks = [] #final list with merged sessions
    afk_state = None 
    afk_pointer = 0
    current_time = None

    for event in events:
        start=event.timestamp
        end=start + timedelta(seconds=event.duration_seconds or 0) #Datetime range operations Python

        while afk_pointer < len(afk_events) and afk_events[afk_pointer].timestamp <= end:
            afk = afk_events[afk_pointer]

            if afk.state == 'start' and afk.timestamp > start:
                ResultBlocks.append({"start": start, "end": afk.timestamp, "type": "active"})
                start = afk.timestamp
            elif afk.state == 'end':
                ResultBlocks.append({"start": start, "end": afk.timestamp, "type": "idle"})
                start = afk.timestamp
        afk_pointer += 1

        if start < end:
            ResultBlocks.append({"start": start, "end": end, "type": "active"})

    return ResultBlocks    