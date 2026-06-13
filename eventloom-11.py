# === Stage 11: Add JSON export for the current application state ===
# Project: EventLoom
def export_state():
    import json
    from pathlib import Path
    base = Path(__file__).parent / "data"
    state = {
        "schedules": [f.read_text(encoding="utf-8") for f in sorted(base.glob("schedule_*.json"))],
        "attendees": [f.read_text(encoding="utf-8") for f in sorted(base.glob("attendee_*.json"))],
        "budgets": [f.read_text(encoding="utf-8") for f in sorted(base.glob("budget_*.json"))],
        "tasks": [f.read_text(encoding="utf-8") for f in sorted(base.glob("task_*.json"))]
    }
    with open(base / "state.json", "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)
