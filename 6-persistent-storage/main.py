import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from reminder_agent.agent import reminder_agent

load_dotenv()

# ==== Part 1: Initialize Persistent Session Service ==== #
db_url = "sqlite:///reminder_agent_data.db"  
session_service = DatabaseSessionService(db_url=db_url)

# ==== Part 2: Define Initial State ==== #
initial_state = {
    "user_id": str(uuid.uuid4()),
    "user_name": "Yonas Y",
    "reminders": [],
}

async def main():
    # Set up constants.
    APP_NAME = "Reminder Agent App"
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
        new_session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    # ===== Part 4: Agent runner setup ===== #
    # Create a runner with the reminder agent.
    runner = Runner(
        agent=reminder_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # ===== Part 5: Interactive Conversation Loop  ===== #
    print("\n Welcome to the Memory Agent App!")
    print("Your reminders will be remembered across sessions.")
    print("Type 'exit' to 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Your data has been saved.")
            break

        # Process the user query through the agent.
        response = await runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            user_input=user_input
        )
        print(f"Reminder Agent: {response}")

if __name__ == "__main__":
    asyncio.run(main())
    


from google.adk.agents import Agent
from database import init_db
# from tools import (
#     add_reminder_tool,
#     view_reminders_tool,
#     update_reminder_tool,
#     delete_reminder_tool,
#     update_user_name_tool
# )

# Initialize DB on startup
init_db()

# ---------- Agent wiring ----------
instruction_text = """
You are a Reminder Agent for one user per session.
You can create, list, update, and delete reminders, and update the user's display name.

IMPORTANT:
- Use these tools whenever appropriate: add_reminder, view_reminder, update_reminder, delete_reminder, update_user_name.
- Always pass due dates as ISO 8601 strings with timezone if possible (e.g., 2025-08-20T14:00:00+03:00).
- If only a date or time is given, assume Africa/Addis_Ababa timezone.
- On success, echo concise, human-friendly summaries; on errors, surface the 'message' returned by the tool.
"""

reminder_agent = Agent(
    name = "reminder_agent",
    model = "gemini-2.0-flash",
    description= "Reminder agent",
    instruction= instruction_text,
    # tools=[
    #     add_reminder_tool, 
    #     view_reminders_tool,
    #     update_reminder_tool, 
    #     delete_reminder_tool,
    #     update_user_name_tool
    #     ],
)
    