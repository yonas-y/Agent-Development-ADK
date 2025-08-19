import sqlite3

DB_NAME = "reminders.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        message TEXT NOT NULL,
                        due_time TEXT
                    )''')
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)
