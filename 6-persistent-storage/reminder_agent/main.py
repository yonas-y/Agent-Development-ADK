import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.genai import types
from agent import reminder_agent
from database import init_db
from tools import add_reminder, view_reminders, update_reminder, delete_reminder
from config import APP_NAME
from session import get_or_create_session, session_service

# Load environment variables
load_dotenv()

# ==== Tool Mapping ====
TOOL_MAP = {
    "add_reminder_tool": add_reminder,
    "view_reminders_tool": view_reminders,
    "update_reminder_tool": update_reminder,
    "delete_reminder_tool": delete_reminder,
}

async def main():
    # Welcome message
    print("\n✨ Welcome to the Reminder Agent App!")
    print("Your reminders will be remembered across sessions.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    # ---- Initialize database ----
    init_db()
    print("Database initialized.")

    USER_ID = input("👤 Enter your user ID: ")
    if not USER_ID:
        print("❌ User ID cannot be empty. Exiting...")
        return

    session_id = await get_or_create_session(USER_ID)

    print(f"Using session ID: {session_id}")

    # Use a runner without sessions
    runner = Runner(
        agent=reminder_agent, 
        app_name=APP_NAME, 
        session_service=session_service)

    while True:
        try:
            user_input = input("📥 Input something to the reminder agent (or use 'exit' or 'quit' to leave): ")
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
                session_id=session_id,
                new_message=user_message,
            ):
                if event.is_final_response() and event.content and event.content.parts:  
                  for part in event.content.parts:
                    # Print agent text
                    if part.text:
                        print(part.text)
                    
                    # Execute any tool calls automatically
                    if part.function_call:
                        tool_name = part.function_call.name
                        args = part.function_call.args

                        if tool_name in TOOL_MAP:
                            output = TOOL_MAP[tool_name](USER_ID, **args)
                            print(output)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting...")
            break

        except Exception as e:
            print(f"⚠️ Error processing input: {e}")

        finally:
            # ---- Graceful cleanup ----
            try:
                await runner.close()  # ✅ Cleanup
            except Exception:
                pass

if __name__ == "__main__":
    asyncio.run(main())
