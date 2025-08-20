from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import tools

# Expose tools to Google ADK
@FunctionTool
def add_reminder_tool(user_id: str, text: str) -> str:
    return tools.add_reminder(user_id, text)

@FunctionTool
def view_reminders_tool(user_id: str) -> str:
    return tools.view_reminders(user_id)

@FunctionTool
def update_reminder_tool(user_id: str, index: int, new_text: str) -> str:
    return tools.update_reminder(user_id, index, new_text)

@FunctionTool
def delete_reminder_tool(user_id: str, index: int) -> str:
    return tools.delete_reminder(user_id, index)

# Simple reminder agent
reminder_agent = Agent(
    name="reminder_agent_without_sessions_db",
    model="gemini-2.0-flash",
    description="In-memory reminder agent with out sessions.",
    instruction="""
    You are a friendly reminder assistant.
    You can add, view, update, and delete reminders for the user.
    Always address the user politely.
    """,
    tools=[
        add_reminder_tool,
        view_reminders_tool,
        update_reminder_tool,
        delete_reminder_tool,
    ],
)
