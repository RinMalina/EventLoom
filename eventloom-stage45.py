# === Stage 45: Add restore from backup with validation ===
# Project: EventLoom
import json, os, hashlib, datetime

def restore_backup(backup_path, target_path):
    if not os.path.exists(target_path):
        raise FileNotFoundError(f"Target {target_path} does not exist.")
    with open(backup_path) as f:
        backup_data = json.load(f)
    with open(target_path) as f:
        current_data = json.load(f)
    required_keys = {"events", "attendees", "budgets", "tasks"}
    if set(backup_data.keys()) != required_keys:
        raise ValueError("Backup schema mismatch.")
    backup_hash = hashlib.sha256(json.dumps(backup_data, sort_keys=True).encode()).hexdigest()[:8]
    current_hash = hashlib.sha256(json.dumps(current_data, sort_keys=True).encode()).hexdigest()[:8]
    if backup_hash == current_hash:
        print("Backup is identical to current state; skipping restore.")
        return False
    with open(target_path, "w") as f:
        json.dump(backup_data, f, indent=2)
    print(f"Restored from {backup_path} (hash: {backup_hash}).")
    return True
