"""
main.py

Entry point for the Customer/Learner Support Agent application.

- Handles user onboarding (new or returning users)
- Creates or resumes ADK sessions with persistent state
- Runs the root agent in a loop, remembering previous interactions
"""

import asyncio
import uuid
from dotenv import load_dotenv
import google.genai.types as types
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService

from config import APP_NAME, DB_URL
from models.user import get_user, create_user
from agent import root_agent


load_dotenv()

# ----- Part 1: Initialize Database Session Service ---- #
adk_session = DatabaseSessionService(DB_URL)

# ------ Part 2: Define initial session state ---- #
initial_state_template = {
    "user_name": None,
    "user_id": None,
    "purchased_courses": [],
    "interaction_history": []
}

async def main():
    # ---- Part 3: User onboarding ---- #
    entered_user_id = input("👤 Enter your User ID (or leave blank if new): ").strip()

    if entered_user_id:
        # Check if user exists in DB
        user = get_user(entered_user_id)
        if user:
            user_id = user.id
            user_name = user.username
            print(f"✅ Welcome back, {user_name} (ID: {user_id})!")
        else:
            # User ID not found → treat as new
            print("⚠️ User ID not found. Let's create a new account.")
            user_name = input("Enter your name: ").strip() or "Guest"
            user_id = entered_user_id  # reuse entered ID
            create_user(user_id, user_name)
            print(f"🆕 New user created: {user_name} (ID: {user_id})")
    else:
        # Completely new user → ask for name + generate ID
        user_name = input("Enter your name: ").strip() or "Guest"
        user_id = str(uuid.uuid4())
        create_user(user_id, user_name)
        print(f"🆕 New user created: {user_name} (ID: {user_id})")

    # ---- Part 4: Create or resume ADK session ---- #
    session_service = await adk_session.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        state={**initial_state_template, "user_id": user_id, "user_name": user_name}
    )

    print(f"🎯 Active Session ID: {session_service.id}")

    # ---- Part 5: Agent Runner Setup ---- #
    runner = Runner(
        agent=root_agent, 
        app_name=APP_NAME, 
        session_service=adk_session)
    
    # Welcome message
    print("\n✨ Welcome to the Customer Support Agent App!")
    print("Your interactions will be remembered across sessions.")
    print("Type 'exit' or 'quit' to end the conversation.\n")
   
    while True:
        try:
            user_input = input("📥 Enter your message: ")
            if user_input.lower() == "exit" or user_input.lower() == "quit":
                print("👋 Goodbye!")
                break

            user_message = types.Content(
                role="user",
                parts=[types.Part(text=user_input)],
                )
                    
            print("🤖 Agent response:")
            for event in runner.run(
                user_id=user_id,
                session_id=session_service.id,
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
            print(f"⚠️ Error processing input: {e}")

        finally:
            # ---- Graceful cleanup ----
            try:
                await runner.close()
            except Exception:
                pass

if __name__ == "__main__":
    asyncio.run(main())
