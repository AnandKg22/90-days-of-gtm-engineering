# Segment CDP Simulator & Event Router
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. Target Event Tracking Plan Schemas
TRACKING_PLAN = {
    "Exam Completed": {
        "exam_id": str,
        "score": (int, float),
        "pass_status": bool
    },
    "Subscription Upgraded": {
        "plan_tier": str,
        "seats_added": int,
        "amount": (int, float)
    }
}

class SegmentCDP:
    def __init__(self):
        self.identity_graph: Dict[str, str] = {} # anonymous_id -> user_id
        self.user_traits: Dict[str, Dict[str, Any]] = {} # user_id -> traits
        
    def identify(self, anonymous_id: str, user_id: str, traits: Dict[str, Any]):
        # Bind Anonymous ID to Identified User ID in the graph
        self.identity_graph[anonymous_id] = user_id
        self.user_traits[user_id] = traits
        
        print(f"\n[CDP IDENTIFY] Mapping anonymous cookie '{anonymous_id}' to user '{user_id}'")
        print(f"  Traits Logged: {traits}")
        print("  - [ROUTED TO HUBSPOT]: Created/Enriched contact profile")
        
    def group(self, user_id: str, group_id: str, traits: Dict[str, Any]):
        print(f"\n[CDP GROUP] Linking User '{user_id}' to Organization Group '{group_id}'")
        print(f"  Group Traits: {traits}")
        print(f"  - [ROUTED TO HUBSPOT]: Associated contact with company '{traits.get('name')}'")
        
    def track(self, user_id: str, event_name: str, properties: Dict[str, Any]):
        print(f"\n[CDP TRACK] Event: '{event_name}' received for user '{user_id}'")
        
        # 1. Schema Validation against Tracking Plan
        if event_name not in TRACKING_PLAN:
            print(f"  [SCHEMA ERROR] Rejecting event: '{event_name}' is not in the Tracking Plan!")
            return
            
        rules = TRACKING_PLAN[event_name]
        for prop_name, prop_type in rules.items():
            if prop_name not in properties:
                print(f"  [SCHEMA ERROR] Rejecting event: Missing required property '{prop_name}'")
                return
                
            val = properties[prop_name]
            if not isinstance(val, prop_type):
                print(f"  [SCHEMA ERROR] Rejecting event: Property '{prop_name}' value {val} has type "
                      f"{type(val).__name__}, expected {prop_type}")
                return
                
        # 2. Validation Passed -> Route to destinations (Multiplexing)
        print(f"  [SCHEMA OK] Event validated successfully. Routing to destinations...")
        print(f"  - [ROUTED TO GOOGLE ANALYTICS]: Logged event '{event_name}' with properties: {properties}")
        print(f"  - [ROUTED TO HUBSPOT CRM]: Updated Company metrics with properties: {properties}")

if __name__ == "__main__":
    cdp = SegmentCDP()
    
    print("=" * 65)
    print("           INITIALIZING SEGMENT CDP EVENT ROUTER")
    print("=" * 65)
    
    # 1. Simulating Anonymous Visitor session
    anon_cookie = "anon_session_881023"
    print(f"Visitor lands on website. Cookie generated: {anon_cookie}")
    
    # 2. Visitor signs up and becomes identified
    cdp.identify(
        anonymous_id=anon_cookie, 
        user_id="usr_9901", 
        traits={"email": "captain@imsgoa.org", "name": "Vikram Singh"}
    )
    
    # 3. Associate user with the B2B organization
    cdp.group(
        user_id="usr_9901", 
        group_id="org_imsgoa", 
        traits={"name": "IMSGOA Maritime College", "employees": 85}
    )
    
    # 4. User completes a mock exam (Valid Event)
    cdp.track(
        user_id="usr_9901", 
        event_name="Exam Completed", 
        properties={"exam_id": "exam_meo_class_4", "score": 82.5, "pass_status": True}
    )
    
    # 5. User triggers invalid event (Missing property)
    cdp.track(
        user_id="usr_9901", 
        event_name="Exam Completed", 
        properties={"exam_id": "exam_meo_class_4"} # Missing score and pass_status
    )
    
    # 6. User triggers invalid event (Wrong type)
    cdp.track(
        user_id="usr_9901", 
        event_name="Subscription Upgraded", 
        properties={"plan_tier": "Enterprise", "seats_added": "twenty", "amount": 4500.00} # seats_added is string, expected int
    )
    
    print("\n" + "=" * 65)
