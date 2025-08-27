"""
setup_db.py

Setup script for the Customer/Learner Support Agent database.

- Creates all tables: users, courses, enrollments, interactions, feedback.
- Seeds the database with sample computer engineering courses.
- Usage: run this script once before starting the main app.

Example:
    python setup_db.py
"""

from db_session_service import engine, SessionLocal
from base import Base
from database import create_course
from sqlalchemy import text

# ------------------------------
# Define sample courses
# ------------------------------
sample_courses = [
    {
        "id": "CE101",
        "name": "Digital Logic Design",
        "description": "Learn fundamentals of digital circuits, logic gates, combinational and sequential circuits."
    },
    {
        "id": "CE102",
        "name": "Computer Architecture",
        "description": "Understand CPU design, memory hierarchy, instruction set architectures, and pipelining."
    },
    {
        "id": "CE103",
        "name": "Embedded Systems",
        "description": "Design and program microcontrollers and embedded devices for real-time applications."
    },
    {
        "id": "CE104",
        "name": "Data Structures and Algorithms",
        "description": "Explore fundamental data structures, algorithm design, and complexity analysis."
    },
    {
        "id": "CE105",
        "name": "Operating Systems",
        "description": "Learn about processes, threads, scheduling, memory management, and file systems."
    },
]

def main():
    # ------------------------------
    # 1. Create all tables
    # ------------------------------
    print("🔧 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

    # ------------------------------
    # 2. Seed sample courses
    # ------------------------------
    print("🌱 Seeding sample courses...")
    for course in sample_courses:
        # Check if course exists before creating
        with SessionLocal() as session:
            existing = session.execute(
                text("SELECT id FROM courses WHERE id = :course_id"),
                {"course_id": course["id"]}
            ).fetchone()
            if not existing:
                create_course(course_id=course["id"], name=course["name"], description=course["description"])
                print(f"➕  Added course: {course['name']}")
            else:
                print(f"⚠️  Course already exists: {course['name']}")

    print("🎉 Database setup complete!")


if __name__ == "__main__":
    main()
