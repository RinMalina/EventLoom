# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: EventLoom
def repair_data_integrity(data):
    if "attendees" in data:
        for i, att in enumerate(data["attendees"]):
            if isinstance(att.get("email"), str) and "@" not in att["email"]:
                data["attendees"][i]["email"] = f"{att['name'].lower().replace(' ', '.')}@example.com"
    if "budgets" in data:
        for item in data["budgets"]:
            try:
                float(item.get("amount", 0))
            except (ValueError, TypeError):
                item["amount"] = 0.0
    if "tasks" in data:
        for task in data["tasks"]:
            if not isinstance(task.get("status"), str) or task["status"] not in ["pending", "done"]:
                task["status"] = "pending"
    return data
