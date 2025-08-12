# Joke Agent

This project implements a **Joke Agent** using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit) and LiteLLM.  
The agent is designed to tell random jokes using a simple tool function.

## Features

- Uses the `openrouter/openai/gpt-4.1` model via LiteLLM.
- Tells a random joke from a set of six pre-defined jokes.
- Simple and fun interaction.

## File Structure

```
3-litellm-agent/
└── joke_agent/
    └── agent.py
```

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-adk litellm
   ```

2. **Set up your `.env` file:**
   ```
   OPEN_ROUTER_KEY=your-openrouter-api-key
   ```

3. **Run the agent:**
   ```bash
   adk run agent.py
   ```
   or, if using as a module:
   ```bash
   python -m joke_agent.agent
   ```

## Requirements

- Python 3.8+
- [google-adk](https://pypi.org/project/google-adk/)
- [litellm](https://pypi.org/project/litellm/)

## License

This project is for educational purpose.