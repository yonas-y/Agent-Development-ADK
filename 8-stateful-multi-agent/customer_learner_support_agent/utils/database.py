import sqlite3
from config import DB_PATH

# ------------------------------
# Initialize all tables
# ------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # # Courses table
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS courses (
    #         course_id TEXT PRIMARY KEY,
    #         course_name TEXT NOT NULL,
    #         description TEXT,
    #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #     )
    # """)

    # # Enrollments table
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS enrollments (
    #         enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         user_id TEXT NOT NULL,
    #         course_id TEXT NOT NULL,
    #         enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    #         completion_status TEXT DEFAULT 'in_progress',
    #         FOREIGN KEY (user_id) REFERENCES users(user_id),
    #         FOREIGN KEY (course_id) REFERENCES courses(course_id)
    #     )
    # """)

    # # Interactions table
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS interactions (
    #         interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         user_id TEXT NOT NULL,
    #         course_id TEXT NOT NULL,
    #         activity TEXT NOT NULL,
    #         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    #         FOREIGN KEY (user_id) REFERENCES users(user_id),
    #         FOREIGN KEY (course_id) REFERENCES courses(course_id)
    #     )
    # """)

    # # Feedback table
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS feedback (
    #         feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         user_id TEXT NOT NULL,
    #         course_id TEXT NOT NULL,
    #         rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    #         comments TEXT,
    #         submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    #         FOREIGN KEY (user_id) REFERENCES users(user_id),
    #         FOREIGN KEY (course_id) REFERENCES courses(course_id)
    #     )
    # """)

    conn.commit()
    conn.close()


# ------------------------------
# User Helper Functions
# ------------------------------
def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, user_name, email FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def create_user(user_id, user_name, email=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, user_name, email) VALUES (?, ?, ?)",
        (user_id, user_name, email)
    )
    conn.commit()
    conn.close()


# ------------------------------
# Course Helper Functions
# ------------------------------
def create_course(course_id, course_name, description=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (course_id, course_name, description) VALUES (?, ?, ?)",
        (course_id, course_name, description)
    )
    conn.commit()
    conn.close()


def get_course(course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
    course = cursor.fetchone()
    conn.close()
    return course


# ------------------------------
# Enrollment Helper Functions
# ------------------------------
def enroll_user_in_course(user_id, course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enrollments (user_id, course_id) VALUES (?, ?)",
        (user_id, course_id)
    )
    conn.commit()
    conn.close()


def get_enrollments(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enrollments WHERE user_id = ?", (user_id,))
    enrollments = cursor.fetchall()
    conn.close()
    return enrollments


# ------------------------------
# Interaction Helper Functions
# ------------------------------
def log_interaction(user_id, course_id, activity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO interactions (user_id, course_id, activity) VALUES (?, ?, ?)",
        (user_id, course_id, activity)
    )
    conn.commit()
    conn.close()


# ------------------------------
# Feedback Helper Functions
# ------------------------------
def add_feedback(user_id, course_id, rating, comments=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (user_id, course_id, rating, comments) VALUES (?, ?, ?, ?)",
        (user_id, course_id, rating, comments)
    )
    conn.commit()
    conn.close()
