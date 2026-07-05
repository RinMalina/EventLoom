# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: EventLoom
def generate_changelog(activity_log):
    """Generate a compact changelog from the activity log."""
    if not activity_log:
        return "No changes recorded."
    
    entries = []
    for entry in sorted(activity_log, key=lambda x: x['timestamp'], reverse=True):
        author = entry.get('author', 'Unknown')
        action = entry.get('action', 'unknown_action').replace('_', ' ').title()
        details = entry.get('details', '')
        
        if details:
            line = f"- [{action}] by {author}: {details}"
        else:
            line = f"- [{action}] by {author}"
        entries.append(line)
    
    return "\n".join(entries[:10])
