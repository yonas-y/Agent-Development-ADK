from database import get_connection

def add_reminder(message, due_time=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (message, due_time) VALUES (?, ?)", (message, due_time))
    conn.commit()
    conn.close()

def get_reminders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, message, due_time FROM reminders")
    reminders = cursor.fetchall()
    conn.close()
    return reminders

def delete_reminder(reminder_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()
