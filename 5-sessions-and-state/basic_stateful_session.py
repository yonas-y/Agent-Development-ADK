import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import agent

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
