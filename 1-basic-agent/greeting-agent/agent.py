from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="A simple agent that greets the user.",
    instruction="You are a greeting agent. Ask the use for name" \
    "and greet them by name."
)
