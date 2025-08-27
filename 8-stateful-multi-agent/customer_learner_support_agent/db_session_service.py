from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL

# SQLAlchemy engine
engine = create_engine(DB_URL, echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
