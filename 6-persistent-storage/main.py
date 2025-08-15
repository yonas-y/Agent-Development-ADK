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

