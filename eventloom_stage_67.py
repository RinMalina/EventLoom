# === Stage 67: Add a function that returns key project metrics ===
# Project: EventLoom
def get_project_metrics(schedules, attendees, budgets, tasks):
    total_events = len(schedules) if schedules else 0
    unique_attendees_count = set()
    for event in (schedules or []):
        if isinstance(event.get('attendees'), list):
            unique_attendees_count.update(event['attendees'])
    
    total_budget_allocated = sum(budgets.values()) if budgets else 0.0
    completed_tasks = len([t for t in tasks if t.get('status') == 'done' or t.get('completed', False)])
    pending_tasks = len(tasks) - completed_tasks
    
    avg_attendees_per_event = (total_events > 0 and sum(len(e.get('attendees', [])) for e in schedules) / total_events) or 0.0
    
    metrics = {
        'total_events': total_events,
        'unique_attendees_count': len(unique_attendees_count),
        'total_budget_allocated': round(total_budget_allocated, 2),
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_rate': round((completed_tasks / max(len(tasks), 1)) * 100, 1) if tasks else 0.0,
        'avg_attendees_per_event': round(avg_attendees_per_event, 1)
    }
    
    return metrics
