# database.py
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Tuple
import logging

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
            due_date TEXT NOT NULL
        )
    """)
    conn.commit()


def init_db(db_path: str):
    """Initialize the database with schema."""
    with get_connection(db_path) as conn:
        create_schema(conn)
    logging.info(f"Database initialized at {db_path}.")


def add_reminder(db_path: str, user_name: str, reminder_text: str, due_date: datetime):
    """
    Adds a new reminder to the database.
    
    Args:
        db_path (str): Path to the database file.
        user_name (str): The name of the user.
        reminder_text (str): The text of the reminder.
        due_date (datetime): The scheduled datetime for the reminder.
    """
    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (user_name, reminder_text, due_date) VALUES (?, ?, ?)",
            (user_name, reminder_text, due_date.isoformat())
        )
        conn.commit()
    logging.info(f"Added reminder for user '{user_name}'.")


def get_reminders(db_path: str, user_name: str) -> List[Tuple]:
    """
    Retrieves all reminders for a given user from the database.
    
    Args:
        db_path (str): Path to the database file.
        user_name (str): The name of the user.
        
    Returns:
        A list of tuples, where each tuple is a reminder record.
    """
    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, reminder_text, due_date FROM reminders WHERE user_name = ? ORDER BY due_date ASC",
            (user_name,)
        )
        reminders = cursor.fetchall()
    logging.info(f"Retrieved {len(reminders)} reminders for user '{user_name}'.")
    return reminders


def delete_reminder(db_path: str, reminder_id: int):
    """
    Deletes a reminder by its ID from the database.
    
    Args:
        db_path (str): Path to the database file.
        reminder_id (int): The ID of the reminder to delete.
    """
    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
        conn.commit()
    logging.info(f"Deleted reminder with ID {reminder_id}.")

