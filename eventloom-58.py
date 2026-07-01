# === Stage 58: Add bulk update behavior for selected records ===
# Project: EventLoom
def bulk_update_records(records, updates):
    """Apply a single update dictionary to all provided records in place."""
    for record in records:
        if isinstance(updates, dict):
            for key, value in updates.items():
                if hasattr(record, key) and not callable(getattr(record, key)):
                    setattr(record, key, value)
        elif callable(updates):
            try:
                updated = updates(record)
                if updated is not None:
                    record.__dict__.update(updated)
            except Exception as e:
                print(f"Update failed for {record}: {e}")

def bulk_add_field(records, field_name, default_value=None):
    """Add a new field to all records with an optional default value."""
    if not hasattr(records[0], field_name):
        for record in records:
            setattr(record, field_name, default_value)
