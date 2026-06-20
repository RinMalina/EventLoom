# === Stage 28: Add overdue item detection based on due dates ===
# Project: EventLoom
from datetime import date, timedelta

def check_overdue_items(tasks):
    today = date.today()
    overdue_list = []
    for task in tasks:
        due_date = task.get('due_date')
        if isinstance(due_date, str):
            try:
                due_date = date.fromisoformat(due_date)
            except ValueError:
                continue
        elif not isinstance(due_date, date):
            continue
        
        is_completed = task.get('completed', False)
        
        if not is_completed and due_date < today:
            days_overdue = (today - due_date).days
            overdue_list.append({
                'id': task.get('id'),
                'title': task.get('title'),
                'due_date': due_date,
                'days_overdue': days_overdue
            })
    return overdue_list
