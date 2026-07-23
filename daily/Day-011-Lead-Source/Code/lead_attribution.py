# Lead Source Marketing Attribution Engine
from typing import List, Dict, Any

class Touchpoint:
    def __init__(self, timestamp: str, source: str, medium: str, campaign: str):
        self.timestamp = timestamp
        self.source = source
        self.medium = medium
        self.campaign = campaign

class CustomerJourney:
    def __init__(self, customer_id: str, deal_value: float):
        self.customer_id = customer_id
        self.deal_value = float(deal_value)
        self.touchpoints: List[Touchpoint] = []
        
    def add_touchpoint(self, timestamp: str, source: str, medium: str, campaign: str):
        self.touchpoints.append(Touchpoint(timestamp, source, medium, campaign))

class AttributionEngine:
    def run_first_touch(self, journey: CustomerJourney) -> Dict[str, Any]:
        if not journey.touchpoints:
            return {"source": "direct", "medium": "none", "campaign": "none"}
            
        # First chronological touchpoint
        first = journey.touchpoints[0]
        return {
            "source": first.source,
            "medium": first.medium,
            "campaign": first.campaign,
            "revenue_credit": journey.deal_value
        }
        
    def run_last_touch(self, journey: CustomerJourney) -> Dict[str, Any]:
        if not journey.touchpoints:
            return {"source": "direct", "medium": "none", "campaign": "none"}
            
        # Last chronological touchpoint before purchase
        last = journey.touchpoints[-1]
        return {
            "source": last.source,
            "medium": last.medium,
            "campaign": last.campaign,
            "revenue_credit": journey.deal_value
        }

if __name__ == "__main__":
    print("=" * 65)
    print("           INITIALIZING MARKETING ATTRIBUTION ENGINE")
    print("=" * 65)
    
    # 1. Create a customer journey (Tolani Maritime Academy)
    # They found us via a Google search ad, later clicked an email newsletter, then converted.
    tolani_journey = CustomerJourney("c_tolani", 8000.00)
    tolani_journey.add_touchpoint("2026-07-01 10:00:00", "google", "cpc", "maritime_exam_prep")
    tolani_journey.add_touchpoint("2026-07-05 14:30:00", "newsletter", "email", "july_institutions")
    tolani_journey.add_touchpoint("2026-07-10 11:00:00", "organic", "search", "seo_ranking")
    
    print(f"Customer Journey: {tolani_journey.customer_id}")
    print(f"Contract Value:   ${tolani_journey.deal_value:,.2f} USD")
    print("Touchpoint Timeline:")
    for idx, tp in enumerate(tolani_journey.touchpoints, 1):
        print(f"  [{idx}] {tp.timestamp} | Source: {tp.source:<12} | Med: {tp.medium:<8} | Camp: {tp.campaign}")
    print("-" * 65)
    
    # 2. Run Attribution Models
    engine = AttributionEngine()
    first_touch = engine.run_first_touch(tolani_journey)
    last_touch = engine.run_last_touch(tolani_journey)
    
    print("[FIRST-TOUCH ATTRIBUTION]")
    print(f"  Credited Channel: {first_touch['source'].upper()} / {first_touch['medium'].upper()}")
    print(f"  Campaign:         {first_touch['campaign']}")
    print(f"  Revenue Credited: ${first_touch['revenue_credit']:,.2f} USD")
    print("-" * 65)
    
    print("[LAST-TOUCH ATTRIBUTION]")
    print(f"  Credited Channel: {last_touch['source'].upper()} / {last_touch['medium'].upper()}")
    print(f"  Campaign:         {last_touch['campaign']}")
    print(f"  Revenue Credited: ${last_touch['revenue_credit']:,.2f} USD")
    print("=" * 65)
