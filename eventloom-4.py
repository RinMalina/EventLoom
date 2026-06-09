# === Stage 4: Implement create operations for the primary records ===
# Project: EventLoom
from datetime import datetime, date
import uuid

def create_event(name: str, start_date: date, end_date: date, location: str) -> dict:
    event_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    return {
        "id": event_id,
        "name": name,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "location": location,
        "created_at": created_at.isoformat(),
        "status": "draft"
    }

def create_attendee(name: str, email: str) -> dict:
    attendee_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    return {
        "id": attendee_id,
        "name": name,
        "email": email,
        "created_at": created_at.isoformat(),
        "status": "pending"
    }

def create_task(title: str, description: str, event_id: str) -> dict:
    task_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "event_id": event_id,
        "created_at": created_at.isoformat(),
        "completed": False,
        "priority": "medium"
    }

def create_budget_item(description: str, amount: float, category: str) -> dict:
    item_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    return {
        "id": item_id,
        "description": description,
        "amount": amount,
        "category": category,
        "created_at": created_at.isoformat(),
        "approved": False
    }
