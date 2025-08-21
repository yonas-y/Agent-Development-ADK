# In-memory reminders storage
from utils import parse_due_date

REMINDERS = {}  # user_id -> list of reminders

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

    if user_id not in REMINDERS:
        REMINDERS[user_id] = []

    reminder = {
        "description": description,
        "due_date": due_date_parsed or "Not specified",
        "remark": remark or " "
    }
    REMINDERS[user_id].append(reminder)

    return (
        f"✅ Reminder added:\n"
        f"   Description: {reminder['description']}\n"
        f"   Due Date: {reminder['due_date']}"
        + (f"\n   Remark: {reminder['remark']}" if reminder['remark'] else "")
    )


# View reminders
def view_reminders(user_id: str) -> str:
    """List all reminders for a user."""
    user_reminders = REMINDERS.get(user_id, [])
    if not user_reminders:
        return "📭 You have no reminders."

    formatted = []
    for i, r in enumerate(user_reminders, start=1):
        entry = (
            f"{i}. \n"
            f"   Description: {r['description']}\n"
            f"   Due Date: {r['due_date']}\n"
            f"   Remark: {r['remark'] or ' '}"
        )
        formatted.append(entry)
    return "\n\n".join(formatted)


def update_reminder(user_id: str, index: int, description: str = None, due_date: str = None, remark: str = None) -> str:
    user_reminders = REMINDERS.get(user_id, [])
    if 0 < index <= len(user_reminders):
        reminder = user_reminders[index - 1]
        if description:
            reminder["description"] = description
        if due_date:
            reminder["due_date"] = parse_due_date(due_date)
        if remark is not None:
            reminder["remark"] = remark
        return f"✏️ Updated reminder {index}: {reminder}"
    return "❌ Reminder not found."


def delete_reminder(user_id: str, index: int) -> str:
    """Delete a reminder by index (1-based)."""
    user_reminders = REMINDERS.get(user_id, [])
    if 0 < index <= len(user_reminders):
        removed = user_reminders.pop(index - 1)
        return f"🗑️ Deleted reminder: {removed['description']} (Due: {removed['due_date']})"
    return "❌ Reminder not found."
