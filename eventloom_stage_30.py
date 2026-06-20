# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: EventLoom
from datetime import datetime, date
import re

def parse_date(date_str: str) -> date | None:
    """Parse a date string from common formats and return a date object."""
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Invalid input: expected non-empty string.")
    
    patterns = [
        (r"^(\d{4})-(\d{2})-(\d{2})$", "%Y-%m-%d"),
        (r"^(\d{1,2})/(\d{1,2})/(\d{2,4})$", None),  # MM/DD/YYYY or DD/MM/YYYY logic handled below
        (r"^(\w+)\s+(\d{1,2}),?\s+(\d{4})$", "%B %d, %Y"),
    ]

    for pattern, fmt in patterns:
        match = re.match(pattern, date_str.strip())
        if match:
            try:
                if fmt is None:
                    # Ambiguous DD/MM vs MM/DD; assume YYYY exists to decide order
                    year = int(match.group(3))
                    month = int(match.group(2))
                    day = int(match.group(1))
                    if len(str(year)) == 4 and (month > 12 or day > 31):
                        # Likely DD/MM/YYYY if first two are small numbers, else MM/DD/YYYY
                        try: date(int(match.group(3)), int(match.group(2)), int(match.group(1)))
                        except ValueError: 
                            continue
                    elif len(str(year)) == 4 and (month > 12 or day > 31):
                         # Fallback for ambiguous cases without strict validation here, try standard swap if fail
                         pass
                    
                    # Try direct parse first
                    d = date(int(match.group(3)), int(match.group(2)), int(match.group(1)))
                    return d
                else:
                    return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError as e:
                continue
    
    raise ValueError(f"Unable to parse date string '{date_str}'. Supported formats: YYYY-MM-DD, MM/DD/YYYY, Month DD, YYYY.")

def normalize_date_input(user_input: str) -> str | None:
    """Attempt to clean and return a standardized 'YYYY-MM-DD' string or None if invalid."""
    try:
        parsed = parse_date(user_input)
        return parsed.isoformat()
    except ValueError:
        return None
