# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: EventLoom
def demo():
    print("=== EventLoom Demo ===")
    e = EventLoom()
    e.add_schedule("2026-05-14", 9, "Morning Briefing", ["Alice"], 50)
    e.add_schedule("2026-05-14", 11, "Keynote", ["Bob","Carol"], 300)
    e.add_attendee("Dana", "dana@example.com")
    print(e.get_schedules())
    print(e.get_attendees())
    print(f"Budget: ${e.budget}$ / Capacity: {e.capacity}")
    e.set_budget(500, 120)
    print(e.get_schedule("Morning Briefing"))
    t = TaskList()
    t.add_task("Send invites", "Dana")
    t.mark_done("Send invites")
    print(t.get_tasks())
