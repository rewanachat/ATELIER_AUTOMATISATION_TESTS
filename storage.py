
import sqlite3
import json
from datetime import datetime

DB_PATH = "runs.db"

def _init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            result_json TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_run(result: dict):
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO runs (timestamp, result_json) VALUES (?, ?)",
        (datetime.now().isoformat(), json.dumps(result)),
    )
    conn.commit()
    conn.close()

def list_runs():
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT timestamp, result_json FROM runs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return [(ts, json.loads(rj)) for ts, rj in rows]
