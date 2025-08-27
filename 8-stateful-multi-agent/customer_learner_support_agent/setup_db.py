"""
setup_db.py

This script initializes the SQLite database for the Customer/Learner Support Agent
project. It performs the following tasks:

1. Creates all necessary tables (users, courses, purchases) if they do not exist.
2. Seeds the database with initial courses related to computer engineering.

Usage:
------
Run this script once before starting the main application to ensure the database
and initial data are ready.

Example:
    python setup_db.py
"""

from sqlalchemy.orm import Session
from db_session_service import engine
from base import Base
from models.courses import Course

# 1️⃣ Create tables
Base.metadata.create_all(bind=engine)

# 2️⃣ Seed initial courses
courses = [
    {
        "title": "Introduction to Computer Architecture",
        "description": "Fundamentals of digital logic, CPU design, memory hierarchy, and instruction set architectures."
    },
    {
        "title": "Embedded Systems Design",
        "description": "Microcontrollers, real-time systems, and hardware-software co-design with hands-on C programming."
    },
    {
        "title": "Computer Networks & Security",
        "description": "Principles of TCP/IP, routing, switching, and cybersecurity basics including encryption and firewalls."
    },
    {
        "title": "Digital Signal Processing (DSP)",
        "description": "Signal processing, Fourier transforms, filtering, and applications in audio, image, and communications."
    },
    {
        "title": "Machine Learning for Engineers",
        "description": "Supervised and unsupervised learning with applications in predictive maintenance and anomaly detection."
    },
]

with Session(engine) as session:
    for c in courses:
        exists = session.query(Course).filter_by(title=c["title"]).first()
        if not exists:
            session.add(Course(title=c["title"], description=c["description"]))
    session.commit()

print("✅ Database setup complete and courses seeded.")
