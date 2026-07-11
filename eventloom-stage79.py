# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: EventLoom
def self_check():
    print("=== EventLoom Self-Check ===")
    from eventloom import schedule, attendee, budget, task
    s = schedule.create(name="Tech Conference", date="2024-11-15", venue="Convention Center")
    a = attendee.add(name="Alice", email="alice@example.com")
    b = budget.set(event_name=s.name, total=5000)
    t = task.create(description="Setup stage", assigned_to=a, deadline="2024-11-14")
    assert s is not None and a is not None and b is not None and t is not None
    print(f"Schedule: {s.name}")
    print(f"Attendee: {a.name} <{a.email}>")
    print(f"Budget: ${b.total}")
    print(f"Task: {t.description} by {t.assigned_to.name} on {t.deadline}")
    print("All checks passed.")
