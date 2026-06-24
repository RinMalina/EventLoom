# === Stage 40: Add plain text report export ===
# Project: EventLoom
def export_report(event_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"EventLoom Report\n")
        f.write("=" * 40 + "\n")
        for section in ['schedule', 'attendees', 'budgets', 'tasks']:
            if section in event_data and event_data[section]:
                f.write(f"\n{section.upper()}\n")
                for item in event_data[section]:
                    f.write(f"  - {item['title']}: {item.get('notes', '')}\n")
        f.write("\n" + "=" * 40 + "\nEnd of Report\n")
