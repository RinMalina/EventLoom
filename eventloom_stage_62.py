# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: EventLoom
def calculate_task_priority(task, attendees):
    """Calculate a priority score for a task based on attendee interest and budget impact."""
    base_score = 0
    if task.get('type') == 'critical':
        base_score += 10
    elif task.get('type') == 'important':
        base_score += 5
    
    interested_count = sum(1 for att in attendees if task['id'] in att.get('interested_tasks', []))
    interest_factor = min(interested_count / max(len(attendees), 1), 1.0) * 20
    
    budget_impact = abs(task.get('budget_cost', 0))
    cost_penalty = min(budget_impact / 100, 5) if task.get('budget_cost') else 0
    
    final_score = base_score + (interest_factor - cost_penalty)
    return round(final_score, 2)
