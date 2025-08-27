"""
database.py

Persistent database operations for the Customer/Learner Support Agent project.
Uses SQLAlchemy ORM for all CRUD operations.

Tables:
- User
- Course
- Enrollment
- Interaction
- Feedback

All operations use SessionLocal from db_session_service.py.

"""

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, CheckConstraint, func
from sqlalchemy.orm import relationship
from db_session_service import SessionLocal
from base import Base
from datetime import datetime

# ------------------------------
# Models
# ------------------------------
class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    enrollments = relationship("Enrollment", back_populates="user")
    interactions = relationship("Interaction", back_populates="user")
    feedbacks = relationship("Feedback", back_populates="user")


class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    enrollments = relationship("Enrollment", back_populates="course")
    interactions = relationship("Interaction", back_populates="course")
    feedbacks = relationship("Feedback", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    completion_status = Column(String, default="in_progress")

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=True)
    activity = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interactions")
    course = relationship("Course", back_populates="interactions")


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comments = Column(Text, nullable=True)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="rating_check"),
    )

    user = relationship("User", back_populates="feedbacks")
    course = relationship("Course", back_populates="feedbacks")


# ------------------------------
# Helper Functions
# ------------------------------
def get_user(user_id: str):
    with SessionLocal() as session:
        return session.query(User).filter_by(id=user_id).first()


def create_user(user_id: str, username: str, email: str = None):
    with SessionLocal() as session:
        user = User(id=user_id, username=username, email=email)
        session.add(user)
        session.commit()
        return user


def get_course(course_id: str):
    with SessionLocal() as session:
        return session.query(Course).filter_by(id=course_id).first()


def create_course(course_id: str, name: str, description: str = None):
    with SessionLocal() as session:
        course = Course(id=course_id, name=name, description=description)
        session.add(course)
        session.commit()
        return course


def enroll_user_in_course(user_id: str, course_id: str):
    with SessionLocal() as session:
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        session.add(enrollment)
        session.commit()
        return enrollment


def get_enrollments(user_id: str):
    with SessionLocal() as session:
        return session.query(Enrollment).filter_by(user_id=user_id).all()


def log_interaction(user_id: str, activity: str, course_id: str = None):
    with SessionLocal() as session:
        interaction = Interaction(user_id=user_id, activity=activity, course_id=course_id)
        session.add(interaction)
        session.commit()
        return interaction


def add_feedback(user_id: str, course_id: str, rating: int, comments: str = None):
    with SessionLocal() as session:
        feedback = Feedback(user_id=user_id, course_id=course_id, rating=rating, comments=comments)
        session.add(feedback)
        session.commit()
        return feedback
