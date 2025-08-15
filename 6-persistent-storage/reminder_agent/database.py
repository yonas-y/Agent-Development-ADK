# ====== Handles storage operations. ====== #
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "reminders.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            title TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_reminder(user_name, title, time):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reminders (user_name, title, time) VALUES (?, ?, ?)",
        (user_name, title, time)
    )
    conn.commit()
    conn.close()

def get_reminders(user_name=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if user_name:
        cursor.execute("SELECT * FROM reminders WHERE user_name=?", (user_name,))
    else:
        cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_reminder(reminder_id, title=None, time=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if title and time:
        cursor.execute(
            "UPDATE reminders SET title=?, time=? WHERE id=?",
            (title, time, reminder_id)
        )
    elif title:
        cursor.execute(
            "UPDATE reminders SET title=? WHERE id=?",
            (title, reminder_id)
        )
    elif time:
        cursor.execute(
            "UPDATE reminders SET time=? WHERE id=?",
            (time, reminder_id)
        )
    conn.commit()
    conn.close()

def delete_reminder(reminder_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
    conn.commit()
    conn.close()
