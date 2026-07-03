# === Stage 64: Add validation for relationship references ===
# Project: EventLoom
class ValidationError(Exception): pass

def validate_references(event, data):
    if 'attendees' in event and 'attendee_ids' in data:
        for aid in data['attendee_ids']:
            if aid not in [a.id for a in event.get('attendees', [])]:
                raise ValidationError(f"Attendee ID {aid} does not exist.")

    if 'tasks' in event and 'task_ids' in data:
        for tid in data['task_ids']:
            if tid not in [t.id for t in event.get('tasks', [])]:
                raise ValidationError(f"Task ID {tid} does not exist.")

    return True
