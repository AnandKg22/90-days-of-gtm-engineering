# Market Segmentation & TAM/SAM/SOM Engine
from typing import List, Dict, Any

class AcademyAccount:
    def __init__(self, name: str, country: str, region: str, students_per_year: int,
                 is_dgs_approved: bool, tech_stack: List[str]):
        self.name = name
        self.country = country
        self.region = region # e.g. West, South, North, East
        self.students_per_year = students_per_year
        self.is_dgs_approved = is_dgs_approved
        self.tech_stack = tech_stack

# Mock raw lead list representing international maritime institutes
prospects_db = [
    AcademyAccount("Tolani Maritime Institute", "IN", "West", 1500, True, ["Moodle", "Stripe"]),
    AcademyAccount("Singapore Maritime Academy", "SG", "Central", 2000, False, ["Blackboard", "Stripe"]),
    AcademyAccount("AMET University", "IN", "South", 3000, True, ["Canvas", "Custom"]),
    AcademyAccount("IMSGOA Maritime College", "IN", "West", 200, True, ["Moodle", "Stripe"]),
    AcademyAccount("Marine Safety Corp Dubai", "AE", "Central", 600, False, ["Custom"]),
    AcademyAccount("Tamil Nadu Maritime Academy", "IN", "South", 400, True, ["Moodle"]),
    AcademyAccount("Lal Bahadur Shastri College", "IN", "West", 1200, True, ["Moodle", "Stripe"]),
    AcademyAccount("Kolkata Marine College", "IN", "East", 800, True, ["Canvas"]),
    AcademyAccount("US Merchant Marine Academy", "US", "East", 1000, False, ["Blackboard"]),
    AcademyAccount("Delhi Maritime Academy", "IN", "North", 300, True, ["Custom"])
]

class MarketSegmentationEngine:
    def __init__(self, accounts: List[AcademyAccount]):
        self.accounts = accounts
        
    def calculate_tam_sam_som(self) -> Dict[str, Any]:
        tam_accounts = []
        sam_accounts = []
        som_accounts = []
        
        # ACV assumptions
        acv_base = 8000.00
        
        for acc in self.accounts:
            # 1. TAM: All prospects in database
            tam_accounts.append(acc)
            
            # 2. SAM: DGS-Approved Indian Academies
            if acc.country == "IN" and acc.is_dgs_approved:
                sam_accounts.append(acc)
                
                # 3. SOM: In SAM + High Tech Fit (uses Moodle/Blackboard) + South/West regions
                has_tech_fit = any(t in acc.tech_stack for t in ["Moodle", "Blackboard"])
                is_target_region = acc.region in ["West", "South"]
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
    print("         VIVAEXAMS MARKET SEGMENTATION REPORT")
    print("=" * 60)
    
    for tier in ["tam", "sam", "som"]:
        name = tier.upper()
        data = results[tier]
        print(f"[{name}]")
        print(f"  Account Count:     {data['count']}")
        print(f"  Annual Value Potential: ${data['value']:,.2f}")
        print("  Accounts Included:")
        for name_item in data["names"]:
            print(f"    - {name_item}")
        print("-" * 60)
    print("=" * 60)
