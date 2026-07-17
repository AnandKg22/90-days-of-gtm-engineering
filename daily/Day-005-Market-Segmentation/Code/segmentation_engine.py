# Market Segmentation & TAM/SAM/SOM Engine for SmartStudy Classrooms
from typing import List, Dict, Any

class SchoolAccount:
    def __init__(self, name: str, country: str, region: str, student_count: int,
                 is_board_affiliated: bool, tech_stack: List[str]):
        self.name = name
        self.country = country
        self.region = region # e.g., North, South, East, West, Central
        self.student_count = student_count
        self.is_board_affiliated = is_board_affiliated
        self.tech_stack = tech_stack

# Mock raw lead list representing schools and coaching centers
prospects_db = [
    SchoolAccount("Allen Career Institute (Kota)", "IN", "North", 15000, True, ["Moodle", "Stripe"]),
    SchoolAccount("Singapore International School", "SG", "Central", 1200, False, ["Blackboard", "Stripe"]),
    SchoolAccount("FIITJEE Delhi", "IN", "North", 8000, True, ["Canvas", "Custom"]),
    SchoolAccount("Vibrant Academy Kota", "IN", "North", 3000, True, ["Moodle", "Stripe"]),
    SchoolAccount("Dubai Private School", "AE", "Central", 2000, False, ["Custom"]),
    SchoolAccount("Chaitanya Academy Hyderabad", "IN", "South", 12000, True, ["Moodle"]),
    SchoolAccount("Base Educational Services Bengaluru", "IN", "South", 4000, True, ["Moodle", "Stripe"]),
    SchoolAccount("Kolkata Science Academy", "IN", "East", 800, True, ["Canvas"]),
    SchoolAccount("Thomas Jefferson High School (US)", "US", "East", 1500, False, ["Blackboard"]),
    SchoolAccount("Delhi Public School R.K. Puram", "IN", "North", 3500, True, ["Custom"])
]

class MarketSegmentationEngine:
    def __init__(self, accounts: List[SchoolAccount]):
        self.accounts = accounts
        
    def calculate_tam_sam_som(self) -> Dict[str, Any]:
        tam_accounts = []
        sam_accounts = []
        som_accounts = []
        
        # ACV assumptions
        acv_base = 1200.00
        
        for acc in self.accounts:
            # 1. TAM: All prospects in database
            tam_accounts.append(acc)
            
            # 2. SAM: Board-Affiliated Indian Schools/Coaching Centers
            if acc.country == "IN" and acc.is_board_affiliated:
                sam_accounts.append(acc)
                
                # 3. SOM: In SAM + High Tech Fit (uses Moodle/Canvas) + North/South active regions
                has_tech_fit = any(t in acc.tech_stack for t in ["Moodle", "Canvas"])
                is_target_region = acc.region in ["North", "South"]
                if has_tech_fit and is_target_region:
                    som_accounts.append(acc)
                    
        # Valuations
        tam_val = len(tam_accounts) * acv_base
        sam_val = len(sam_accounts) * acv_base
        som_val = len(som_accounts) * acv_base
        
        return {
            "tam": {"count": len(tam_accounts), "value": tam_val, "names": [a.name for a in tam_accounts]},
            "sam": {"count": len(sam_accounts), "value": sam_val, "names": [a.name for a in sam_accounts]},
            "som": {"count": len(som_accounts), "value": som_val, "names": [a.name for a in som_accounts]}
        }

if __name__ == "__main__":
    engine = MarketSegmentationEngine(prospects_db)
    results = engine.calculate_tam_sam_som()
    
    print("=" * 60)
    print("       SMARTSTUDY CLASSROOMS MARKET SEGMENTATION REPORT")
    print("=" * 60)
    
    for tier in ["tam", "sam", "som"]:
        name = tier.upper()
        data = results[tier]
        print(f"[{name}]")
        print(f"  Account Count:          {data['count']}")
        print(f"  Annual Value Potential: ${data['value']:,.2f}")
        print("  Accounts Included:")
        for name_item in data["names"]:
            print(f"    - {name_item}")
        print("-" * 60)
    print("=" * 60)
