import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session 
from google.genai import types
from question_answering_agent.agent import question_answering_agent


load_dotenv()

# Create a new session service to store state.
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Yonas Y T",
    "user_preferences": 
        "I like to play football, watching movies, and reading books."\
        "My favorite food is Italian."\
        "My favorite TV show is Game of Thrones.",
}

# Create a NEW session.
APP_NAME = "YON Bot"
USER_ID = "yoni_99"
SESSION_ID = str(uuid.uuid4())

async def main():
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )

    print(f"--- Examining Session Properties ---")
    print(f"\tID {'id'}: {stateful_session.id}")
    print(f"\tApplication Name (`app_name`): {stateful_session.app_name}")
    print(f"\tUser ID (`user_id`): {stateful_session.user_id}")
    # print(f"\tState (`state`): {stateful_session.state}") # Note: Only shows initial state here
    print(f"\tEvents (`events`): {stateful_session.events}") # Initially empty
    print(f"\tLast Update (`last_update_time`): {stateful_session.last_update_time:.2f}")
    print(f"---------------------------------")

asyncio.run(main())

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)
