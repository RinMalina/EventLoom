# === Stage 26: Add weekly summary calculations ===
# Project: EventLoom
def calculate_weekly_summary(events):
    """Aggregate event data by week for reporting."""
    weekly_data = {}
    for event in events:
        if 'date' not in event: continue
        try:
            date_obj = datetime.fromisoformat(event['date'].replace('Z', '+00:00'))
            iso_week = date_obj.isocalendar()[1]
            week_key = f"Week {iso_week}"
        except Exception:
            continue
        
        if week_key not in weekly_data:
            weekly_data[week_key] = {'count': 0, 'total_budget': 0.0, 'attendees': set()}
        
        weekly_data[week_key]['count'] += 1
        weekly_data[week_key]['total_budget'] += float(event.get('budget', 0)) or 0
        
        if event.get('attendee_ids'):
            for aid in event['attendee_ids']:
                weekly_data[week_key]['attendees'].add(aid)
    
    return {k: {'count': v['count'], 'total_budget': round(v['total_budget'], 2), 
                 'unique_attendees': len(v['attendees'])} for k, v in sorted(weekly_data.items())}
