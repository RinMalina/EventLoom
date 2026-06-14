# === Stage 13: Add file save support using a configurable path ===
# Project: EventLoom
import os, json, sys
from pathlib import Path
CONFIG_PATH = getattr(sys.argv[1], 'path', None) or os.path.expanduser('~/.config/eventloom/settings.json')
DATA_DIR = Path(CONFIG_PATH).parent / 'data' if CONFIG_PATH else Path.cwd()
def ensure_dirs():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / '.gitkeep').touch(exist_ok=True)
def get_file_path(key):
    return DATA_DIR / f"{key}.json"
def save_event(event_data):
    path = get_file_path('event')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(event_data, f, indent=2)
    print(f"[OK] Event saved to {path}")
def load_event():
    try:
        return json.loads(get_file_path('event').read_text(encoding='utf-8')) if get_file_path('event').exists() else {}
    except Exception as e:
        print(f"[ERR] Failed to load event: {e}")
        return {}
if __name__ == '__main__':
    ensure_dirs()
    save_event({'title': 'Demo', 'date': '2024-12-31'})
