# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: EventLoom
def format_event_summary(event: Event) -> str:
    """Return a one-line summary of an event."""
    return (f"{event.name} ({event.location}, {len(event.attendees)} "
            f"attendees, budget ${event.budget})")


def find_events_by_date(events: List[Event], date: str) -> List[Event]:
    """Return all events that occur on the given date."""
    return [e for e in events if e.date == date]


def get_tasks_for_event(event_id: int, tasks: List[Task]) -> List[Task]:
    """Return only the tasks belonging to the given event."""
    return [t for t in tasks if t.event_id == event_id]


def compute_total_budget(events: List[Event]) -> float:
    """Sum the budgets of all provided events."""
    return sum(e.budget for e in events)


def sort_events_by_date(events: List[Event]) -> List[Event]:
    """Return a sorted copy of the event list by date string."""
    return sorted(events, key=lambda e: e.date)
