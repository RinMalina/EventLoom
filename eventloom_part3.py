# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: EventLoom
def validate_event_field(value, field_name, min_len=1, max_len=50, allowed_chars=None):
    if value is None:
        return f"Error: '{field_name}' cannot be empty."
    if len(value) < min_len or len(value) > max_len:
        return f"Error: '{field_name}' length must be between {min_len} and {max_len} characters."
    if allowed_chars and not all(c in allowed_chars for c in value):
        return f"Error: '{field_name}' contains invalid characters. Allowed: {allowed_chars}"
    return None

def validate_event_id(event_id, prefix="evt"):
    if not event_id.startswith(prefix):
        return f"Error: Event ID must start with '{prefix}'. Got: {event_id}"
    try:
        int(event_id[len(prefix):])
    except ValueError:
        return f"Error: Event ID suffix must be numeric. Got: {event_id}"
    return None

def validate_attendee_name(name, min_len=2, max_len=30):
    if not name.strip():
        return "Error: Attendee name cannot contain only whitespace."
    if len(name) < min_len or len(name) > max_len:
        return f"Error: Attendee name length must be between {min_len} and {max_len} characters."
    return None

def validate_budget_item(item_name, amount):
    if not item_name or len(item_name.strip()) == 0:
        return "Error: Budget item name cannot be empty."
    try:
        float(amount)
    except (TypeError, ValueError):
        return "Error: Budget amount must be a valid number."
    if amount < 0:
        return "Error: Budget amount cannot be negative."
    return None

def validate_task_description(desc, min_len=5, max_len=200):
    if not desc or len(desc.strip()) == 0:
        return "Error: Task description cannot be empty."
    if len(desc) < min_len or len(desc) > max_len:
        return f"Error: Task description length must be between {min_len} and {max_len} characters."
    return None
