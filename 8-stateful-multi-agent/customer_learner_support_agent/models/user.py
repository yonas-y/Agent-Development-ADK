from db_session_service import SessionLocal
from database import User


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
