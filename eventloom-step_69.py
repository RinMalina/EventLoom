# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: EventLoom
def reset_demo_data(db):
    """Reset all tables to their demo seed values for manual testing."""
    import eventloom.db as db_module
    from eventloom.models import Event, Attendee, Budget, Task
    from eventloom.seed import DEMO_DATA

    # Clear tables in the right order (FKs first)
    db.delete_all(Task.__table__)
    db.delete_all(Budget.__table__)
    db.delete_all(Attendee.__table__)
    db.delete_all(Event.__table__)

    # Re-seed with demo data
    event = Event(**DEMO_DATA["event"])
    attendee = Attendee(**DEMO_DATA["attendee"])
    budget = Budget(**DEMO_DATA["budget"])
    task = Task(**DEMO_DATA["task"])

    db.insert(event)
    db.insert(attendee)
    db.insert(budget)
    db.insert(task)
