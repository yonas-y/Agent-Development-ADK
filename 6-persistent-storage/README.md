# Reminder Agent — Persistent Storage Example

A small project that demonstrates a reminder agent with persistent session and reminder storage using Google ADK. The project stores reminders in SQLite and uses ADK session persistence to keep user state across runs.

## Features
- Stateful agent using Google ADK Runner and session services
- Persistent SQLite storage for reminders
- Simple FunctionTool-based API for add/view/update/delete reminders
- Example main script that initializes DB and session storage

## Repo layout
```
6-persistent-storage/
├─ README.md
├─ reminder_agent/
│  ├─ agent.py
│  ├─ database.py
│  ├─ main.py
│  ├─ tools.py
│  ├─ session.py
│  ├─ config.py
│  └─ utils.py
├─ reminder_agent_data.db
└─ reminders.db
```

## Requirements
- Python 3.8+
- google-adk
- python-dotenv
- (sqlite3 is part of the stdlib)

Install:
```bash
python -m pip install google-adk python-dotenv
```

## Configuration
Set environment variables in `reminder_agent/.env` or your system env. Example keys:
```
GOOGLE_API_KEY=your-key
OPEN_ROUTER_KEY=...
```

Define DB URL in code or env:
```python
DB_URL = "sqlite:///reminder_agent_data.db"
```

Note: `DatabaseSessionService` accepts a SQLAlchemy-style URL (e.g. `sqlite:///file.db`). The simple sqlite3 initializer function in `database.py` needs a filesystem path — strip the `sqlite:///` prefix when calling `init_db()`.

Example to support both:
```python
# extract file path for init_db, keep full URL for session service
if DB_URL.startswith("sqlite:///"):
    db_path = DB_URL.replace("sqlite:///", "")
else:
    db_path = DB_URL

init_db(db_path)                      # uses sqlite3.connect(db_path)
session_service = DatabaseSessionService(db_url=DB_URL)  # uses full URL
```

## Initialize database
Call `init_db()` before running the agent to ensure tables exist. The `main.py` example included does this automatically when started.

## Running
From the `6-persistent-storage` folder run as a module (recommended so package imports work):
```bash
python -m reminder_agent.main
```
Or:
```bash
python reminder_agent/main.py
```

## Common Troubleshooting
- Import errors: run as module (`python -m reminder_agent.main`) or use package-style imports (`from reminder_agent.database import init_db`).
- Async errors: await async session calls (e.g., `await session_service.create_session(...)`) or run inside `asyncio.run(main())`.
- DB path vs URL: strip `sqlite:///` for sqlite3, keep full URL for session service.
- If `DatabaseSessionService` can't connect, check that SQLAlchemy-compatible URL is correct and dependencies installed.

## Notes
- SQLite DB files are included for examples but you may remove them if you want to start fresh.
- Keep secrets out of the repository; add `.env` to `.gitignore`.

## License
Example / educational