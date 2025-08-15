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