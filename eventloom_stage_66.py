# === Stage 66: Add export of a short status dashboard ===
# Project: EventLoom
def export_dashboard(events, attendees, budgets, tasks):
    from datetime import date
    today = date.today()
    lines = ["=== EventLoom Status Dashboard ===", f"Date: {today}", ""]
    for e in events:
        status = "Upcoming" if e['date'] > today else ("Past" if e['date'] < today else "Today")
        lines.append(f"[{status}] {e['name']} ({len(e.get('attendees', []))} attendees)")
    lines.append("")
    total_budget = sum(budgets.values())
    spent = sum(t.get('cost', 0) for t in tasks if t.get('completed'))
    remaining = total_budget - spent
    lines.append(f"Budget: {total_budget:.2f} | Spent: {spent:.2f} | Remaining: {remaining:.2f}")
    lines.append("")
    pending_tasks = [t['task'] for t in tasks if not t.get('completed')]
    if pending_tasks:
        lines.append("Pending Tasks:")
        for i, task in enumerate(pending_tasks[:5], 1):
            lines.append(f"  {i}. {task}")
    else:
        lines.append("All tasks completed!")
    return "\n".join(lines)
