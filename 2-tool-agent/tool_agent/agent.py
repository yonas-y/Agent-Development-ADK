from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools import agent_tool

from .custom_agents import google_search_agent
from .custom_functions import get_fx_rate
from typing import Dict
from datetime import datetime

def get_current_time() -> Dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    instruction="You are a helpful agent that uses the following tools:" \
    "- get_current_time" \
    "- get_fx_rate" \
    "- google_search_agent",
    tools=[
        FunctionTool(get_fx_rate),
        FunctionTool(get_current_time),
        agent_tool.AgentTool(google_search_agent, "google_search_agent")
    ]
)
