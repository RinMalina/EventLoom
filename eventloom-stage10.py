# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: EventLoom
class SearchIndex:
    def __init__(self):
        self._index = {}  # Maps lowercase field_value -> list of (field, original_value)

    def index_field(self, record, field_name):
        value = str(record.get(field_name, '')).lower().strip()
        if not value: return
        key = f"{field_name}:{value}"
        self._index.setdefault(key, []).append((field_name, record[field_name]))

    def search(self, query, fields=None):
        results = []
        q = query.lower().strip()
        for field in (fields or ['name', 'event', 'task']):
            key = f"{field}:{q}"
            if key in self._index:
                for fname, val in self._index[key]:
                    if val not in results:
                        results.append(val)
        return list(set(results))

    def clear(self):
        self._index.clear()
