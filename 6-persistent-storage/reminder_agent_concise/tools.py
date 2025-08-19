from models import add_reminder, get_reminders, delete_reminder

def add_reminder_tool(message, due_time=None):
    add_reminder(message, due_time)
    return f"✅ Reminder added: {message}"

def view_reminders_tool():
    reminders = get_reminders()
    if not reminders:
        return "📭 No reminders found."
    return "\n".join([f"{r[0]}. {r[1]} (Due: {r[2]})" for r in reminders])

def delete_reminders_tool(reminder_id):
    delete_reminder(reminder_id)
    return f"🗑️ Reminder {reminder_id} deleted."
