# === Stage 73: Add a lightweight HTML report export ===
# Project: EventLoom
def export_html_report(self, output_path="eventloom_report.html"):
    """Export current event data as a simple HTML report."""
    lines = []
    lines.append("<!DOCTYPE html><html><head><title>EventLoom Report</title>")
    lines.append("<style>body{font-family:monospace;max-width:800px;margin:auto;padding:2em;}table{border-collapse:collapse;width:100%;}th,td{text-align:left;border-bottom:1px solid #ccc;padding:6px 12px;}th{background:#f0f0f0;}</style>")
    lines.append("</head><body><h1>EventLoom Report</h1>")

    for section in self._sections.values():
        if isinstance(section, Schedule):
            lines.append("<h2>Schedule</h2><table><tr><th>Time</th><th>Title</th></tr>")
            for entry in sorted(section.entries, key=lambda e: e.time):
                lines.append(f"<tr><td>{entry.time}</td><td>{entry.title}</td></tr>")
            lines.append("</table>")
        elif isinstance(section, Attendees):
            lines.append("<h2>Attendees</h2><table><tr><th>Name</th><th>Email</th></tr>")
            for name, email in section.items():
                lines.append(f"<tr><td>{name}</td><td>{email}</td></tr>")
            lines.append("</table>")

    return "\n".join(lines) + "\n</body></html>"

self._export_html = export_html_report(self)
