# === Stage 37: Add recommendations for the next useful action ===
# Project: EventLoom
import sys, json, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from eventloom.core.storage import Storage
from eventloom.views.schedule_view import ScheduleView
from eventloom.views.budget_view import BudgetView
from eventloom.utils.recommender import Recommender

def main():
    storage = Storage()
    recommender = Recommender(storage)
    
    if not storage.events:
        print("No events found. Create an event first.")
        return
    
    current_event_id = input("\nEnter Event ID (or press Enter for latest): ").strip() or list(storage.events.keys())[-1]
    event_data = storage.get_event(current_event_id)
    
    if not event_data:
        print(f"Event {current_event_id} not found.")
        return
    
    schedule_view = ScheduleView(event_data, storage)
    budget_view = BudgetView(event_data, storage)
    
    actions = recommender.generate_next_actions(event_data, current_event_id)
    
    if not actions:
        print("No specific recommendations available at this moment.")
        return

    print("\n--- Recommended Next Actions ---")
    for i, action in enumerate(actions, 1):
        print(f"{i}. {action['title']}")
        if action.get('details'):
            print(f"   Details: {action['details'][:80]}...")
    
    try:
        choice = input("\nSelect an action number (or press Enter to skip): ").strip()
        if not choice and actions:
            print("Skipping recommendation.")
            return
        
        selected_action = actions[int(choice) - 1] if choice else None
        
        if selected_action:
            confirm = input(f"Execute '{selected_action['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                success, message = storage.execute_action(selected_action.get('command'))
                print(message)
                
    except ValueError:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
