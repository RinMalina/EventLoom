# === Stage 46: Add a schema version field and migration helper ===
# Project: EventLoom
from typing import Dict, Any, Optional
import json
from pathlib import Path

SCHEMA_VERSION = 2

def migrate_data(data: Dict[str, Any]) -> Dict[str, Any]:
    if data.get("__schema_version", 1) < SCHEMA_VERSION:
        if "budgets" not in data and "tasks" not in data:
            data["budgets"] = []
            data["tasks"] = []
        data["__schema_version"] = SCHEMA_VERSION
    return data

def save_with_metadata(data: Dict[str, Any], path: Path) -> None:
    migrated = migrate_data(data.copy())
    with open(path, "w", encoding="utf-8") as f:
        json.dump(migrated, f, indent=2, ensure_ascii=False)
