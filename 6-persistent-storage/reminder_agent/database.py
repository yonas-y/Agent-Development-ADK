import sqlite3
from typing import List, Dict, Optional
from config import DB_PATH

# Initialize the database and table
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            remark TEXT
        )
    """)
    conn.commit()
    conn.close()

# Add a new reminder
def add_reminder_db(user_id: str, description: str, due_date: str, remark: Optional[str] = None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO reminders (user_id, description, due_date, remark)
        VALUES (?, ?, ?, ?)
    """, (user_id, description, due_date, remark or ""))
    conn.commit()
    conn.close()

# Get all reminders for a user
def get_reminders_db(user_id: str) -> List[Dict]:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, description, due_date, remark FROM reminders WHERE user_id = ? ORDER BY due_date", (user_id,))
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "description": row[1], "due_date": row[2], "remark": row[3]} for row in rows]

# Update a reminder by ID
def update_reminder_db(reminder_id: int, description: Optional[str] = None, due_date: Optional[str] = None, remark: Optional[str] = None) -> bool:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    updates = []
    params = []

    if description is not None:
        updates.append("description = ?")
        params.append(description)
    if due_date is not None:
        updates.append("due_date = ?")
        params.append(due_date)
    if remark is not None:
        updates.append("remark = ?")
        params.append(remark)

    if not updates:
        return False

    params.append(reminder_id)
    query = f"UPDATE reminders SET {', '.join(updates)} WHERE id = ?"
    c.execute(query, tuple(params))
    conn.commit()
    updated = c.rowcount > 0
    conn.close()
    return updated

# Delete a reminder by ID
def delete_reminder_db(reminder_id: int) -> bool:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
    conn.commit()
    deleted = c.rowcount > 0
    conn.close()
    return deleted
