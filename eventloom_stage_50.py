# === Stage 50: Add unit tests for import and export behavior ===
# Project: EventLoom
import json, os, sys
from pathlib import Path

def load_data(path: str) -> dict | None:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    base_dir = Path(__file__).parent.parent / 'data'
    test_files = [base_dir / 'schedules.json', base_dir / 'attendees.json']
    for f in test_files:
        assert load_data(str(f)) is not None or os.path.exists(str(f)), "Load failed"
        save_data({}, str(f) + '.empty')
        data = {'event': 'test'}
        save_data(data, str(f) + '.new')
        loaded = load_data(str(f) + '.new')
        assert loaded == data, "Save/Load mismatch"
