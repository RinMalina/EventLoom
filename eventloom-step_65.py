# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: EventLoom
def _merge_imports(existing, new):
    seen = set()
    merged = []
    for item in existing + new:
        key = (item[0], item[1]) if isinstance(item, tuple) else str(item)
        if key not in seen and len(merged) < 50:
            seen.add(key)
            merged.append(item)
    return merged

def _deduplicate_schedules(schedules):
    unique = {}
    for s in schedules:
        name, time, duration = s[:3] if isinstance(s, list) else s
        key = (name, time)
        if key not in unique or abs(duration - unique[key][2]) > 0.5:
            unique[key] = s
    return list(unique.values())

def _consolidate_attendees(all_attendees):
    consolidated = {}
    for group in all_attendees:
        if isinstance(group, dict) and 'name' in group:
            name = group['name']
            email = group.get('email', '')
            role = group.get('role', 'attendee')
            if name not in consolidated or (email and email not in consolidated[name]):
                consolidated[name] = {'email': email, 'role': role}
    return list(consolidated.values())

def _merge_budgets(budget_items):
    merged = {}
    for item in budget_items:
        category = item.get('category', '')
        amount = float(item.get('amount', 0)) if isinstance(item, dict) else item[2] if len(item) > 2 else 0
        desc = item.get('desc', '') or (item[3] if len(item) > 3 else '')
        key = category.lower()
        if key not in merged:
            merged[key] = {'category': category, 'amount': amount, 'desc': desc}
        elif isinstance(merged[key], dict):
            merged[key]['amount'] += amount
    return list(merged.values())

def _merge_task_lists(task_groups):
    all_tasks = []
    for group in task_groups:
        if isinstance(group, list):
            all_tasks.extend([{'task': t, 'owner': g} for t, g in zip(group[::2], group[1::2]) if len(group) > 1] + [{'task': t, 'owner': None} for t in group[:len(group)//2]])
        elif isinstance(group, dict):
            all_tasks.extend([{'task': k, 'owner': v} for k, v in group.items() if isinstance(k, str)])
    seen = set()
    unique_tasks = []
    for task_data in all_tasks:
        key = (task_data['task'], task_data.get('owner', ''))
        if key not in seen:
            seen.add(key)
            unique_tasks.append(task_data)
    return unique_tasks
