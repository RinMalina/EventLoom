# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: EventLoom
def safe_load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[EventLoom] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[EventLoom] Malformed JSON in '{path}': {e}")
        return {}
