from db_session_service import SessionLocal
from database import Feedback

# ------------------------------
# Helper Functions
# ------------------------------

def add_feedback(user_id: str, course_id: str, rating: int, comments: str = None):
    with SessionLocal() as session:
        feedback = Feedback(user_id=user_id, 
                            course_id=course_id, 
                            rating=rating, 
                            comments=comments)
        session.add(feedback)
        session.commit()
        return feedback
