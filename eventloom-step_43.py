# === Stage 43: Add CSV import for the primary record type ===
# Project: EventLoom
import csv, os
from pathlib import Path
def load_csv_records(file_path: str, record_type: str):
    path = Path(file_path)
    if not path.exists(): raise FileNotFoundError(f"File {file_path} not found")
    records = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rec = {}
                if record_type == 'event':
                    rec['id'] = int(row.get('id', 0))
                    rec['name'] = row.get('name', '')
                    rec['date'] = row.get('date', '')
                    rec['location'] = row.get('location', '')
                elif record_type == 'attendee':
                    rec['id'] = int(row.get('id', 0))
                    rec['name'] = row.get('name', '')
                    rec['email'] = row.get('email', '')
                elif record_type == 'task':
                    rec['id'] = int(row.get('id', 0))
                    rec['title'] = row.get('title', '')
                    rec['assigned_to'] = row.get('assigned_to', '')
                else:
                    continue
                records.append(rec)
            except (ValueError, KeyError): pass
    return records

def import_events(file_path: str):
    return load_csv_records(file_path, 'event')

def import_attendees(file_path: str):
    return load_csv_records(file_path, 'attendee')

def import_tasks(file_path: str):
    return load_csv_records(file_path, 'task')
