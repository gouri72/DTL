import sqlite3
from config import Config

def init_database():
    conn = sqlite3.connect(Config.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS disaster_news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            content TEXT NOT NULL,
            disaster_type TEXT,
            location TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            url TEXT,
            author TEXT,
            relevance_score REAL
        )
    """)

    conn.commit()
    conn.close()


def save_to_database(data):
    conn = sqlite3.connect(Config.DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO disaster_news
        (source, content, disaster_type, location, url, author, relevance_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("source"),
        data.get("content"),
        data.get("disaster_type"),
        data.get("location"),
        data.get("url"),
        data.get("author"),
        data.get("relevance_score", 0.0),
    ))

    conn.commit()
    conn.close()
