# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: EventLoom
def format_schedule_row(day, events):
    if not events:
        return f"[{day}] No events scheduled."
    lines = [f"[{day}]"]
    for i, event in enumerate(events, 1):
        time = event.get("time", "N/A")
        title = event.get("title", "Untitled")
        desc = event.get("description", "")
        if desc:
            lines.append(f"  {i}. {time} | {title}")
            lines.append(f"     {desc[:50]}...")
        else:
            lines.append(f"  {i}. {time} | {title}")
    return "\n".join(lines)

def format_attendee_list(name, role, status):
    status_str = "✓ Active" if status else "✗ Inactive"
    return f"{name} ({role}) - {status_str}"

def format_budget_item(category, amount, limit=None):
    status = "OK" if (limit is None or amount <= limit) else "OVER"
    bar_len = int((amount / limit * 100) if limit else 0)
    bar = "█" * bar_len + "░" * (100 - bar_len) if limit else "█" * 10
    return f"{category:15} | {amount:>8.2f} | [{bar}] {status}"

def format_task_list(task, priority, done):
    symbol = "[x]" if done else "[ ]"
    color = "⚠️" if priority == "high" else "ℹ️"
    return f"{symbol} {color} {task}"

def print_event_summary(events, attendees, budget, tasks):
    print("\n=== EVENT LOOM SUMMARY ===")
    for day in sorted(set(e.get("day") for e in events)):
        print(format_schedule_row(day, [e for e in events if e.get("day") == day]))
    print("\n--- Attendees ---")
    for a in attendees:
        print(format_attendee_list(a["name"], a["role"], a["status"]))
    print("\n--- Budget ---")
    for item in budget:
        print(format_budget_item(item["category"], item["amount"], item.get("limit")))
    print("\n--- Tasks ---")
    for t in tasks:
        print(format_task_list(t["task"], t["priority"], t["done"]))
