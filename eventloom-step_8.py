# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: EventLoom
from typing import Optional, Callable
import re

def filter_events(
    events: list[dict],
    status: Optional[str] = None,
    category: Optional[str] = None,
    owner: Optional[str] = None,
    tag: Optional[str] = None
) -> list[dict]:
    """Filter event records by optional criteria."""
    if not events:
        return []

    def matches_status(e):
        return e.get('status') == status or (not status and 'status' in e)

    def matches_category(e):
        cat = category.lower() if category else None
        ev_cat = e.get('category', '').lower() if isinstance(e.get('category'), str) else ''
        # Handle multi-category lists like "Work, Fun"
        return (not cat and 'category' in e) or (cat in [ev_cat] + re.split(r'\s*,\s*', ev_cat))

    def matches_owner(e):
        own = owner.lower() if owner else None
        ev_own = e.get('owner', '').lower() if isinstance(e.get('owner'), str) else ''
        return (not own and 'owner' in e) or (own in [ev_own] + re.split(r'\s*,\s*', ev_own))

    def matches_tag(e):
        tg = tag.lower() if tag else None
        ev_tg = e.get('tag', '').lower() if isinstance(e.get('tag'), str) else ''
        return (not tg and 'tag' in e) or (tg in [ev_tg] + re.split(r'\s*,\s*', ev_tg))

    filtered = []
    for event in events:
        if matches_status(event) and matches_category(event) and matches_owner(event) and matches_tag(event):
            filtered.append(event)
    return filtered
