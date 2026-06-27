# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: EventLoom
from datetime import date, timedelta
import json

def run_demo():
    # Initialize simple in-memory storage for the demo
    events = [
        {"id": 1, "name": "Tech Summit", "date": date.today() + timedelta(days=2), "budget": 5000},
        {"id": 2, "name": "Workshop A", "date": date.today() + timedelta(days=3), "budget": 1200}
    ]
    
    attendees = [
        {"id": 101, "name": "Alice", "email": "alice@example.com"},
        {"id": 102, "name": "Bob", "email": "bob@example.com"}
    ]
    
    tasks = [
        {"event_id": 1, "title": "Book venue", "status": "pending"},
        {"event_id": 1, "title": "Send invites", "status": "in_progress"}
    ]
    
    # Simulate workflow: Add attendee, update task status, log summary
    new_attendee = {"id": 103, "name": "Charlie", "email": "charlie@example.com"}
    attendees.append(new_attendee)
    
    for event in events:
        if event["id"] == 1:
            task_to_update = next(t for t in tasks if t["event_id"] == event["id"])
            task_to_update["status"] = "completed"
            
    # Generate summary report
    total_budget = sum(e["budget"] for e in events)
    active_tasks = len([t for t in tasks if t["status"] != "completed"])
    
    print(f"Demo EventLoom Workflow:")
    print(f"- Total Events: {len(events)}")
    print(f"- Total Attendees: {len(attendees)}")
    print(f"- Remaining Budget: ${total_budget}")
    print(f"- Active Tasks: {active_tasks}")
    
    # Save state to file for persistence demo
    with open("eventloom_demo_state.json", "w") as f:
        json.dump({"events": events, "attendees": attendees, "tasks": tasks}, f)

if __name__ == "__main__":
    run_demo()
