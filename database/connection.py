import sqlite3
import os

DB_NAME = "vitacare.db"

SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "schema.sql")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    
    conn.row_factory = sqlite3.Row

    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_connection()
    try:
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            script = f.read()
        conn.executescript(script)
        conn.commit()
    finally:
        conn.close()