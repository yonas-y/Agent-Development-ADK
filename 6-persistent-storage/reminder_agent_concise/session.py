# Session service + context memory
import json
from database import get_connection
from config import APP_NAME, db_path

initial_state = json.dumps({"history": []})  # simple JSON for context memory

class SessionService:
    async def list_sessions(self, app_name: str, user_id: str):
        with get_connection(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, state FROM sessions WHERE app_name = ? AND user_id = ?", (app_name, user_id))
            rows = cursor.fetchall()
        return {"sessions": [{"id": row[0], "state": row[1]} for row in rows]}

    async def create_session(self, app_name: str, user_id: str, state: str):
        with get_connection(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sessions (app_name, user_id, state) VALUES (?, ?, ?)", (app_name, user_id, state))
            conn.commit()
            session_id = cursor.lastrowid
        return {"id": session_id, "state": state}

    async def update_session_state(self, session_id: int, new_state: dict):
        """Store updated state (context memory) as JSON."""
        with get_connection(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE sessions SET state = ? WHERE id = ?", (json.dumps(new_state), session_id))
            conn.commit()

    async def get_session_state(self, session_id: int):
        """Retrieve state JSON as dict."""
        with get_connection(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT state FROM sessions WHERE id = ?", (session_id,))
            row = cursor.fetchone()
        if row:
            try:
                return json.loads(row[0])
            except Exception:
                return {}
        return {}

session_service = SessionService()

# ==== Session Management ====
async def get_or_create_session(user_id: str):
    existing_sessions = await session_service.list_sessions(APP_NAME, user_id)

    if existing_sessions["sessions"]:
        session_id = existing_sessions["sessions"][0]["id"]
        print(f"Continuing with existing session: {session_id}")
        return session_id

    new_session = await session_service.create_session(APP_NAME, user_id, initial_state)
    print(f"Created new session: {new_session['id']}")
    return new_session["id"]
