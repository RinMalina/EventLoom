# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: EventLoom
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class EventLoom:
    def __init__(self):
        self.events: List[Dict] = []
        self.attendees: Dict[str, Dict] = {}
        self.budgets: Dict[str, float] = {"total": 0.0, "spent": 0.0}
        self.tasks: List[Dict] = []

    def add_event(self, name: str, date: datetime, location: str):
        event = {
            "id": len(self.events) + 1,
            "name": name,
            "date": date,
            "location": location
        }
        self.events.append(event)

    def register_attendee(self, name: str, email: str):
        if name not in self.attendees:
            self.attendees[name] = {"email": email, "checked_in": False}

    def add_task(self, description: str, event_id: int, priority: int = 1):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "event_id": event_id,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)

    def spend_budget(self, amount: float, category: str):
        if amount > 0:
            self.budgets["spent"] += amount
            print(f"Budget spent: {amount} in category: {category}")

# Demo initialization
loom = EventLoom()
loom.add_event("TechConf 2024", datetime(2024, 11, 15, 9, 0), "Moscow Convention Center")
loom.register_attendee("Ivan Petrov", "ivan@example.com")
loom.register_attendee("Anna Smirnova", "anna@example.com")
loom.add_task("Rent venue", 1, priority=1)
loom.add_task("Buy catering", 1, priority=2)
loom.spend_budget(5000.0, "Venue")
