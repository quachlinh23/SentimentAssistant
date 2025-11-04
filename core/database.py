# core/database.py
import sqlite3
from datetime import datetime
from config.settings import DB_PATH, HISTORY_LIMIT

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def save_result(text: str, sentiment: str):
    conn = sqlite3.connect(DB_PATH)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO sentiments (text, sentiment, timestamp) VALUES (?, ?, ?)",
        (text, sentiment, timestamp)
    )
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT text, sentiment, timestamp FROM sentiments ORDER BY timestamp DESC"
    )
    history = cursor.fetchall()
    conn.close()
    return history