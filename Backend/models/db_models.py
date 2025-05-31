from sqlalchemy import Column, String, Float, Text, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    tab_url = Column(Text)
    title = Column(Text)
    scroll_depth = Column(Float)
    duration_seconds = Column(Float)
    category = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True))
