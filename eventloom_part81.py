# === Stage 81: Add final README text as a module string with usage examples ===
# Project: EventLoom
# EventLoom – Usage Examples & Quick Reference
from eventloom import Schedule, Attendee, Budget, TaskList


class DemoEvent:
    """Run a full demo of the toolkit."""

    def run(self):
        # Schedules
        schedule = Schedule("Spring Conference")
        schedule.add_slot(9, 10, "Keynote", attendees=["Alice", "Bob"])
        schedule.add_slot(10, 11, "Workshop A", attendees=["Charlie"])

        # Attendees
        alice = Attendee(name="Alice", email="alice@example.com")
        bob = Attendee(name="Bob", email="bob@example.com")
        attendee_list = [alice, bob]

        # Budgets
        budget = Budget("Spring Conference")
        budget.add_item("Venue", 500)
        budget.add_item("Catering", 200)
        total = budget.total()
        print(f"Total estimated cost: ${total}")

        # Task Lists
        tasks = TaskList("Conference Setup")
        tasks.add_task("Book venue", "Alice")
        tasks.add_task("Order food", "Bob")
        completed = [t for t in tasks if t["status"] == "done"]
        print(f"Completed: {len(completed)} / {len(tasks)}")

        # Combine everything into a report
        print("\n--- Event Report ---")
        print(f"Event: {schedule.name}")
        print(f"Attendees ({len(attendee_list)}): {[a.name for a in attendee_list]}")
        print(f"Budget total: ${total}")
        print(f"Tasks done: {len(completed)}/{len(tasks)}")


if __name__ == "__main__":
    demo = DemoEvent()
    demo.run()
