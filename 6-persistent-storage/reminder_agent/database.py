import sqlite3
from contextlib import contextmanager
import logging

DB_PATH = "reminders.db"

@contextmanager
def get_connection(db_path: str = DB_PATH):
    """Context manager to yield a SQLite connection safely."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


def create_schema(conn: sqlite3.Connection):
    """Create reminders and sessions tables if they do not exist."""
    cursor = conn.cursor()
    
    # Reminders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            message TEXT NOT NULL,
            due_time TEXT
        )
    """)
    
    # Sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT NOT NULL,
            user_id TEXT NOT NULL,
            state TEXT DEFAULT '{}'
        )
    """)
    
    conn.commit()


def init_db(db_path: str = DB_PATH):
    """Initialize database schema."""
    with get_connection(db_path) as conn:
        create_schema(conn)
    logging.info(f"Database initialized at {db_path}.")
