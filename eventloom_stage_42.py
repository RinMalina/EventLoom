# === Stage 42: Add CSV export without external dependencies ===
# Project: EventLoom
def export_to_csv(data, filename="event_data.csv"):
    import csv
    if isinstance(data, dict):
        headers = list(data.keys())
        rows = [data]
    elif hasattr(data, 'items'):
        headers = list(data.items())[0][1].keys() if data.items()[0][1] else []
        rows = [dict(data)]
    else:
        return False
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return True
