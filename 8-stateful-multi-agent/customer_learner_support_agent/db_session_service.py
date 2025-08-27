"""
db_session_service.py

This module sets up the SQLAlchemy database connection and session factory
for the Customer/Learner Support Agent project.

It provides:

1. 'engine' - The SQLAlchemy engine used to connect to the SQLite database.
2. 'SessionLocal' - A session factory to create database sessions for ORM operations.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL

# SQLAlchemy engine
engine = create_engine(DB_URL, echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
