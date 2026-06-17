# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: EventLoom
def manage_tags(tags, item):
    if 'tags' not in tags: tags['tags'] = set()
    if item.get('tagged'): 
        for t in item.pop('tagged', []): tags['tags'].add(t)
        return True
    return False

def remove_tag(tags, item, tag_name):
    if 'tags' not in tags: return False
    if tag_name in tags['tags']: tags['tags'].remove(tag_name); return True
    return False

def get_tag_summary(items, tag_filter=None):
    summary = {'total': len(items), 'by_tag': {}}
    for it in items: 
        t = it.get('tagged', []) or []
        if not t and tag_filter is None: continue
        current_tags = set(t) if isinstance(t, list) else {t}
        for tg in current_tags: 
            summary['by_tag'][tg] = summary['by_tag'].get(tg, 0) + 1
    return summary

def filter_by_tags(items, tags):
    if not items or 'tags' not in tags: return items
    active_tags = set(tags.get('tags', []))
    return [it for it in items if any(it.get('tagged') and t in active_tags for t in (it.get('tagged') or []))]
