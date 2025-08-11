from google.adk.agents import Agent
from google.adk.tools import google_search

# Create an agent with google search tool as a search specialist
google_search_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description='A search agent that uses google search to get latest information ' \
    'about current events, weather, or business hours.',
    instruction='Use google search to answer user questions about real-time,' \
    ' logistical information.',
    tools=[google_search]
)
