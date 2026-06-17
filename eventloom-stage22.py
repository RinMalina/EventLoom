# === Stage 22: Add favorite records and quick favorite listing ===
# Project: EventLoom
from typing import Optional, Dict, List
import json
from pathlib import Path

class FavoriteManager:
    def __init__(self, data_dir: str = "data"):
        self.data_path = Path(data_dir) / "favorites.json"
        self._ensure_file()

    def _ensure_file(self):
        if not self.data_path.exists():
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_favorite(self, name: str, category: Optional[str] = None, notes: Optional[str] = None) -> bool:
        try:
            favorites = self._load()
            existing = next((item for item in favorites if item['name'] == name), None)
            if existing:
                return False
            
            record = {
                'id': len(favorites) + 1,
                'name': name,
                'category': category or 'General',
                'notes': notes or '',
                'created_at': self._now()
            }
            favorites.append(record)
            self._save(favorites)
            return True
        except Exception:
            return False

    def remove_favorite(self, name: str) -> bool:
        try:
            favorites = self._load()
            count = sum(1 for item in favorites if item['name'] == name)
            if count == 0:
                return False
            
            new_favs = [item for item in favorites if item['name'] != name]
            if len(new_favs) < len(favorites):
                self._save(new_favs)
            return True
        except Exception:
            return False

    def get_all(self, category_filter: Optional[str] = None) -> List[Dict]:
        try:
            favorites = self._load()
            if not category_filter:
                return favorites
            
            filtered = [item for item in favorites if item['category'] == category_filter]
            return sorted(filtered, key=lambda x: x['created_at'], reverse=True)
        except Exception:
            return []

    def _load(self) -> List[Dict]:
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = []
        return data

    def _save(self, items: List[Dict]):
        try:
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(items, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _now(self):
        from datetime import datetime
        return datetime.now().isoformat()
