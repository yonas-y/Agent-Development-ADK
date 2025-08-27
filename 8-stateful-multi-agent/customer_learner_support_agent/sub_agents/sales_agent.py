from google.adk.agents import Agent
from google.adk.sessions import DatabaseSessionService
from google.adk.tools import FunctionTool
from customer_learner_support_agent.config import DB_URL
from customer_learner_support_agent.models.purchase import Purchase
from datetime import datetime

db_session_service = DatabaseSessionService(DB_URL)

def check_and_record_purchase(user_id: int, course_id: int) -> dict:
    """
    Check if the user has already purchased the course.
    If not, record it with timestamp.
    """
    session = db_session_service.get_session()
    try:
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
    except Exception as e:
        session.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        session.close()

sales_agent_instruction = """
You are the **Sales Agent**, responsible for handling course sales, promotions, 
and purchase-related inquiries. Your responsibilities include:

1. **Course Availability & Purchase Validation**:
   - Before confirming a course purchase, check if the learner has already bought 
     the course using the `check_course_purchase_tool`.
   - If the course has already been purchased, inform the learner and prevent 
     duplicate purchases.
   - If the course is not yet purchased, proceed with the transaction.

2. **Purchase Recording**:
   - Every successful course purchase must be stored in the database, 
     including:
       - User ID
       - Course ID
       - Purchase date/time
   - This ensures transaction history is preserved for customer support, 
     return policy eligibility, and personalized recommendations.

3. **Sales Support**:
   - Provide learners with information about pricing, promotions, and bundles.
   - Suggest complementary or recommended courses based on the learner's 
     past purchases.

4. **Refund and Policy Awareness**:
   - Reference company policy for refunds, return windows, or cancellations.
   - Ensure recorded purchase timestamps are used to determine refund eligibility.

Guidelines:
- Always prevent duplicate course purchases for the same user.
- Store transactions consistently with timestamps for traceability.
- Maintain a professional and persuasive sales tone while prioritizing learner value.
"""

sales_agent = Agent(
    name="sales_agent",
    model="gemini-2.0-flash",
    description="Sales Agent handling inquiries related to educational " \
    "sales, promotions, and course recommendations.",
    instruction=sales_agent_instruction,
    tools=[
        FunctionTool(check_and_record_purchase),
        ]
)
