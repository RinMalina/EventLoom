# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: EventLoom
def demo_event_loom():
    """A compact end-to-end example of EventLoom in action."""
    from eventloom import Schedule, Attendee, Budget, TaskList

    # 1. Create a schedule
    schedule = Schedule("Spring Conference")
    schedule.add_session(9, "Opening", 30)
    schedule.add_session(10, "Keynote: AI in Education", 60)
    schedule.add_break(11, 15)
    schedule.add_session(15, "Workshop A", 45)
    schedule.add_session(17, "Closing & Q&A", 30)

    # 2. Add attendees
    alice = Attendee("Alice Chen", "alice@example.com")
    bob = Attendee("Bob Smith", "bob@example.com")
    schedule.register_alice()
    schedule.register_bob()

    # 3. Set a budget
    budget = Budget(5000)
    budget.add_item("Venue rental", 2000)
    budget.add_item("Catering", 1500)
    budget.add_item("Marketing", 1000)
    budget.add_item("Miscellaneous", 500)

    # 4. Task list
    tasks = TaskList()
    tasks.add("Secure venue", "2026-01-15")
    tasks.add("Send invitations", "2026-01-20")
    tasks.add("Order food", "2026-02-01")

    # Print a summary
    print(f"Event: {schedule.title}")
    print(f"Attendees registered: {len(schedule.attendees)}")
    print(f"Budget remaining: ${budget.remaining:.2f}")
    print(f"Pending tasks: {tasks.count()}")
