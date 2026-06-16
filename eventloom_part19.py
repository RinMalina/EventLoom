# === Stage 19: Add undo support for the last simple mutation ===
# Project: EventLoom
import json
from typing import Optional, List, Dict, Any

class EventLoom:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
    
    def _snapshot(self) -> None:
        """Save current state to history for undo."""
        snapshot = {
            "schedules": list(self.schedules.items()),
            "attendees": list(self.attendees.items()),
            "budgets": list(self.budgets.items()),
            "tasks": list(self.tasks.items())
        }
        self.history.append(snapshot)
    
    def _undo_last_mutation(self) -> Optional[Dict[str, Any]]:
        """Revert the last state change if history exists."""
        if not self.history:
            return None
        
        # Pop and restore previous snapshot
        prev_state = self.history.pop()
        
        try:
            for key in ["schedules", "attendees", "budgets", "tasks"]:
                current_data = getattr(self, key)
                
                # Restore from snapshot (assuming simple dict/list structures)
                if isinstance(current_data, dict):
                    restored_data = {k: v for k, v in prev_state[key]}
                    setattr(self, key, restored_data)
                elif isinstance(current_data, list):
                    restored_data = [item for item in prev_state[key]]
                    setattr(self, key, restored_data)
                    
            return {"status": "reverted", "step": len(prev_state)}
        except Exception:
            # If restoration fails (e.g., complex objects), re-apply snapshot to history
            self.history.append(prev_state)
            return None

    def add_schedule(self, name: str, items: List[str]) -> None:
        if not hasattr(self, "schedules"):
            self.schedules = {}
        self._snapshot()
        self.schedules[name] = items
    
    def add_attendee(self, name: str, email: str) -> None:
        if not hasattr(self, "attendees"):
            self.attendees = {}
        self._snapshot()
        self.attendees[name] = email
    
    def set_budget(self, category: str, amount: float) -> None:
        if not hasattr(self, "budgets"):
            self.budgets = {}
        self._snapshot()
        self.budgets[category] = amount
    
    def add_task(self, task_name: str, description: str) -> None:
        if not hasattr(self, "tasks"):
            self.tasks = []
        self._snapshot()
        self.tasks.append({"name": task_name, "description": description})
