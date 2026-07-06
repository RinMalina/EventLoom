# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: EventLoom
def seed_demo_data():
    """Populate EventLoom with deterministic sample data for quick testing."""
    from datetime import date, timedelta
    # Schedules
    schedules = {
        "2025-10-15": ["9:00", "10:30", "14:00"],
        "2025-10-16": ["9:00", "13:00"],
    }
    # Attendees
    attendees = [
        {"name": "Alice Chen", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        {"name": "Carol White", "email": "carol@example.com"},
    ]
    # Budgets (in USD)
    budgets = {
        "venue": 2000,
        "catering": 500,
        "marketing": 300,
        "miscellaneous": 100,
    }
    # Tasks with deadlines and owners
    tasks = [
        {"title": "Book venue", "owner": "Alice Chen", "deadline": date(2025, 9, 20), "status": "done"},
        {"title": "Plan catering", "owner": "Bob Smith", "deadline": date(2025, 10, 1), "status": "in_progress"},
        {"title": "Create flyers", "owner": "Carol White", "deadline": date(2025, 9, 30), "status": "todo"},
    ]
    # Return all seed data as a dict for easy access
    return {
        "schedules": schedules,
        "attendees": attendees,
        "budgets": budgets,
        "tasks": tasks,
    }
