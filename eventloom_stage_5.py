# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: EventLoom
def update_event_schedule(event_id, new_date):
    if event_id not in schedules:
        print(f"Error: Event with ID {event_id} not found.")
        return False
    schedules[event_id]['date'] = new_date
    return True

def update_attendee_status(event_id, attendee_name, status):
    if event_id not in attendees:
        print(f"Error: Event with ID {event_id} not found.")
        return False
    for name, info in attendees[event_id].items():
        if name == attendee_name:
            info['status'] = status
            return True
    print(f"Error: Attendee '{attendee_name}' not found in event {event_id}.")
    return False

def update_budget_item(event_id, item_name, new_amount):
    if event_id not in budgets:
        print(f"Error: Budget for event {event_id} not found.")
        return False
    if item_name not in budgets[event_id]:
        print(f"Error: Item '{item_name}' not found in budget for event {event_id}.")
        return False
    budgets[event_id][item_name] = new_amount
    return True

def update_task_status(event_id, task_name, status):
    if event_id not in tasks:
        print(f"Error: Task list for event {event_id} not found.")
        return False
    for name, info in tasks[event_id].items():
        if name == task_name:
            info['status'] = status
            return True
    print(f"Error: Task '{task_name}' not found in event {event_id}.")
    return False
