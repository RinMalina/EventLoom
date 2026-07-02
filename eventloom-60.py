# === Stage 60: Add saved views for frequently used filters ===
# Project: EventLoom
class SavedViewManager:
    def save_view(self, name: str, filters: dict) -> None:
        with open("views.json", "w") as f:
            json.dump({name: filters}, f, indent=2)

    def load_views(self) -> dict:
        try:
            with open("views.json") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def apply_view(self, name: str) -> None:
        views = self.load_views()
        if name in views:
            filters = views[name]
            for key, value in filters.items():
                setattr(EventLoomSystem, f"filter_{key}", value)
