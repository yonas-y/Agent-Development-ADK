import sqlite3
from contextlib import contextmanager


@contextmanager
def get_connection(db_path: str):
    """
    Context manager that yields a database connection.
    Ensures connection is properly closed even on error.
    """
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


def create_schema(conn: sqlite3.Connection):
    """Create reminders table if not exists."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            reminder_text TEXT NOT NULL,
            due_date TEXT
        )
    """)
    conn.commit()


def init_db(db_path: str):
    """Initialize the database with schema."""
    with get_connection(db_path) as conn:
        create_schema(conn)
