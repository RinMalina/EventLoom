# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: EventLoom
def delete_event(event_id, confirm=False):
    if event_id in events:
        if confirm or input(f"Delete event '{events[event_id]['name']}'? (y/n): ").lower() == 'y':
            del events[event_id]
            print(f"Event '{events[event_id]['name']}' deleted.")
            return True
        else:
            print("Deletion cancelled.")
            return False
    else:
        print(f"Event with ID {event_id} not found.")
        return False

def delete_attendee(event_id, attendee_name):
    if event_id in events and attendee_name in events[event_id]['attendees']:
        del events[event_id]['attendees'][attendee_name]
        print(f"Attendee '{attendee_name}' removed from event '{events[event_id]['name']}'.")
        return True
    else:
        print("Attendee not found in the specified event.")
        return False

def delete_task(event_id, task_name):
    if event_id in events and 'tasks' in events[event_id]:
        if task_name in events[event_id]['tasks']:
            del events[event_id]['tasks'][task_name]
            print(f"Task '{task_name}' removed from event '{events[event_id]['name']}'.")
            return True
        else:
            print("Task not found in the specified event.")
            return False
    else:
        print("Event or tasks list not found.")
        return False

def delete_budget_item(event_id, item_name):
    if event_id in events and 'budget' in events[event_id]:
        if item_name in events[event_id]['budget']:
            del events[event_id]['budget'][item_name]
            print(f"Budget item '{item_name}' removed from event '{events[event_id]['name']}'.")
            return True
        else:
            print("Budget item not found in the specified event.")
            return False
    else:
        print("Event or budget list not found.")
        return False
