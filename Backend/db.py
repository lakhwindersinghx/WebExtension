import sqlite3
from models import EventInput
from urllib.parse import urlparse

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
            category TEXT
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
    category = categorize_url(event.tab_url)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (tab_url, title, scroll_depth, category)
        VALUES (?, ?, ?, ?)
    ''', (event.tab_url, event.title, event.scroll_depth, category))
    conn.commit()
    conn.close()

def fetch_events():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT tab_url, title, scroll_depth, category FROM events ORDER BY id DESC LIMIT 50')
    rows = cursor.fetchall()
    conn.close()
    return [
        {"tab_url": row[0], "title": row[1], "scroll_depth": row[2], "category": row[3]}
        for row in rows
    ]
