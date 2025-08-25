# Manager Agent (Multi-Agent Demo)

A Manager Agent that orchestrates specialized sub-agents to analyze the stock market.  
The manager delegates tasks to sub-agents, aggregates results, and returns a concise, actionable summary.

## Features
- Delegates work to sub-agents: stock_analyst, trend_predictor, news_analyst.
- Includes tools: current time provider and agent-tool wrapper for the news analyst.
- Combines quantitative analysis with qualitative news sentiment.
- Designed for extensibility — add more sub-agents or tools as needed.

## Minimal Requirements
- Python 3.8+
- google-adk
- python-dotenv (optional for env vars)

Install:
```bash
pip install google-adk python-dotenv
```

## Repo layout
```
manager_agent/
├─ agent.py               # Manager agent definition (root_agent)
├─ utils/
│  └─ tools.py            # get_current_time tool
└─ sub_agents/
   ├─ news_analyst/       # news_analyst.agent
   ├─ stock_analyst/      # stock_analyst.agent
   └─ trend_predictor/    # trend_predictor.agent
```

## agent.py overview
- root_agent: Llm Agent configured with sub_agents and tools.
- Tools used:
  - AgentTool(news_analyst_agent)
  - FunctionTool(get_current_time)

## Usage
1. Ensure sub-agents are available and importable from the package.
2. Run your application that creates a Runner using `root_agent`, or import `root_agent` into a runner script.


## Notes
- Sub-agents must be valid Agent objects and import paths correct (package-relative imports).
- Keep secrets out of source control (use `.env` and `.gitignore`).
- The Manager Agent instruction text is the primary orchestration policy — tune it for your workflow.

## Extending
- Add more specialized sub-agents (e.g., risk_assessor, portfolio_optimizer).
- Add tools for fetching live market data, caching, or persistence.

## License
Educational /