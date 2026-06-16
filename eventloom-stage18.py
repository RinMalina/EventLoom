# === Stage 18: Add an activity log with timestamps and action names ===
# Project: EventLoom
class ActivityLog:
    def __init__(self, log_file="event_loom.log"):
        self.file = log_file

    def _ensure_dir(self):
        import os
        dir_name = os.path.dirname(self.file) or "."
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def write(self, action: str, details: dict | None = None):
        from datetime import datetime
        self._ensure_dir()
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] {action}"
        if details:
            for k, v in details.items():
                line += f" | {k}: {v}"
        with open(self.file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def log_event_created(self, name: str):
        self.write("EVENT_CREATED", {"name": name})

    def log_attendee_added(self, name: str):
        self.write("ATTENDEE_ADDED", {"name": name})

    def log_budget_updated(self, total: float):
        self.write("BUDGET_UPDATED", {"total": total})

    def log_task_completed(self, task_id: int):
        self.write("TASK_COMPLETED", {"task_id": task_id})
