# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: EventLoom
from datetime import datetime, timedelta
import json
from pathlib import Path

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 90

def archive_old_records(records: list[dict], days: int = RETENTION_DAYS) -> tuple[list[dict], list[str]]:
    cutoff = datetime.now() - timedelta(days=days)
    active, archived_ids = [], []
    for r in records:
        if "completed_at" in r and r["completed_at"] < cutoff:
            archived_ids.append(r.pop("id"))  # remove id to avoid duplication on restore
            json.dump({**r, "_archived": True}, open(Path(ARCHIVE_DIR) / f"{r.get('event', 'unknown')}.json"), "w")
        else:
            active.append(r)
    return active, archived_ids

def restore_records(records: list[dict], ids: list[str]) -> None:
    for rid in ids:
        r = json.loads(open(Path(ARCHIVE_DIR) / f"{rid}.json").read()) if Path(f"{rid}.json").exists() else {}
        records.append(r)
