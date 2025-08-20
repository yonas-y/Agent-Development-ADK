# ==== CONFIGURATION ==== #
DB_URL  = "sqlite:///reminder_agent_data.db"  

# Extract file path for init_db
db_path = DB_URL.replace("sqlite:///", "") if DB_URL.startswith("sqlite:///") else DB_URL

APP_NAME = "Reminder Agent App"