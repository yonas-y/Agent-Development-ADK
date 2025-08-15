import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService, Session
from memory_agent.agent import memory_agent
# from utils import call_agent_async

load_dotenv()

# ==== Part 1: Initialize Persistent Session Service ==== #
db_url = "sqlite:///./my_memory_agent_data.db"  
session_service = DatabaseSessionService(db_url=db_url)

# ==== Part 2: Define Initial State ==== #
initial_state = {
    "user_id": str(uuid.uuid4()),
    "user_name": "Yonas Y",
    "reminders": [],
}

async def main():
    # Set up constants.
    APP_NAME = "Memory Agent App"
    USER_ID = initial_state["user_id"]
    USER_NAME = initial_state["user_name"]
    REMINDERS = initial_state["reminders"]

    # ===== Part 3: Session Management - Find or Create ===== #
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    # If there's an existing session, use it; otherwise, create a new one.
    if existing_sessions and len(existing_sessions) > 0:
        # Use the most recent session
        SESSION_ID = existing_sessions[0].id
        print(f"Continuing with existing session: {SESSION_ID}")
    else:
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

