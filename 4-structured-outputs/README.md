# Email Agent

This project implements an **Email Generation Agent** using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit).  
The agent generates professional email content based on user requests and returns the result in a structured format.

## Features

- Uses the `gemini-2.0-flash` model.
- Generates concise, professional, or friendly emails as needed.
- Returns output as a structured JSON object with `subject` and `body` fields.
- Enforces output schema using [Pydantic](https://docs.pydantic.dev/).

## File Structure

```
4-structured-outputs/
└── email_agent/
    └── agent.py
```

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-adk pydantic
   ```

2. **Set up your `.env` file** (if required by your ADK setup):
   ```
   GOOGLE_GENAI_USE_VERTEXAI=False
   GOOGLE_API_KEY=your-api-key-here
   ```

3. **Run the agent:**
   ```bash
   adk run agent.py
   ```
   or, if using as a module:
   ```bash
   python -m email_agent.agent
   ```

## Requirements

- Python 3.8+
- [google-adk](https://pypi.org/project/google-adk/)
- [pydantic](https://pypi.org/project/pydantic/)

## License

This project is for educational purpose.
