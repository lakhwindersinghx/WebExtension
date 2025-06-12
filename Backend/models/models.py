from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventInput(BaseModel):
    tab_url: str
    title: str
    scroll_depth: float
    duration_seconds: Optional[float] = None  # Optional if browser doesn't always send it
    category: Optional[str] = None
    timestamp: Optional[datetime] = None      # Optional if backend auto-generates it

class AFKEventInput(BaseModel):
    state: str  # "start" or "end"
    timestamp: datetime

class AFKEventOutput(BaseModel):
    id: int
    state: str
    timestamp: datetime

    class Config:
        orm_mode = True
    