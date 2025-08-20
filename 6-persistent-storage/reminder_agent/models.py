from database import get_connection

def add_reminder(user_id, message, due_time=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (user_id, message, due_time) VALUES (?, ?, ?)", 
                   (user_id, message, due_time))
    conn.commit()
    conn.close()

def get_reminders(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, message, due_time FROM reminders WHERE user_id = ?", (user_id,))
    reminders = cursor.fetchall()
    conn.close()
    return reminders

def delete_reminder(user_id, reminder_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reminders WHERE id = ? AND user_id = ?", (reminder_id, user_id))
    conn.commit()
    conn.close()
