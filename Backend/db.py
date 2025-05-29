import sqlite3
from models import EventInput
from urllib.parse import urlparse
from datetime import datetime

DB_FILE = "events.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tab_url TEXT,
            title TEXT,
            scroll_depth REAL,
            duration_seconds INTEGER,
            category TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def categorize_url(url):
    domain = urlparse(url).netloc.lower()
    if "youtube" in domain or "netflix" in domain:
        return "entertainment"
    elif "linkedin" in domain or "glassdoor" in domain:
        return "job search"
    elif "google" in domain or "wikipedia" in domain:
        return "research"
    elif "instagram" in domain or "twitter" in domain:
        return "social media"
    else:
        return "other"

def insert_event(event: EventInput):
    category = event.category or categorize_url(event.tab_url)
    timestamp = event.timestamp or datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (tab_url, title, scroll_depth, duration_seconds, category, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        event.tab_url,
        event.title,
        event.scroll_depth,
        event.duration_seconds,
        category,
        timestamp
    ))
    conn.commit()
    conn.close()

def fetch_events():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, tab_url, title, scroll_depth, duration_seconds, category, timestamp
        FROM events
        ORDER BY id DESC
        LIMIT 50
    ''')
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "tab_url": row[1],
            "title": row[2],
            "scroll_depth": row[3],
            "duration_seconds": row[4],
            "category": row[5],
            "timestamp": row[6]
        }
        for row in rows
    ]
