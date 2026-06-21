# === Stage 31: Add compact table rendering for long lists ===
# Project: EventLoom
from rich.table import Table, Column
def render_compact_table(data: list[dict], headers: list[str]) -> str:
    if not data: return "No data"
    col_widths = {h: min(15, len(h)) for h in headers}
    table = Table(box=None, show_header=True)
    for h in headers: table.add_column(h, width=col_widths[h], overflow="ellipsis")
    for row in data:
        cells = [str(row.get(h, ""))[:col_widths[h]] for h in headers]
        table.add_row(*cells)
    return str(table).replace("\n", "\n  ")
