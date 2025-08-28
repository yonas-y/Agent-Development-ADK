from db_session_service import SessionLocal
from database import Enrollment

# ------------------------------
# Helper Functions
# ------------------------------
def enroll_user_in_course(user_id: str, course_id: str):
    with SessionLocal() as session:
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        session.add(enrollment)
        session.commit()
        return enrollment


def get_enrollments(user_id: str):
    with SessionLocal() as session:
        return session.query(Enrollment).filter_by(user_id=user_id).all()


