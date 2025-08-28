"""
database.py

Persistent database operations for the Customer/Learner Support Agent project.
Uses SQLAlchemy ORM for all CRUD operations.

Tables:
- User
- Course
- Enrollment
- Purchase
- Interaction
- Feedback

All operations use SessionLocal from db_session_service.py.

"""

from sqlalchemy import Column, String, Integer, Float, Numeric
from sqlalchemy import ForeignKey, DateTime, Text, CheckConstraint
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
    purchases = relationship("Purchase", back_populates="user")


class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    duration= Column(Float, nullable=False)  # duration in hours.
    price= Column(Numeric(10, 2), nullable=False)   # Price in dollars.
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    enrollments = relationship("Enrollment", back_populates="course")
    interactions = relationship("Interaction", back_populates="course")
    feedbacks = relationship("Feedback", back_populates="course")
    purchases = relationship("Purchase", back_populates="course")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="completed")  # completed | canceled | refunded
    canceled_at = Column(DateTime, nullable=True)
    refunded_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="purchases")
    course = relationship("Course", back_populates="purchases")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(String, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    completion_status = Column(String, default="in_progress")

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(String, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.id"), nullable=True)
    activity = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interactions")
    course = relationship("Course", back_populates="interactions")


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(String, primary_key=True, autoincrement=True)
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
