from models import add_reminder, get_reminders, delete_reminder

def add_reminder_tool(user_id, message, due_time=None):
    add_reminder(user_id, message, due_time)
    return f"✅ Reminder added: {message}"

def view_reminders_tool(user_id):
    reminders = get_reminders(user_id)
    if not reminders:
        return "📭 No reminders found."
    return "\n".join([f"{r[0]}. {r[1]} (Due: {r[2]})" for r in reminders])

def delete_reminders_tool(user_id, reminder_id):
    delete_reminder(user_id, reminder_id)
    return f"🗑️ Reminder {reminder_id} deleted."
