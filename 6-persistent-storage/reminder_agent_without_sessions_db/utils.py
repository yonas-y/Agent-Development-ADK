import dateparser

def parse_due_date(text: str) -> str:
    """
    Convert a natural language date like 'tomorrow' into YYYY-MM-DD format.
    """
    dt = dateparser.parse(text)
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M")  # optional time included
    else:
        return text  # fallback, store as-is
