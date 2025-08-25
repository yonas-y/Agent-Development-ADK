"""
Project Configuration File

Contains:
- Database configuration.
- Agent related common configurations.
"""

# ==== CONFIGURATION ==== #
DB_URL  = "sqlite:///learner_support_database.db"  

# Extract file path for init_db
DB_PATH = DB_URL.replace("sqlite:///", "") if DB_URL.startswith("sqlite:///") else DB_URL

APP_NAME = "Customer Learner Support Agent"