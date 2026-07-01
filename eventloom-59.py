# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: EventLoom
class BulkDeleteGuard:
    def __init__(self, repo):
        self.repo = repo
        self.confirm_flag = False

    def set_confirm(self, value):
        if not isinstance(value, bool):
            raise ValueError("Confirm flag must be a boolean")
        self.confirm_flag = value

    def execute_bulk_delete(self, target_list_name, ids_to_remove):
        if not self.confirm_flag:
            print(f"[WARN] Bulk delete disabled for '{target_list_name}'. Set confirm=True to proceed.")
            return 0
        
        removed_count = 0
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
            
            if target_list_name not in data.get("events", {}):
                print(f"[INFO] List '{target_list_name}' not found.")
                return removed_count
            
            event_data = data["events"][target_list_name]
            original_ids = set(event_data.get("items", {}).keys())
            
            for item_id in ids_to_remove:
                if item_id in original_ids:
                    del event_data["items"][item_id]
                    removed_count += 1
            
            with open("data.json", "w") as f:
                json.dump(data, f, indent=2)
            
            print(f"[OK] Removed {removed_count} items from '{target_list_name}'.")
        except Exception as e:
            print(f"[ERROR] Failed to delete items: {e}")
        
        return removed_count
