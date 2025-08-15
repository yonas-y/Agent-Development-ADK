from google.adk.agents import Agent

memory_agent = Agent(
    name = "memory_agent",
    model = "gemini-2.0-flash",
    description= "Memory agent",
    instruction= "You are a helpful assistant that remembers user information." \
    ""
)
