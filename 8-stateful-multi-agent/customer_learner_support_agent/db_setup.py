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
from models.courses import create_course
from database import Course
from sqlalchemy import text

# ------------------------------
# Define sample courses
# ------------------------------
sample_courses = [
    {
        "id": "CE101",
        "name": "Digital Logic Design",
        "duration": 15,
        "price": 99.99,
        "description": "Learn fundamentals of digital circuits, logic gates, "
        "combinational and sequential circuits."
    },
    {
        "id": "CE102",
        "name": "Computer Architecture",
        "duration": 20,
        "price": 159.99,
        "description": "Understand CPU design, memory hierarchy, "
        "instruction set architectures, and pipelining."
    },
    {
        "id": "CE103",
        "name": "Embedded Systems",
        "duration": 20,
        "price": 199.99,
        "description": "Design and program microcontrollers and embedded devices "
        "for real-time applications."
    },
    {
        "id": "CE104",
        "name": "Data Structures and Algorithms",
        "duration": 20,
        "price": 199.99,
        "description": "Explore fundamental data structures, algorithm design, "
        "and complexity analysis."
    },
    {
        "id": "CE105",
        "name": "Operating Systems",
        "duration": 20,
        "price": 199.99,
        "description": "Learn about processes, threads, scheduling, memory management, "
        "and file systems."
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
                create_course(course_id=course["id"], 
                              name=course["name"], 
                              duration=course["duration"],                               
                              price=course["price"],
                              description=course["description"]
                               )
                print(f"➕  Added course: {course['name']}")
            else:
                # Update existing course.
                db_course = session.query(Course).filter(Course.id == course["id"]).first()
                db_course.name = course["name"]
                db_course.description = course["description"]
                db_course.duration = course["duration"]
                db_course.price = course["price"]

                session.commit()
                print(f"🔄 Updated course: {course['name']}")

    print("🎉 Database setup complete!")

if __name__ == "__main__":
    main()
