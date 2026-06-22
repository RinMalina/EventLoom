# === Stage 34: Add support for multiple local user profiles ===
# Project: EventLoom
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, base_path):
        self.base = Path(base_path) / ".profiles"
        self._ensure_dir()
    
    def _ensure_dir(self):
        if not self.base.exists():
            self.base.mkdir(parents=True)
    
    def load_profile(self, name: str) -> dict | None:
        path = self.base / f"{name}.json"
        try:
            with open(path) as f:
                return json.load(f)
        except FileNotFoundError:
            return None
    
    def save_profile(self, name: str, data: dict):
        path = self.base / f"{name}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

def get_current_user_profiles() -> list[str]:
    mgr = ProfileManager(".")
    return [p.stem for p in mgr.base.glob("*.json")]
