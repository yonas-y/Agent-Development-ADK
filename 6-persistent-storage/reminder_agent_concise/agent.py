from tools import add_reminder_tool, view_reminders_tool, delete_reminders_tool
from google.generativeai import GenerativeModel

class Agent:
    def __init__(self, name, model, description, instruction, tools):
        self.name = name
        self.model_name = model
        self.description = description
        self.instruction = instruction
        self.tools = {tool.__name__: tool for tool in tools}
        self.model = GenerativeModel(model)  # Google ADK Gemini model

    def normalize_input(self, user_input: str):
        """Use Gemini to parse free-form text into structured fields."""
        prompt = f"""
        You are a reminder assistant. Convert the following input into JSON:
        - message: the reminder text
        - due_time: a normalized time string (e.g., '2025-08-19 14:00' or None if not clear).

        Input: "{user_input}"
        Respond with JSON only.
        """
        response = self.model.generate_content(prompt)
        try:
            return eval(response.text)  # assumes Gemini responds with JSON dict
        except Exception:
            return {"message": user_input, "due_time": None}

    def run_tool(self, tool_name, *args, **kwargs):
        if tool_name not in self.tools:
            return f"❌ Unknown tool: {tool_name}"
        try:
            return self.tools[tool_name](*args, **kwargs)
        except Exception as e:
            return f"⚠️ Error running {tool_name}: {e}"

# ---------- Agent wiring ----------
instruction_text = """
You are a Reminder Agent for one user per session.
You can create, list, and delete reminders.

IMPORTANT:
- Use these tools whenever appropriate: add_reminder, view_reminders, delete_reminder.
- On success, echo concise, human-friendly summaries; on errors, surface the 'message' returned by the tool.
"""

reminder_agent = Agent(
    name="reminder_agent",
    model="gemini-2.0-flash",
    description="Reminder agent",
    instruction=instruction_text,
    tools=[
        add_reminder_tool,
        view_reminders_tool,
        delete_reminders_tool,
    ],
)
