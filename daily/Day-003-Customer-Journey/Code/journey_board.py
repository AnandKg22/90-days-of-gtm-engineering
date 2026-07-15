# Journey Mapping Board State Machine
from typing import List, Dict, Any

class CustomerProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.email = ""
        self.company = ""
        self.employee_count = 0
        self.stage = "Visitor" # Starting stage
        self.events_log = []
        self.is_qualified = False

class JourneyTracker:
    def __init__(self):
        self.profiles: Dict[str, CustomerProfile] = {}

    def get_or_create_profile(self, user_id: str) -> CustomerProfile:
        if user_id not in self.profiles:
            self.profiles[user_id] = CustomerProfile(user_id)
        return self.profiles[user_id]

    def process_event(self, event: Dict[str, Any]):
        user_id = event["user_id"]
        event_name = event["event_name"]
        props = event.get("properties", {})
        
        profile = self.get_or_create_profile(user_id)
        profile.events_log.append(event)
        
        old_stage = profile.stage
        
        # 1. State Machine Transition Logic
        if event_name == "page_view":
            # If they visit the pricing page, trigger a high-intent log alert
            if props.get("url") == "/pricing":
                print(f"[INTENT ALERT] User {user_id} viewed the PRICING page!")
                
        elif event_name == "form_signup":
            profile.email = props.get("email", "")
            profile.company = props.get("company", "")
            if profile.stage == "Visitor":
                profile.stage = "Lead"
                
        elif event_name == "enrichment_completed":
            profile.employee_count = props.get("employee_count", 0)
            if profile.employee_count > 50:
                profile.is_qualified = True
                if profile.stage == "Lead":
                    profile.stage = "SQL"
                    
        elif event_name == "demo_booked":
            if profile.stage in ["Lead", "SQL"]:
                profile.stage = "Opportunity"
                
        elif event_name == "payment_success":
            profile.stage = "Customer"
            
        # 2. Log transitions
        if old_stage != profile.stage:
            print(f"[TRANSITION] Profile {user_id}: {old_stage} ===> {profile.stage}")

# Mock event feed representing a single user's journey over 3 days
mock_event_feed = [
    {"user_id": "usr_9921", "event_name": "page_view", "properties": {"url": "/home"}},
    {"user_id": "usr_9921", "event_name": "page_view", "properties": {"url": "/features"}},
    {"user_id": "usr_9921", "event_name": "page_view", "properties": {"url": "/pricing"}}, # High intent
    {"user_id": "usr_9921", "event_name": "form_signup", "properties": {"email": "captain@imsgoa.org", "company": "IMSGOA"}},
    {"user_id": "usr_9921", "event_name": "enrichment_completed", "properties": {"employee_count": 80, "industry": "Maritime Academy"}}, # SQL
    {"user_id": "usr_9921", "event_name": "demo_booked", "properties": {"scheduled_at": "2026-07-15 10:00:00"}}, # Opportunity
    {"user_id": "usr_9921", "event_name": "payment_success", "properties": {"amount": 5000.00, "plan": "Enterprise B2B"}} # Customer
]

if __name__ == "__main__":
    print("=" * 60)
    print("        INITIALIZING VIVAEXAMS JOURNEY TRACKING RUN")
    print("=" * 60)
    
    tracker = JourneyTracker()
    
    # Process events sequentially
    for step, event in enumerate(mock_event_feed, 1):
        print(f"\\n[Step {step}] Processing Event: {event['event_name']}")
        tracker.process_event(event)
        
    print("\\n" + "=" * 60)
    print("               FINAL PIPELINE STATE SUMMARY")
    print("=" * 60)
    final_profile = tracker.profiles["usr_9921"]
    print(f"User ID:        {final_profile.user_id}")
    print(f"Company:        {final_profile.company} (Size: {final_profile.employee_count})")
    print(f"Contact Email:  {final_profile.email}")
    print(f"Current Stage:  {final_profile.stage}")
    print(f"Qualified Lead: {final_profile.is_qualified}")
    print("=" * 60)
