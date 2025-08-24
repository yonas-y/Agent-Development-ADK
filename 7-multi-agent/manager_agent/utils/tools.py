from datetime import datetime, timezone

def get_current_time() -> dict:
    """
    Provides the current UTC date and time (timezone-aware).
    Returns:
        dict: Contains current UTC ISO 8601 datetime (with 'Z'), date, and time.
    """
    now = datetime.now(timezone.utc).replace(microsecond=0)
    return {
        "timezone": "UTC",
        "datetime": now.isoformat().replace("+00:00", "Z"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
    }