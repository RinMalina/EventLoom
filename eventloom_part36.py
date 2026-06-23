# === Stage 36: Add templates for quickly creating common records ===
# Project: EventLoom
from typing import Optional, Dict, Any
from datetime import date
import json

class RecordTemplate:
    """Utility to generate pre-filled records for common event types."""
    
    @staticmethod
    def create_schedule_item(name: str, start_time: str, end_time: str, location: str = "TBD") -> Dict[str, Any]:
        return {
            "id": f"SCH-{date.today().strftime('%Y%m%d')}-{name[:4].upper()}",
            "title": name,
            "start": start_time,
            "end": end_time,
            "location": location,
            "status": "planned"
        }

    @staticmethod
    def create_attender(name: str, email: str, role: Optional[str] = None) -> Dict[str, Any]:
        return {
            "id": f"ATT-{date.today().strftime('%Y%m%d')}-{name[:4].upper()}",
            "full_name": name,
            "email": email,
            "role": role or "attendee",
            "status": "confirmed"
        }

    @staticmethod
    def create_budget_item(category: str, amount: float, description: Optional[str] = None) -> Dict[str, Any]:
        return {
            "id": f"BUD-{date.today().strftime('%Y%m%d')}-{category[:4].upper()}",
            "category": category,
            "amount": amount,
            "description": description or "",
            "status": "pending"
        }

    @staticmethod
    def create_task(title: str, assignee: Optional[str] = None, due_date: Optional[date] = None) -> Dict[str, Any]:
        return {
            "id": f"TAS-{date.today().strftime('%Y%m%d')}-{title[:4].upper()}",
            "title": title,
            "assignee": assignee or "",
            "due_date": due_date.isoformat() if due_date else None,
            "status": "open"
        }

    @staticmethod
    def load_templates_from_file(file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Template file not found at {file_path}")
            return {}
