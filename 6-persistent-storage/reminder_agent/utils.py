# utils.py
from datetime import datetime

def format_reminder(reminder: tuple) -> str:
    """Format reminder row from DB into a readable string."""
    reminder_id, user_name, text, due_date = reminder
    return f"[{reminder_id}] {text} (due: {due_date}, user: {user_name})"

def parse_due_date(due_date_str: str) -> str:
    """
    Convert input date string into ISO format.
    For now, assume 'YYYY-MM-DD HH:MM' format.
    """
    try:
        dt = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        return dt.isoformat()
    except ValueError:
        raise ValueError("Due date must be in 'YYYY-MM-DD HH:MM' format.")

def validate_reminder_text(text: str) -> str:
    """Ensure reminder text is not empty."""
    text = text.strip()
    if not text:
        raise ValueError("Reminder text cannot be empty.")
    return text
