import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import reminder_agent
from tools import add_reminder, view_reminders, update_reminder, delete_reminder

load_dotenv()

# Create a new session service to store state.
session_service_stateful = InMemorySessionService()

APP_NAME = "Reminder App."

async def main():
    print("[Reminder Agent] Ready! (In-memory only)")
    print("Type 'exit' to quit.\n")

    USER_ID = input("👤 Enter your user ID: ")

    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=USER_ID,
    )

    print(f"--- Examining Session Properties ---")
    print(f"\tSession ID: {stateful_session.id}")
    print(f"\tApplication Name: {stateful_session.app_name}")
    print(f"\tUser ID: {stateful_session.user_id}")
    print(f"---------------------------------")

    # Use a runner without sessions
    runner = Runner(
        agent=reminder_agent, 
        app_name=APP_NAME, 
        session_service=session_service_stateful)

    while True:
        try:
            user_input = input("📥 Input something for the reminder app: ")
            if user_input.lower() == "exit" or user_input.lower() == "quit":
                print("👋 Goodbye!")
                break

            user_message = types.Content(
                role="user",
                parts=[types.Part(text=user_input)],
                )
                    
            print("Agent response:")
            for event in runner.run(
                user_id=USER_ID,
                session_id=USER_ID,
                new_message=user_message,
            ):
                if event.is_final_response() and event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            print(part.text)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting...")
            break

        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
