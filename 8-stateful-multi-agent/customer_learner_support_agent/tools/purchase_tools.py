from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from db_session_service import SessionLocal
from database import Purchase   

def check_and_record_purchase(user_id: int, course_id: int) -> dict:
    """
    Check if the user has already purchased the course.
    If not, record it with timestamp.
    """
    try:
        with SessionLocal() as session:
            existing = session.query(Purchase).filter_by(user_id=user_id, course_id=course_id).first()
            if existing:
                return {
                    "status": "failed",
                    "message": "Course already purchased earlier.",
                    "purchase_date": existing.purchase_date.isoformat()
                }

            # Record new purchase
            new_purchase = Purchase(
                user_id=user_id,
                course_id=course_id,
                purchase_date=datetime.utcnow()
            )
            session.add(new_purchase)
            session.commit()

            return {
                "status": "success",
                "message": "Course purchased successfully.",
                "purchase_date": new_purchase.purchase_date.isoformat()
            }

    except SQLAlchemyError as e:
        # Rollback is automatic if exception occurs before commit
        return {"status": "error", "message": str(e)}
