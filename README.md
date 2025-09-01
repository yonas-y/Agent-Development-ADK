# Agent Development ADK — Example Gallery

This repository contains a collection of practical examples for building agents using the [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/agent-development-kit).  
Each example demonstrates a different aspect of agent development, from basic interaction to multi-agent orchestration and persistent state.

---

## Examples Overview

### 1. **Basic Agent**
- **Location:** `1-basic-agent/`
- **Description:**  
  A simple agent that greets the user and demonstrates basic ADK agent setup.
- **Key Concepts:**  
  Agent definition, model selection, basic instructions.

---

### 2. **Tool Agent**
- **Location:** `2-tool-agent/`
- **Description:**  
  An agent that uses external tools (functions, APIs) to answer questions or perform tasks.
- **Key Concepts:**  
  Integrating `FunctionTool`, agent-tool wrappers, and third-party tools.

---

### 3. **LiteLLM Joke Agent**
- **Location:** `3-litellm-agent/`
- **Description:**  
  An agent using LiteLLM to tell jokes, demonstrating integration with alternative LLM providers.
- **Key Concepts:**  
  LiteLLM model usage, tool-based joke generation.

---

### 4. **Structured Output Agent**
- **Location:** `4-structured-outputs/`
- **Description:**  
  An agent that returns structured data (e.g., email content) using Pydantic schemas.
- **Key Concepts:**  
  Output schema enforcement, JSON output, Pydantic integration.

---

### 5. **Sessions and State**
- **Location:** `5-sessions-and-state/`
- **Description:**  
  Demonstrates session management and stateful interactions, allowing agents to remember user preferences.
- **Key Concepts:**  
  Session services, state persistence, user-specific context.

---

### 6. **Persistent Storage**
- **Location:** `6-persistent-storage/`
- **Description:**  
  A reminder agent with persistent storage using SQLite and ADK's database session service.
- **Key Concepts:**  
  Database-backed sessions, CRUD operations, persistent reminders.

---

### 7. **Multi-Agent Manager**
- **Location:** `7-multi-agent/`
- **Description:**  
  A manager agent that coordinates multiple sub-agents (e.g., news analyst, stock analyst, trend predictor).
- **Key Concepts:**  
  Multi-agent orchestration, agent delegation, tool composition.

---

## How to Use

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**  
   Add your API keys and settings to a `.env` file in each example directory as needed.

3. **Run an example:**  
   Navigate to the example directory and run the main script.  
   For example:
   ```bash
   cd 6-persistent-storage/reminder_agent
   python main.py
   ```

4. **Explore and extend:**  
   Each example is self-contained and can be modified to suit your needs.  
   Use them as templates for your own agent projects.

---

## Requirements

See [`requirements.txt`](requirements.txt) for a full list of dependencies:
- `google-adk[database]`
- `yfinance`
- `psutil`
- `litellm`
- `google-generativeai`
- `python-dotenv`

---

## Tips

- Run scripts as modules (`python -m package.module`) for correct imports.
- Use `.env` files for secrets and API keys.
- Check each example's README for specific instructions and details.

---

## License

These examples are provided for educational purposes under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).