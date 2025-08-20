# In-memory reminders storage
REMINDERS = {}  # user_id -> list of reminders

# Add a reminder
def add_reminder(user_id: str, text: str) -> str:
    if user_id not in REMINDERS:
        REMINDERS[user_id] = []
    REMINDERS[user_id].append(text)
    return f"✅ Reminder added: {text}"

# View reminders
def view_reminders(user_id: str) -> str:
    user_reminders = REMINDERS.get(user_id, [])
    if not user_reminders:
        return "📭 You have no reminders."
    return "\n".join([f"{i+1}. {r}" for i, r in enumerate(user_reminders)])

# Update reminder by index (1-based)
def update_reminder(user_id: str, index: int, new_text: str) -> str:
    user_reminders = REMINDERS.get(user_id, [])
    if 0 < index <= len(user_reminders):
        old = user_reminders[index - 1]
        user_reminders[index - 1] = new_text
        return f"✏️ Updated reminder '{old}' -> '{new_text}'"
    return "❌ Reminder not found."

# Delete reminder by index (1-based)
def delete_reminder(user_id: str, index: int) -> str:
    user_reminders = REMINDERS.get(user_id, [])
    if 0 < index <= len(user_reminders):
        removed = user_reminders.pop(index - 1)
        return f"🗑️ Deleted reminder: {removed}"
    return "❌ Reminder not found."
