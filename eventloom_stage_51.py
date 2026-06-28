# === Stage 51: Add unit tests for search and filter behavior ===
# Project: EventLoom
import unittest
from eventloom import EventLoom, Attendee, Task, BudgetItem

class TestEventLoomSearch(unittest.TestCase):
    def setUp(self):
        self.event = EventLoom("TechSummit 2024")
        self.attendees = [
            Attendee("Alice", "alice@example.com"),
            Attendee("Bob", "bob@example.com"),
            Attendee("Charlie", "charlie@example.com"),
            Attendee("David", "david@example.com"),
            Attendee("Eve", "eve@example.com")
        ]
        self.tasks = [
            Task("Setup venue", 20, False),
            Task("Send invites", 5, True),
            Task("Catering order", 150, False)
        ]
        self.budgets = [BudgetItem("Venue", 5000), BudgetItem("Food", 3000)]
        
    def test_search_attendees_by_name(self):
        self.event.add_attendees(self.attendees)
        results = self.event.search_attendees(name="li")
        self.assertEqual(len(results), 2)
        self.assertTrue(any(a.name == "Alice" for a in results))
        self.assertTrue(any(a.name == "Charlie" for a in results))

    def test_search_tasks_by_status(self):
        self.event.add_tasks(self.tasks)
        completed = self.event.search_tasks(status="completed")
        pending = self.event.search_tasks(status="pending")
        self.assertEqual(len(completed), 1)
        self.assertTrue(any(t.name == "Send invites" for t in completed))
        self.assertEqual(len(pending), 2)

    def test_search_budgets_by_category(self):
        self.event.add_budgets(self.budgets)
        food_items = self.event.search_budgets(category="Food")
        venue_items = self.event.search_budgets(category="Venue")
        self.assertEqual(len(food_items), 1)
        self.assertEqual(venue_items[0].amount, 5000)

    def test_filter_combined(self):
        self.event.add_attendees(self.attendees)
        self.event.add_tasks(self.tasks)
        # Filter pending tasks related to setup (name contains 'Setup')
        results = self.event.search_tasks(status="pending", name_contains="Setup")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Setup venue")

    def test_search_empty_results(self):
        self.event.add_attendees([Attendee("Zack", "z@example.com")])
        results = self.event.search_attendees(name="nonexistent")
        self.assertEqual(len(results), 0)
