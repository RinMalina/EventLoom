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

# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: EventLoom
SETTINGS = {
    "currency": "USD",
    "timezone": "UTC",
    "max_attendees_per_event": 100,
    "budget_warning_threshold_percent": 80,
    "task_priority_levels": ["critical", "high", "medium", "low"],
}

def update_setting(key: str, value):
    """Update a single setting and return the new configuration."""
    if key not in SETTINGS:
        raise KeyError(f"Unknown setting key: {key}")
    SETTINGS[key] = value
    print(f"[Settings] Updated '{key}' to {value}")

def get_setting(key: str, default=None):
    """Retrieve a setting or return the provided default."""
    return SETTINGS.get(key, default)

def reset_settings():
    """Reset all settings to their default values defined in this block."""
    global SETTINGS
    SETTINGS = {
        "currency": "USD",
        "timezone": "UTC",
        "max_attendees_per_event": 100,
        "budget_warning_threshold_percent": 80,
        "task_priority_levels": ["critical", "high", "medium", "low"],
    }
    print("[Settings] All settings reset to defaults.")

def validate_settings():
    """Perform basic validation on current settings."""
    if not isinstance(SETTINGS["max_attendees_per_event"], int) or SETTINGS["max_attendees_per_event"] <= 0:
        raise ValueError("Invalid max_attendees_per_event")
    if not (0 < SETTINGS["budget_warning_threshold_percent"] <= 100):
        raise ValueError("Invalid budget_warning_threshold_percent")
    print("[Settings] Validation passed.")

def load_settings_from_file(filepath: str) -> dict:
    """Load settings from a JSON file and merge with defaults."""
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            user_overrides = json.load(f)
        for k, v in user_overrides.items():
            if k in SETTINGS:
                SETTINGS[k] = v
        return SETTINGS
    except FileNotFoundError:
        print(f"[Settings] File {filepath} not found. Using defaults.")
        return SETTINGS
