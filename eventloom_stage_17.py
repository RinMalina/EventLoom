# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: EventLoom
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("=== DRY RUN MODE ===")
        for line in open(__file__):
            if "print" in line:
                continue
            if "return" in line or "raise" in line:
                continue
            stripped = line.strip()
            if not stripped.startswith("#"):
                print(f"# Would execute: {stripped}")
        return True
    return False

def safe_write(path, content):
    import os
    if dry_run_mode():
        print(f"[DRY-RUN] Would write to '{path}':")
        for line in content.splitlines():
            print(f"  {line}")
        return False
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write '{path}': {e}")
        return False

def safe_remove(path):
    import os
    if dry_run_mode():
        print(f"[DRY-RUN] Would remove file: '{path}'")
        return True
    try:
        os.remove(path)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to remove '{path}': {e}")
        return False

def safe_rename(old_path, new_path):
    import shutil
    if dry_run_mode():
        print(f"[DRY-RUN] Would rename '{old_path}' -> '{new_path}'")
        return True
    try:
        shutil.move(old_path, new_path)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to rename files: {e}")
        return False
