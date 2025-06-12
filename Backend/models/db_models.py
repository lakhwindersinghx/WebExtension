from sqlalchemy import Column, String, Float, Text, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    user_id = Column(String, index=True) 
    id = Column(Integer, primary_key=True, index=True)
    tab_url = Column(Text)
    title = Column(Text)
    scroll_depth = Column(Float)
    duration_seconds = Column(Float)
    category = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True))

class AFKEvent(Base): 
    __tablename__ = "afk_events"  
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    state = Column(String, nullable=False) # String instead of Text for small fixed values like "start"/"end"
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)

