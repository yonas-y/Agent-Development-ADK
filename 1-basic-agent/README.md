# Greeting Agent

This project contains a simple agent built using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit).  
The agent is designed to greet users by asking for their name and responding with a personalized greeting.

## Features

- Uses the `gemini-2.0-flash` model.
- Asks the user for their name.
- Greets the user by name.
- Configurable via `.env` for API keys and settings.

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-adk
   ```

2. **Set up your `.env` file:**
   ```
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY=your-api-key-here
   ```

3. **Run the agent:**
   ```bash
   adk run agent.py
   ```

## Requirements

- Python 3.8+
- [google-adk](https://pypi.org/project/google-adk/)

## License

This project is for
