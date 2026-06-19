# === Stage 27: Add monthly summary calculations ===
# Project: EventLoom
def calculate_monthly_summary(events, expenses):
    from datetime import date
    months = {}
    for event in events:
        m_key = f"{event['month']}/{event['year']}"
        if m_key not in months:
            months[m_key] = {'revenue': 0.0, 'costs': 0.0}
        months[m_key]['revenue'] += event.get('budget', {}).get('total', 0)
    for expense in expenses:
        m_key = f"{expense['month']}/{expense['year']}"
        if m_key not in months:
            months[m_key] = {'revenue': 0.0, 'costs': 0.0}
        months[m_key]['costs'] += expense.get('amount', 0)
    for month_data in months.values():
        month_data['profit'] = round(month_data['revenue'] - month_data['costs'], 2)
    return list(months.items())
