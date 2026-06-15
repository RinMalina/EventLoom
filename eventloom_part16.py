# === Stage 16: Add argparse support for the most common commands ===
# Project: EventLoom
import argparse

def main():
    parser = argparse.ArgumentParser(prog="eventloom", description="Event planning toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Schedule command
    sched_parser = subparsers.add_parser("schedule", help="Manage event schedules")
    sched_parser.add_argument("--add", action="store_true", help="Add a new schedule entry")
    sched_parser.add_argument("--list", action="store_true", help="List all schedules")

    # Attendees command
    att_parser = subparsers.add_parser("attendees", help="Manage attendees")
    att_parser.add_argument("--add", type=str, metavar="NAME", help="Add an attendee by name")
    att_parser.add_argument("--remove", type=str, metavar="NAME", help="Remove an attendee")

    # Budget command
    bud_parser = subparsers.add_parser("budget", help="Manage budgets")
    bud_parser.add_argument("--add", type=float, metavar="AMOUNT", help="Add a budget item")
    bud_parser.add_argument("--list", action="store_true", help="List all budget items")

    # Tasks command
    task_parser = subparsers.add_parser("tasks", help="Manage tasks")
    task_parser.add_argument("--add", type=str, metavar="TASK", help="Add a new task")
    task_parser.add_argument("--complete", type=str, metavar="TASK", help="Mark a task as complete")

    args = parser.parse_args()
    if not hasattr(args, "command"):
        parser.print_help()
        return 1
    print(f"Executing command: {args.command}")
    # Placeholder for actual logic implementation based on parsed arguments
    return 0

if __name__ == "__main__":
    exit(main())
