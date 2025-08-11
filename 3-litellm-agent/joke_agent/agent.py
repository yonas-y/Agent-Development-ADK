import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
)

def get_jokes():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "Why can't you give Elsa a balloon? Because she will let it go!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    return random.choice(jokes)

root_agent = Agent(
    name="joke_agent",
    model=model,
    description="A fun agent that tells jokes.",
    instruction="You are a joke-telling agent. Use only the get_jokes tool to tell a joke.",
    tools=[get_jokes],
)