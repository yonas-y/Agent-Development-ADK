# In-memory reminders storage
from utils import parse_due_date
import database as db

def add_reminder(user_id: str, description: str, due_date: str = None, remark: str = None) -> str:
    """Add a new reminder. 
    Args:
        description: What the reminder is about.
        due_date: Optional due date (e.g. 'tomorrow', '2025-08-21', 'Friday').
        remark: Optional extra note.
    Returns:
        Confirmation message with reminder details.
    """
    # Convert natural language dates to proper datetime string
    due_date_parsed = parse_due_date(due_date) if due_date else None
    db.add_reminder_db(user_id, description, due_date_parsed, remark)

    return (
        f"✅ Reminder added:\n"
        f"   Description: {description}\n"
        f"   Due Date: {due_date_parsed or 'Not specified'}"
        + (f"\n   Remark: {remark or ' '}" if remark else "")
    )


# View reminders
def view_reminders(user_id: str) -> str:
    """List all reminders for a user."""
    reminders = db.get_reminders_db(user_id)
    if not reminders:
        return "📭 You have no reminders."

    formatted = []
    for i, r in enumerate(reminders, start=1):
        entry = (
            f"{i}. \n"
            f"   Description: {r['description']}\n"
            f"   Due Date: {r['due_date']}\n"
            f"   Remark: {r['remark'] or ' '}"
        )
        formatted.append(entry)
    return "\n\n".join(formatted)


# Update reminder by index (1-based)
def update_reminder(user_id: str, index: int, new_text: str) -> str:
    reminders = db.get_reminders_db(user_id)
    if 0 < index <= len(reminders):
        reminder_id = reminders[index - 1]['id']
        db.update_reminder_db(reminder_id, description=new_text)
        return f"✏️ Updated reminder '{reminders[index - 1]['description']}' -> '{new_text}'"
    return "❌ Reminder not found."


# Delete reminder by index (1-based)
def delete_reminder(user_id: str, index: int) -> str:
    reminders = db.get_reminders_db(user_id)
    if 0 < index <= len(reminders):
        reminder_id = reminders[index - 1]['id']
        db.delete_reminder_db(reminder_id)
        return f"🗑️ Deleted reminder: {reminders[index - 1]['description']}"
    return "❌ Reminder not found."