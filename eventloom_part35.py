# === Stage 35: Add active user switching and user-specific records ===
# Project: EventLoom
from dataclasses import field, dataclass
import json
from pathlib import Path

@dataclass
class User:
    name: str
    role: str = "attendee"
    active: bool = True
    
def load_users(file_path: Path) -> dict[str, User]:
    users_file = file_path / "users.json"
    if not users_file.exists():
        return {}
    with open(users_file) as f:
        data = json.load(f)
    return {u["name"]: User(**u) for u in data}

def save_users(file_path: Path, users: dict[str, User]) -> None:
    users_file = file_path / "users.json"
    with open(users_file, "w") as f:
        json.dump([{"name": u.name, "role": u.role, "active": u.active} for u in users.values()], f)

def get_active_user(file_path: Path) -> User | None:
    users = load_users(file_path)
    active = next((u for u in users.values() if u.active), None)
    return active
