# === Stage 14: Add file load support with fallback demo data ===
# Project: EventLoom
def load_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "events": [
                {"name": "Kickoff", "date": "2024-10-01", "attendees": ["Alice"], "budget": 500, "tasks": ["Book venue"]}
            ],
            "schedules": [{"event_id": 0, "time": "09:00"}],
            "attendees": {"Alice": {"email": "alice@example.com", "role": "Speaker"}},
            "budgets": {"total": 500, "spent": 200}
        }
