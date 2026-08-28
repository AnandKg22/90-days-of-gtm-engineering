# GTM Funnel Conversion & Velocity Analyzer
import sys
from datetime import datetime
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Raw CRM Opportunity stage history log
crm_stage_logs = [
    # Deal 1: Progresses all the way to Won
    {"deal_id": 101, "stage": "Lead", "date": "2026-06-01"},
    {"deal_id": 101, "stage": "MQL", "date": "2026-06-03"}, # 2 days
    {"deal_id": 101, "stage": "SQL", "date": "2026-06-07"}, # 4 days
    {"deal_id": 101, "stage": "Opportunity", "date": "2026-06-12"}, # 5 days
    {"deal_id": 101, "stage": "Won", "date": "2026-06-30"}, # 18 days
    
    # Deal 2: Drops off at SQL
    {"deal_id": 102, "stage": "Lead", "date": "2026-06-02"},
    {"deal_id": 102, "stage": "MQL", "date": "2026-06-06"}, # 4 days
    {"deal_id": 102, "stage": "SQL", "date": "2026-06-15"}, # 9 days
    
    # Deal 3: Progresses all the way to Won
    {"deal_id": 103, "stage": "Lead", "date": "2026-06-05"},
    {"deal_id": 103, "stage": "MQL", "date": "2026-06-06"}, # 1 day
    {"deal_id": 103, "stage": "SQL", "date": "2026-06-10"}, # 4 days
    {"deal_id": 103, "stage": "Opportunity", "date": "2026-06-15"}, # 5 days
    {"deal_id": 103, "stage": "Won", "date": "2026-06-25"}, # 10 days
    
    # Deal 4: Drops off at MQL
    {"deal_id": 104, "stage": "Lead", "date": "2026-06-10"},
    {"deal_id": 104, "stage": "MQL", "date": "2026-06-12"}, # 2 days
    
    # Deal 5: Drops off immediately at Lead
    {"deal_id": 105, "stage": "Lead", "date": "2026-06-15"}
]

class FunnelMetricsAnalyzer:
    def __init__(self, logs: List[Dict[str, Any]]):
        self.logs = logs
        
    def analyze_funnel(self) -> Tuple[Dict[str, int], Dict[str, float], Dict[str, float]]:
        # 1. Reconstruct deal transition timelines
        deal_stages: Dict[int, List[Tuple[str, datetime]]] = {}
        for log in self.logs:
            did = log["deal_id"]
            stage = log["stage"]
            dt = datetime.strptime(log["date"], "%Y-%m-%d")
            if did not in deal_stages:
                deal_stages[did] = []
            deal_stages[did].append((stage, dt))
            
        # Sort each deal's stage history by date
        for did in deal_stages:
            deal_stages[did].sort(key=lambda x: x[1])
            
        # 2. Count unique deals reaching each stage
        stage_counts = {"Lead": 0, "MQL": 0, "SQL": 0, "Opportunity": 0, "Won": 0}
        
        # 3. Track durations for velocity calculations
        # stage_durations: stage_name -> List of days spent
        stage_durations = {"Lead": [], "MQL": [], "SQL": [], "Opportunity": []}
        
        for did, transitions in deal_stages.items():
            stages_visited = [t[0] for t in transitions]
            
            # Increment counts for all visited stages
            for st in stages_visited:
                if st in stage_counts:
                    stage_counts[st] += 1
                    
            # Calculate elapsed time spent at each stage before moving on
            for i in range(len(transitions) - 1):
                curr_stage, curr_date = transitions[i]
                next_stage, next_date = transitions[i+1]
                
                duration_days = (next_date - curr_date).days
                if curr_stage in stage_durations:
                    stage_durations[curr_stage].append(duration_days)
                    
        # 4. Calculate Conversion Rates
        conversion_rates = {}
        lead_count = max(1, stage_counts["Lead"])
        
        conversion_rates["Lead-to-MQL"] = (stage_counts["MQL"] / lead_count) * 100
        conversion_rates["MQL-to-SQL"] = (stage_counts["SQL"] / max(1, stage_counts["MQL"])) * 100
        conversion_rates["SQL-to-Opportunity"] = (stage_counts["Opportunity"] / max(1, stage_counts["SQL"])) * 100
        conversion_rates["Opportunity-to-Won"] = (stage_counts["Won"] / max(1, stage_counts["Opportunity"])) * 100
        conversion_rates["Overall-Conversion"] = (stage_counts["Won"] / lead_count) * 100
        
        # 5. Calculate Average Velocity
        avg_velocity = {}
        for st, durations in stage_durations.items():
            avg_velocity[st] = sum(durations) / len(durations) if durations else 0.0
            
        return stage_counts, conversion_rates, avg_velocity

if __name__ == "__main__":
    analyzer = FunnelMetricsAnalyzer(crm_stage_logs)
    counts, rates, velocity = analyzer.analyze_funnel()
    
    print("=" * 65)
    print("             VIVAEXAMS SALES FUNNEL & VELOCITY ENGINE")
    print("=" * 65)
    
    # 1. Print Stage Counts
    print("Stage Volume Counts:")
    for st, count in counts.items():
        print(f"  - {st:<12}: {count} Accounts")
    print("-" * 65)
    
    # 2. Print Step Conversion Rates
    print("Stage-to-Stage Conversion Rates:")
    print(f"  - Lead to MQL:      {rates['Lead-to-MQL']:.1f}%")
    print(f"  - MQL to SQL:       {rates['MQL-to-SQL']:.1f}%")
    print(f"  - SQL to Opp:       {rates['SQL-to-Opportunity']:.1f}%")
    print(f"  - Opp to Closed Won: {rates['Opportunity-to-Won']:.1f}%")
    print(f"  (*) Overall Funnel Conversion: {rates['Overall-Conversion']:.1f}%")
    print("-" * 65)
    
    # 3. Print Stage Velocity (Average Days spent)
    print("Average Funnel Velocity (Days in Stage):")
    for st, days in velocity.items():
        print(f"  - {st:<12}: {days:.1f} Days")
        
    total_cycle_time = sum(velocity.values())
    print(f"  (*) Total Funnel Cycle Time: {total_cycle_time:.1f} Days")
    print("-" * 65)
    
    # Audit Alerts
    print("FUNNEL OPTIMIZATION RECOMMENDATIONS:")
    if rates["Lead-to-MQL"] < 40.0:
        print("  [WARNING] Low Lead-to-MQL conversion. Improve ad targeting or landing page copy.")
    if velocity["Opportunity"] > 15.0:
        print("  [WARNING] Deals are stalling in negotiation. Simplify procurement and sign loops.")
    if rates["Overall-Conversion"] >= 1.0:
        print("  [SUCCESS] Funnel conversion is healthy.")
    print("=" * 65)
