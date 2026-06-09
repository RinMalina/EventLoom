# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: EventLoom
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Attendee:
    name: str
    email: str
    role: str = "guest"
    dietary_restrictions: List[str] = field(default_factory=list)
    confirmed: bool = False

@dataclass
class Task:
    title: str
    description: str
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    status: str = "pending"

@dataclass
class BudgetItem:
    category: str
    estimated_cost: float
    actual_cost: Optional[float] = None
    notes: str = ""

@dataclass
class EventSchedule:
    day: date
    time_slot: str
    event_name: str
    location: str
    attendees: List[Attendee] = field(default_factory=list)
    tasks: List[Task] = field(default_factory=list)
    budget_items: List[BudgetItem] = field(default_factory=list)
