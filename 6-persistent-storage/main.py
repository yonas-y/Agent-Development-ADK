import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner

from reminder_agent.agent import reminder_agent
from reminder_agent.database import init_db

# Load environment variables
load_dotenv()

# ==== CONFIGURATION ==== #
APP_NAME = "Reminder Agent App"
DB_URL  = "sqlite:///reminder_agent_data.db"  

# Extract file path for init_db
if DB_URL.startswith("sqlite:///"):
    db_path = DB_URL.replace("sqlite:///", "")
else:
    db_path = DB_URL

# Initialize DB with file path
init_db(db_path)

# Initialize session persistence with full URL
session_service = DatabaseSessionService(db_url=DB_URL)

# Default initial state for a new user
initial_state = {
    "user_id": str(uuid.uuid4()),
    "user_name": "Yonas Y",
    "reminders": [],
}

# ==== Session Management ==== #
async def get_or_create_session(user_id: str):
    """Retrieve an existing session or create a new one."""
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

# ==== Main Loop ==== #
async def main():

    user_id = initial_state["user_id"]

    # Session management
    session_id = await get_or_create_session(user_id)

    # Runner with reminder agent
    runner = Runner(
        agent=reminder_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # Welcome message
    print("\n✨ Welcome to the Reminder Agent App!")
    print("Your reminders will be remembered across sessions.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    # Conversation loop
    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("👋 Goodbye! Your data has been saved.")
                break

            # Process input with agent
            response = await runner.run(
                user_id=user_id,
                session_id=session_id,
                user_input=user_input
            )
            print(f"Reminder Agent: {response}")

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting...")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
