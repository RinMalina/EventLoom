# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: EventLoom
import unittest
from eventloom.helpers import validate_email, calculate_total_budget

class TestHelpers(unittest.TestCase):
    def test_validate_email_valid(self):
        self.assertTrue(validate_email("user@example.com"))
    
    def test_validate_email_invalid_format(self):
        self.assertFalse(validate_email("not-an-email"))
    
    def test_calculate_total_budget_empty(self):
        items = []
        total, breakdown = calculate_total_budget(items)
        self.assertEqual(total, 0.0)
        self.assertEqual(breakdown, {})
    
    def test_calculate_total_budget_single_item(self):
        items = [{"name": "Venue", "cost": 500}]
        total, breakdown = calculate_total_budget(items)
        self.assertEqual(total, 500.0)
        self.assertIn("Venue", breakdown)

if __name__ == "__main__":
    unittest.main()
