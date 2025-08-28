from sqlalchemy.exc import IntegrityError
from db_session_service import SessionLocal
from database import Purchase
from datetime import datetime
from typing import Optional

# ------------------------------
# Helper Functions
# ------------------------------
    
def create_purchase(session,
                    user_id: str, 
                    course_id: str, 
                    purchase_date: datetime = None):
    """Low-level helper: inserts a purchase into DB."""
    purchase = Purchase(
        user_id=user_id,
        course_id=course_id,
        purchase_date=purchase_date or datetime.utcnow()
    )
    session.add(purchase)
    return purchase


def add_purchase(user_id: str, 
                 course_id: str, 
                 purchase_date: Optional[str] = None):
    """Always create a new purchase (may error if duplicate)."""
    with SessionLocal() as session:
        try:
            dt = datetime.fromisoformat(purchase_date) if purchase_date else datetime.utcnow()
            purchase = create_purchase(session, user_id, course_id, dt)
            session.commit()
            session.refresh(purchase)
            return purchase
        except IntegrityError:
            session.rollback()
            raise


def get_purchases(user_id: str):
    """Return all purchases of a user."""
    with SessionLocal() as session:
        return session.query(Purchase).filter_by(user_id=user_id).all()


def check_and_record_purchase(user_id: str, 
                              course_id: str, 
                              purchase_date: Optional[str] = None):
    """Only create purchase if it doesn't already exist."""
    with SessionLocal() as session:
        purchase = session.query(Purchase).filter_by(user_id=user_id, course_id=course_id).first()
        if purchase:
            return purchase

        # Parse purchase_date string if provided, otherwise use utcnow
        dt = datetime.fromisoformat(purchase_date) if purchase_date else datetime.utcnow()
        purchase = create_purchase(session, user_id, course_id, dt)
        session.commit()
        session.refresh(purchase)
        return purchase


def get_order_history(user_id: str):
    """Return all purchases made by a specific user."""
    with SessionLocal() as session:
        return session.query(Purchase).filter_by(user_id=user_id).all()


def get_purchase_details(order_id: int):
    """Return details of a specific purchase by its ID."""
    with SessionLocal() as session:
        return session.query(Purchase).filter_by(id=order_id).first()


def cancel_purchase(order_id: int):
    """Cancel a purchase if it's eligible for cancellation."""
    with SessionLocal() as session:
        purchase = session.query(Purchase).filter_by(id=order_id).first()
        if not purchase:
            return None

        # For simplicity, assume we just flag as 'canceled'
        purchase.status = "canceled"
        purchase.canceled_at = datetime.utcnow()
        session.commit()
        session.refresh(purchase)
        return purchase


def process_refund(order_id: int):
    """Process a refund for a given purchase."""
    with SessionLocal() as session:
        purchase = session.query(Purchase).filter_by(id=order_id).first()
        if not purchase:
            return None

        # Mark as refunded (you could also integrate with a payment API here)
        purchase.status = "refunded"
        purchase.refunded_at = datetime.utcnow()
        session.commit()
        session.refresh(purchase)
        return purchase
