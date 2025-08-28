from db_session_service import SessionLocal
from database import Interaction

# ------------------------------
# Helper Functions
# ------------------------------
def log_interaction(user_id: str, activity: str, course_id: str = None):
    with SessionLocal() as session:
        interaction = Interaction(user_id=user_id, activity=activity, course_id=course_id)
        session.add(interaction)
        session.commit()
        return interaction
