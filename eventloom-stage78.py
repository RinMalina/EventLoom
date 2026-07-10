# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: EventLoom
def _format_duration(minutes: int) -> str:
    """Return a human-readable duration string."""
    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''}"
    hours, rem = divmod(minutes, 60)
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if rem > 0:
        parts.append(f"{rem} minute{'s' if rem != 1 else ''}")
    return " and ".join(parts) or "instant"


def _parse_time_slot(slot_str: str):
    """Parse a time slot string like '14:00-15:30' into (start, end)."""
    start_s, end_s = slot_str.split("-")
    from datetime import datetime
    fmt = "%H:%M"
    return datetime.strptime(start_s.strip(), fmt), datetime.strptime(end_s.strip(), fmt)


def _overlap_minutes(t1_start: str, t1_end: str, t2_start: str, t2_end: str):
    """Return overlapping minutes between two time ranges."""
    s1, e1 = _parse_time_slot(t1_start + "-" + t1_end)
    s2, e2 = _parse_time_slot(t2_start + "-" + t2_end)
    overlap_start = max(s1, s2)
    overlap_end = min(e1, e2)
    return (overlap_end - overlap_start).total_seconds() / 60


def _budget_remaining(budget: dict) -> float:
    """Return remaining budget after subtracting allocated items."""
    spent = sum(item["allocated"] for item in budget.get("items", []))
    total = budget["total"]
    return round(total - spent, 2)
