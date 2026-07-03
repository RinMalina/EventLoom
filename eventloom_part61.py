# === Stage 61: Add performance timing for core list and search operations ===
# Project: EventLoom
import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] took {end - start:.6f}s")
        return result
    return wrapper

def benchmark_list_ops():
    from eventloom import EventLoom
    loom = EventLoom("test_event.yaml")
    
    # Populate with dummy data for realistic timing
    for i in range(50):
        loom.add_attendee(f"Attendee_{i}", "attendee@test.com", 100.0)
        loom.add_task(f"Task_{i}", "pending", f"user_{i % 3}")
    
    # Time attendee lookup by name (O(N))
    @timed
    def find_attendee_by_name(name):
        return loom.attendees.get(name, None)
    
    # Time task search by status (linear scan over tasks dict)
    @timed
    def get_pending_tasks():
        return [t for t in loom.tasks.values() if t.status == "pending"]
    
    # Run benchmarks
    find_attendee_by_name("Attendee_0")
    get_pending_tasks()

if __name__ == "__main__":
    benchmark_list_ops()
