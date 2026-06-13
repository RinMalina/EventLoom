# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: EventLoom
from operator import itemgetter, attrgetter
def sort_events(events, key='date'):
    if key == 'title': return sorted(events, key=itemgetter('title'))
    if key == 'priority': return sorted(events, key=lambda e: -e.get('priority', 0))
    if key == 'updated_at': return sorted(events, key=itemgetter('updated_at'), reverse=True)
    if key == 'date': return sorted(events, key=itemgetter('date'))
    return events
