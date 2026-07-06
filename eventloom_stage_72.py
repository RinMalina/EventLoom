# === Stage 72: Add Markdown report export ===
# Project: EventLoom
def export_markdown_report(event):
    """Export a compact markdown report of an event."""
    lines = []
    lines.append(f"# {event.name}\n")
    if event.date:
        lines.append(f"**Date:** {event.date.strftime('%Y-%m-%d')}\n")
    location = ", ".join(event.venue) if isinstance(event.venue, list) else str(event.venue)
    lines.append(f"**Location:** {location}\n\n")

    if event.attendees:
        lines.append("## Attendees\n")
        for name in sorted(event.attendees):
            lines.append(f"- {name}")
        lines.append("\n")

    if event.budget:
        total = sum(b.total_cost for b in event.budget)
        lines.append(f"## Budget\n")
        for item in event.budget:
            lines.append(f"- **{item.item}**: ${item.quantity * item.unit_price:.2f}")
        lines.append(f"\n**Total:** ${total:.2f}\n\n")

    if event.tasks:
        lines.append("## Tasks\n")
        for task in sorted(event.tasks, key=lambda t: (t.completed, t.title)):
            status = "✅" if task.completed else "⬜"
            lines.append(f"- {status} **{task.title}**\n")
    return "\n".join(lines)
