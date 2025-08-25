from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from customer_learner_support_agent.config import DB_URL

Base = declarative_base()

class Interaction(Base):
    """
    ORM model for logging user interactions.
    """
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String(50), nullable=False)
    agent = Column(String(50), nullable=False)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DatabaseSessionService:
    """
    Service class for managing database sessions and logging interactions.
    """

    def __init__(self, db_url=DB_URL):
        """
        Initialize the database connection and create tables if they don't exist.
        """
        self.engine = create_engine(db_url, echo=False, future=True)
        Base.metadata.create_all(self.engine)  # Creates tables
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def log_interaction(self, user_id: str, agent: str, query: str, response: str):
        """
        Logs a user-agent interaction into the database.
        """
        session = self.SessionLocal()
        try:
            interaction = Interaction(
                user_id=user_id,
                agent=agent,
                query=query,
                response=response
            )
            session.add(interaction)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_interactions(self, user_id: str = None, agent: str = None):
        """
        Retrieve interactions from the database, optionally filtered by user_id or agent.
        """
        session = self.SessionLocal()
        try:
            query = session.query(Interaction)
            if user_id:
                query = query.filter(Interaction.user_id == user_id)
            if agent:
                query = query.filter(Interaction.agent == agent)
            return query.all()
        finally:
            session.close()
