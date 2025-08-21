from google.adk.sessions import DatabaseSessionService
from config import DB_URL, APP_NAME

# Initial state for a new session
initial_state = {
    "reminders": []
}

# Initialize session persistence
session_service = DatabaseSessionService(db_url=DB_URL)

async def get_or_create_session(user_id: str):
    """Retrieve an existing session or create a new one for the user."""
    existing_sessions = await session_service.list_sessions(
        app_name=APP_NAME,
        user_id=user_id,
    )

    if existing_sessions.sessions:
        session_id = existing_sessions.sessions[0].id
        print(f"Continuing with existing session: {session_id}")
        return session_id

    new_session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        state=initial_state,
    )
    print(f"Created new session: {new_session.id}")
    return new_session.id

async def get_session_state(user_id: str, session_id: str):
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
    )
    return session.state

async def update_session_state(user_id: str, session_id: str, new_state: dict):
    await session_service.update_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
        state=new_state,
    )
    