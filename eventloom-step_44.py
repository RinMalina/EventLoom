# === Stage 44: Add backup creation for the data file ===
# Project: EventLoom
import os, json, datetime
def backup_data(file_path):
    if not os.path.exists(file_path): return False
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path) or "."
    backup_file = f"{dir_name}/backup_{base_name}.{timestamp}"
    try:
        with open(backup_file, "w", encoding="utf-8") as dst:
            dst.write(json.dumps(load_data(file_path), indent=2))
        return True
    except Exception:
        return False

def load_data(file_path):
    if not os.path.exists(file_path): return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}
