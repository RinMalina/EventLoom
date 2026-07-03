# === Stage 63: Add relationships between records where useful ===
# Project: EventLoom
from typing import Optional, List
import datetime as dt

class Event:
    def __init__(self, title: str, date: dt.date):
        self.title = title
        self.date = date
        self.attendees: List['Attendee'] = []
        self.budget_items: List['BudgetItem'] = []
        self.tasks: List['Task'] = []

class Attendee:
    def __init__(self, name: str):
        self.name = name
        self.events_attending: List[Event] = []

    def register_for(self, event: Event) -> None:
        if not any(e.title == event.title for e in self.events_attending):
            self.events_attending.append(event)
            event.attendees.append(self)

class BudgetItem:
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount
        self.event_budgets: List[Event] = []

    def allocate_to(self, event: Event) -> None:
        if not any(b.name == event.title for b in self.event_budgets):
            self.event_budgets.append(event)
            event.budget_items.append(self)

class Task:
    def __init__(self, description: str, assigned_to: Optional[Attendee]):
        self.description = description
        self.assigned_to = assigned_to
        if assigned_to:
            # Assuming a reverse relationship or flag could be added to Attendee for tasks
            pass 

class EventLoomDB:
    def __init__(self):
        self.events: dict[str, Event] = {}
        self.attendees: dict[str, Attendee] = {}
        self.budget_items: dict[str, BudgetItem] = {}

    def add_event(self, title: str, date: dt.date) -> Event:
        event = Event(title, date)
        self.events[title] = event
        return event

    def get_or_create_attendee(self, name: str) -> Attendee:
        if name not in self.attendees:
            self.attendees[name] = Attendee(name)
        return self.attendees[name]

    def add_budget_item(self, name: str, amount: float) -> BudgetItem:
        item = BudgetItem(name, amount)
        self.budget_items[name] = item
        return item

    def register_attendee_for_event(self, attendee_name: str, event_title: str) -> None:
        attendee = self.get_or_create_attendee(attendee_name)
        event = self.events[event_title]
        attendee.register_for(event)

    def allocate_budget_to_event(self, budget_name: str, event_title: str) -> None:
        item = self.budget_items[budget_name]
        event = self.events[event_title]
        item.allocate_to(event)
