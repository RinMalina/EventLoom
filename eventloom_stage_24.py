# === Stage 24: Add grouped summaries by category or status ===
# Project: EventLoom
def generate_grouped_summary(events, category_field='category', status_field='status'):
    groups = {}
    for event in events:
        key = event.get(category_field) or 'Uncategorized'
        if key not in groups:
            groups[key] = {'total': 0, 'completed': 0, 'pending': 0}
        groups[key]['total'] += 1
        status = event.get(status_field)
        if status == 'Completed':
            groups[key]['completed'] += 1
        else:
            groups[key]['pending'] += 1
    
    for key in sorted(groups.keys()):
        data = groups[key]
        print(f"\n[{key}]")
        print(f"  Total Events: {data['total']}")
        print(f"  Completed: {data['completed']}")
        print(f"  Pending: {data['pending']}")
