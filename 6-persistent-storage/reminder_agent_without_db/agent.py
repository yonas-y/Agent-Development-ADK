from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import tools

# Expose tools to Google ADK
@FunctionTool
def add_reminder_tool(user_id: str, description: str, due_date: str, remark: str ) -> str:
    """Add a structured reminder for a user."""
    remark = remark or None  # Allow empty remark
    return tools.add_reminder(user_id, description, due_date, remark)

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
    name="reminder_agent_in_memory",
    model="gemini-2.0-flash",
    description="Interactive in-memory reminder agent that parses natural language dates.",
    instruction="""
    You are a friendly reminder assistant.
    You can add, view, update, and delete reminders for the user.
    When adding reminders, extract description, due date, and optional remark.
    Convert relative dates like 'tomorrow', 'next Friday', or 'in 2 hours' into a proper date format.

    You MUST always extract reminders into structured fields:
      - description (string, required)
      - due_date (string, can be natural language like 'tomorrow', convert to YYYY-MM-DD HH:MM)
      - remark (string, optional; if missing, ask the user if they want to add a remark)

    If the user does not provide a remark, politely ask them if they want to add one.

    For the due_date:
      - Use the current date and time as a reference when parsing relative dates.
      - If the user specifies a time (e.g., 'tomorrow at 9am', 'next Friday at 18:00'), use that time.
      - If the time is ambiguous (e.g., just 'tomorrow'), you may default to 14:00 (afternoon), but always ask the user:
        "I have set the reminder for [parsed date and time]. Would you like to adjust the time?"
      - If the user replies with a different time, update the reminder accordingly.

    When showing reminders, display them in a structured format:
      Description: ...
      Due Date: ...
      Remark: ...
    
    If a user asks to 'show reminders', format each reminder this way instead of plain text.

    Always respond politely and confirm actions.
    """,
    tools=[
        add_reminder_tool,
        view_reminders_tool,
        update_reminder_tool,
        delete_reminder_tool,
    ]
)
