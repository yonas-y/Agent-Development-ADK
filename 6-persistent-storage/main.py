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

if __name__ == "__main__":
    asyncio.run(main())
