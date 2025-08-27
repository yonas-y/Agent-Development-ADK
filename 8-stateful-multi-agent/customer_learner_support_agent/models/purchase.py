from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from customer_learner_support_agent.models.base import Base
import datetime


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    purchased_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Optional: relationships to link users and courses
    user = relationship("User", back_populates="purchases")
    course = relationship("Course", back_populates="purchases")
