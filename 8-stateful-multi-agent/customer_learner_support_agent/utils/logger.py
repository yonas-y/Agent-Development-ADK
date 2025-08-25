from .db_session_service import DatabaseSessionService
from config import DB_URL

# Initialize DB session service (you could also inject this later)
db_service = DatabaseSessionService(db_url=DB_URL)

def log_interaction(user_id: str, query: str, response: str, agent: str = "root_agent"):
    """
    Logs an interaction into the database.
    """
    db_service.log_interaction(
        user_id=user_id,
        agent=agent,
        query=query,
        response=response
    )
    return {"status": "logged"}
