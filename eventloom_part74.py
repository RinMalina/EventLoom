# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: EventLoom
def diff_snapshots(before, after):
    """Compare two state snapshots and return a readable summary of changes."""
    if before == after:
        return {"status": "unchanged", "message": "Snapshots are identical."}

    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        old_val = before.get(key)
        new_val = after.get(key)
        if old_val != new_val:
            changes.append({
                "field": key,
                "old": str(old_val),
                "new": str(new_val),
                "type": "added" if old_val is None else "removed" if new_val is None else "modified",
            })

    return {
        "status": "changed",
        "changes": changes,
        "summary": f"{sum(1 for c in changes if c['type'] == 'added')} added, "
                   f"{sum(1 for c in changes if c['type'] == 'removed')} removed, "
                   f"{sum(1 for c in changes if c['type'] == 'modified')} modified",
    }

# Example usage:
# before = {"schedule": ["9am meeting", "2pm keynote"], "budget_used": 500}
# after  = {"schedule": ["9am meeting", "2pm keynote", "4pm workshop"], "budget_used": 750, "attendees": 30}
# result = diff_snapshots(before, after)
# print(result["changes"])
