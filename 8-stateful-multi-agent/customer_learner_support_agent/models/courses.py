from db_session_service import SessionLocal
from database import Course

# ------------------------------
# Helper Functions
# ------------------------------

def get_course(course_id: str):
    with SessionLocal() as session:
        return session.query(Course).filter_by(id=course_id).first()
    
    
def get_all_courses():
    """
    Retrieve all courses and return as a list of dictionaries for agent responses.
    """
    with SessionLocal() as session:
        courses = session.query(Course).all()
        return [
            {
                "id": c.id,
                "name": c.name,
                "duration": float(c.duration),
                "price": float(c.price),
                "description": c.description
            }
            for c in courses
        ]


def create_course(course_id: str, 
                  name: str, 
                  duration: float, 
                  price: float, 
                  description: str = None):
    with SessionLocal() as session:
        course = Course(id=course_id, 
                        name=name, 
                        duration=duration, 
                        price=price, 
                        description=description)
        session.add(course)
        session.commit()
        return course
    