import dateparser
from datetime import datetime, timedelta

def parse_due_date(text: str) -> str:
    """
    Convert natural language date into YYYY-MM-DD HH:MM format.
    Handles:
      - "tomorrow", "next Friday", "tomorrow afternoon", etc.
      - Defaults to sensible times if no time is specified:
        - morning -> 09:00
        - afternoon -> 14:00
        - evening -> 18:00
        - night -> 20:00
      - Uses the system's current date and time as the reference.
      - Leaves it to the agent to ask for confirmation if needed.
    """
    now = datetime.now()  # System current datetime

    # Settings for dateparser
    settings = {
        'PREFER_DATES_FROM': 'future',
        'RELATIVE_BASE': now,
        'RETURN_AS_TIMEZONE_AWARE': False
    }

    dt = dateparser.parse(text, settings=settings)
    if not dt:
        # fallback if parsing fails
        return text

    # If the user did not specify a time, assign a sensible default
    if dt.hour == 0 and dt.minute == 0:
        text_lower = text.lower()
        if "morning" in text_lower:
            dt = dt.replace(hour=9, minute=0)
        elif "afternoon" in text_lower:
            dt = dt.replace(hour=14, minute=0)
        elif "evening" in text_lower:
            dt = dt.replace(hour=18, minute=0)
        elif "night" in text_lower:
            dt = dt.replace(hour=20, minute=0)
        else:
            # Ambiguous time: default to 14:00
            dt = dt.replace(hour=14, minute=0)
            # Agent should ask the user to confirm or adjust the time
        # Ensure relative dates like "tomorrow" are always in the future
    if dt.date() <= now.date():
        dt += timedelta(days=1)

    return dt.strftime("%Y-%m-%d %H:%M")
