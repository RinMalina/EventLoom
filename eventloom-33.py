# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: EventLoom
SETTINGS = {
    "currency": "USD",
    "timezone": "UTC",
    "max_guests": 100,
    "budget_limit": 5000.0,
}


def update_setting(key: str, value) -> bool:
    if key in SETTINGS and isinstance(SETTINGS[key], type(value)):
        SETTINGS[key] = value
        return True
    raise ValueError(f"Invalid setting '{key}' or type mismatch")


def get_settings() -> dict:
    return SETTINGS.copy()


def validate_budget(budget: float) -> bool:
    if budget < 0:
        return False
    try:
        update_setting("budget_limit", budget)
        return True
    except ValueError:
        return False


def set_max_guests(count: int) -> bool:
    if count <= 0 or count > 10000:
        return False
    try:
        update_setting("max_guests", count)
        return True
    except ValueError:
        return False
