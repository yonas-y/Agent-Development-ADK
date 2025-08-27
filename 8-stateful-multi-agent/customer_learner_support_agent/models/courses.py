from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String)

    # One-to-many relationship: one course can be purchased many times
    purchases = relationship("Purchase", back_populates="course")
