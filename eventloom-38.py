# === Stage 38: Add data integrity checks for broken references ===
# Project: EventLoom
def validate_references(data):
    errors = []
    for event in data.get("events", []):
        if event["id"] not in [e["id"] for e in data.get("events", [])]: continue
        for attendee in event.get("attendees", []):
            if attendee["user_id"] not in [u["id"] for u in data.get("users", [])]:
                errors.append(f"Event {event['name']} references non-existent user {attendee['user_id']}.")
            for task in attendee.get("tasks", []):
                if task["task_id"] not in [t["id"] for t in data.get("tasks", [])]:
                    errors.append(f"Attendee {attendee['name']} references non-existent task {task['task_id']}.")
        for budget_item in event.get("budget_items", []):
            if budget_item["category_id"] not in [c["id"] for c in data.get("categories", [])]:
                errors.append(f"Event {event['name']} references non-existent category {budget_item['category_id']}.")
    return errors
