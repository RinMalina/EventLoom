# === Stage 25: Add daily summary calculations ===
# Project: EventLoom
def calculate_daily_summary(event_data):
    daily_totals = {}
    for day, details in event_data.get("schedule", {}).items():
        if isinstance(details, dict) and "tasks" in details:
            total_cost = sum(t.get("cost", 0) for t in details["tasks"])
            attendees_count = len(details.get("attendees", []))
            daily_totals[day] = {
                "total_tasks": len(details["tasks"]),
                "estimated_budget": total_cost,
                "registered_attendees": attendees_count
            }
    return {"daily_breakdown": daily_totals}
