# Stateful Question Answering Agent

This project demonstrates how to build a **stateful question answering agent** using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit).  
It showcases session and state management, allowing the agent to answer questions based on user-specific preferences stored in session state.

## Features

- Uses the `gemini-2.0-flash` model.
- Maintains user state and preferences across sessions.
- Answers questions using personalized information.
- Demonstrates session creation, retrieval, and event handling.

## Directory Structure

```
5-sessions-and-state/
├── basic_stateful_session.py
└── question_answering_agent/
    └── agent.py
```

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-adk python-dotenv
   ```

2. **Set up your `.env` file** (if required by your ADK setup):
   ```
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY=your-api-key-here
   ```

3. **Run the main script:**
   ```bash
   python basic_stateful_session.py
   ```

## How It Works

- `question_answering_agent/agent.py` defines the agent logic.
- `basic_stateful_session.py`:
  - Loads environment variables.
  - Creates a session with initial user state.
  - Runs the agent using the `Runner`.
  - Sends a sample question to the agent.
  - Prints the agent's response and session state.


## Requirements

- Python 3.8+
- [google-adk](https://pypi.org/project/google-adk/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## License

This project is for educational purpose.