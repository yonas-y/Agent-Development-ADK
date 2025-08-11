# Tool Agent

This project implements a **Tool Agent** using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit).  
The agent is designed to assist users by leveraging multiple tools, including time retrieval, currency exchange rates, Google search, and Wikipedia lookup.

## Features

- Uses the `gemini-2.0-flash` model.
- Retrieves the current time.
- Fetches foreign exchange rates.
- Performs Google searches via a custom agent.
- Looks up information on Wikipedia using LangChain.

## File Structure

```
2-tool-agent/
└── tool_agent/
    ├── agent.py
    ├── custom_agents.py
    ├── custom_functions.py
    └── third_party_tools.py
```

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-adk langchain
   ```

2. **Set up your `.env` file:**
   ```
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY=your-api-key-here
   ```

3. **Run the agent as a module:**
   ```bash
   python -m tool_agent.agent
   ```
   > **Note:** Relative imports require running as a module from the parent directory.

## Requirements

- Python 3.8+
- [google-adk](https://pypi.org/project/google-adk/)
- [langchain](https://pypi.org/project/langchain/)

## License

This project is for educational purposes.