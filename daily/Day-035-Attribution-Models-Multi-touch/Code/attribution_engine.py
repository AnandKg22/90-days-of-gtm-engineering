# GTM Multi-Touch Attribution Engine
import sys
from datetime import datetime
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Click logs tracking user marketing touches
campaign_clicks = [
    # User 1 Touchpoints (Google -> Email -> LinkedIn -> Conversion)
    {"user_id": "usr_01", "channel": "google", "date": "2026-07-01"},
    {"user_id": "usr_01", "channel": "email", "date": "2026-07-05"},
    {"user_id": "usr_01", "channel": "linkedin", "date": "2026-07-10"},
    
    # User 2 Touchpoints (LinkedIn -> Google -> Conversion)
    {"user_id": "usr_02", "channel": "linkedin", "date": "2026-07-02"},
    {"user_id": "usr_02", "channel": "google", "date": "2026-07-08"},
    
    # User 3 Touchpoints (Google -> Conversion)
    {"user_id": "usr_03", "channel": "google", "date": "2026-07-05"},
]

# Converted Won Deals
won_conversions = [
    {"user_id": "usr_01", "revenue": 10000.00},
    {"user_id": "usr_02", "revenue": 5000.00},
    {"user_id": "usr_03", "revenue": 2000.00}
]

class MultiTouchAttributionEngine:
    def __init__(self, clicks: List[Dict[str, Any]], conversions: List[Dict[str, Any]]):
        self.clicks = clicks
        self.conversions = conversions
        
    def _get_user_touchpaths(self) -> Dict[str, List[str]]:
        # Group user clicks, sort chronologically, return channel list
        paths = {}
        grouped = {}
        for c in self.clicks:
            uid = c["user_id"]
            dt = datetime.strptime(c["date"], "%Y-%m-%d")
            if uid not in grouped:
                grouped[uid] = []
            grouped[uid].append((c["channel"], dt))
            
        for uid in grouped:
            grouped[uid].sort(key=lambda x: x[1])
            paths[uid] = [item[0] for item in grouped[uid]]
        return paths

    def calculate_attribution(self) -> Dict[str, Dict[str, float]]:
        paths = self._get_user_touchpaths()
        
        # Initialize revenue trackers
        channels = ["google", "linkedin", "email"]
        models = ["first_touch", "last_touch", "linear", "u_shaped"]
        
        results = {m: {ch: 0.0 for ch in channels} for m in models}
        
        for conv in self.conversions:
            uid = conv["user_id"]
            rev = conv["revenue"]
            
            # Skip if user has no recorded clicks
            if uid not in paths or not paths[uid]:
                continue
                
            path = paths[uid]
            length = len(path)
            
            # 1. First Touch Attribution
            results["first_touch"][path[0]] += rev
            
            # 2. Last Touch Attribution
            results["last_touch"][path[-1]] += rev
            
            # 3. Linear Attribution
            split_rev = rev / length
            for ch in path:
                results["linear"][ch] += split_rev
                
            # 4. U-Shaped Attribution (40/20/40)
            if length == 1:
                results["u_shaped"][path[0]] += rev
            elif length == 2:
                results["u_shaped"][path[0]] += rev * 0.50
                results["u_shaped"][path[-1]] += rev * 0.50
            else:
                results["u_shaped"][path[0]] += rev * 0.40
                results["u_shaped"][path[-1]] += rev * 0.40
                middle_weight = 0.20 / (length - 2)
                for i in range(1, length - 1):
                    results["u_shaped"][path[i]] += rev * middle_weight
                    
        return results

if __name__ == "__main__":
    engine = MultiTouchAttributionEngine(campaign_clicks, won_conversions)
    attrib_report = engine.calculate_attribution()
    
    print("=" * 65)
    print("             VIVAEXAMS MULTI-TOUCH ATTRIBUTION ENGINE")
    print("=" * 65)
    
    print(f"{'Channel':<10} | {'First Touch':<11} | {'Last Touch':<11} | {'Linear':<11} | {'U-Shaped (40/20/40)':<18}")
    print("-" * 65)
    
    channels = ["google", "linkedin", "email"]
    for ch in channels:
        print(f"{ch:<10} | "
              f"${attrib_report['first_touch'][ch]:<10,.2f} | "
              f"${attrib_report['last_touch'][ch]:<10,.2f} | "
              f"${attrib_report['linear'][ch]:<10,.2f} | "
              f"${attrib_report['u_shaped'][ch]:<10,.2f}")
    print("-" * 65)
    
    # Audit Recommendation
    print("ATTRIBUTION COMPARISON INSIGHT:")
    google_last = attrib_report["last_touch"]["google"]
    google_ushaped = attrib_report["u_shaped"]["google"]
    
    print(f"  * Google Ads revenue credit under Last Touch:  ${google_last:,.2f}")
    print(f"  * Google Ads revenue credit under U-Shaped:    ${google_ushaped:,.2f}")
    diff = abs(google_last - google_ushaped)
    print(f"  * Revenue attribution variance:                ${diff:,.2f}")
    print("-" * 65)
    print("  [RECOMMENDATION]: Last-Touch models skew budgets toward closing channels.")
    print("  Deploy a U-Shaped (Position-Based) model in Looker to credit early discoverability.")
    print("=" * 65)
