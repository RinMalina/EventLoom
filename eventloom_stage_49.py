# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: EventLoom
from unittest import TestCase, mock
import sys
sys.path.insert(0, '..')
from eventloom.core.event_manager import EventManager

class TestEventManagerEdgeCases(TestCase):
    def setUp(self):
        self.em = EventManager()
    
    @mock.patch('eventloom.storage.file_system.read_file', return_value='[]')
    def test_delete_nonexistent_task_raises_keyerror(self, mock_read):
        with self.assertRaises(KeyError):
            self.em.delete_task("non_existent_event", "non_existent_task")

    @mock.patch('eventloom.storage.file_system.write_file')
    def test_update_budget_with_zero_amount_updates_successfully(self, mock_write):
        initial_data = [{"id": 1, "name": "Venue", "budget": 500}]
        mock_read.return_value = str(initial_data)
        self.em.update_budget("Venue", 0)
        self.assertEqual(mock_write.call_count, 1)

    @mock.patch('eventloom.storage.file_system.read_file', return_value='[]')
    def test_update_schedule_with_empty_string_clears_event(self, mock_read):
        initial_data = [{"id": 1, "name": "Setup", "time": "09:00"}]
        mock_read.return_value = str(initial_data)
        self.em.update_schedule("Event A", "", "")
        self.assertEqual(mock_write.call_count, 1)
