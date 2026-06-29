# === Stage 53: Add command help text and usage examples ===
# Project: EventLoom
import argparse, sys

def print_help():
    prog = "eventloom"
    epilog = """Examples:
  %(prog)s schedule --date 2024-12-31      Show daily agenda for a specific date.
  %(prog)s budget --category food          List all expenses tagged 'food'.
  %(prog)s attendee --name alice           Print contact info for Alice.
  %(prog)s task --status pending           List tasks not yet completed."""

    parser = argparse.ArgumentParser(
        prog=prog, description="Event planning toolkit: manage schedules, attendees, budgets, and tasks.", epilog=epilog
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Schedule command
    p_sched = subparsers.add_parser("schedule", help="View or add event schedule entries.")
    p_sched.add_argument("--date", "-d", type=str, default="", help="Date in YYYY-MM-DD format (optional).")
    p_sched.add_argument("--add", "-a", action="store_true", help="Enable adding new events via interactive prompt.")

    # Attendee command
    p_att = subparsers.add_parser("attendee", help="Manage attendee list and details.")
    p_att.add_argument("--name", "-n", type=str, default="", help="Name of the attendee to look up or add.")
    p_att.add_argument("--email", "-e", type=str, default=None, help="Email address for the attendee.")

    # Budget command
    p_bud = subparsers.add_parser("budget", help="Track event expenses and budget limits.")
    p_bud.add_argument("--category", "-c", type=str, default="", help="Filter by expense category (e.g., food).")
    p_bud.add_argument("--limit", "-l", type=float, default=None, help="Set or check the total budget limit.")

    # Task command
    p_task = subparsers.add_parser("task", help="Manage to-do lists for event preparation.")
    p_task.add_argument("--status", "-s", choices=["pending", "completed"], default="pending", help="Filter by task status.")
    p_task.add_argument("--add", "-a", action="store_true", help="Add a new interactive task.")

    args = parser.parse_args()
    print(f"Usage: {prog} [command] [options]")
    if not args.command:
        parser.print_help(sys.stderr)
        return 1
    # Placeholder logic for actual command execution would go here based on parsed args.
    return 0

if __name__ == "__main__":
    sys.exit(print_help())
