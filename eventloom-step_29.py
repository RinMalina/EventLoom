# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: EventLoom
from datetime import datetime, timedelta
def get_upcoming_tasks(tasks: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [t for t in tasks if t.get("due_date") and now <= t["due_date"] < cutoff]

def get_upcoming_events(events: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [e for e in events if e.get("start_date") and now <= e["start_date"] < cutoff]

def get_upcoming_budget_alerts(budgets: list[dict], threshold_pct: float = 0.8) -> list[dict]:
    alerts = []
    for b in budgets:
        spent = sum(item.get("amount", 0) for item in b.get("expenses", []))
        limit = b.get("limit")
        if limit and spent / limit >= threshold_pct:
            alerts.append({"category": b["name"], "spent": spent, "limit": limit})
    return alerts

def get_upcoming_attendee_deadlines(attendees: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [a for a in attendees if a.get("deadline") and now <= a["deadline"] < cutoff]
