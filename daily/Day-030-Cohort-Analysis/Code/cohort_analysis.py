# GTM Cohort Retention Analyzer
import sys
from datetime import datetime
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Raw user activity logs: (user_id, event_name, event_date)
activity_logs = [
    # Cohort Week 1: Users signing up between 2026-07-01 and 2026-07-07
    {"user_id": "usr_01", "event_name": "Login", "event_date": "2026-07-01"},
    {"user_id": "usr_01", "event_name": "Exam Started", "event_date": "2026-07-08"}, # W1
    {"user_id": "usr_01", "event_name": "Exam Completed", "event_date": "2026-07-15"}, # W2
    {"user_id": "usr_01", "event_name": "Login", "event_date": "2026-07-22"}, # W3
    
    {"user_id": "usr_02", "event_name": "Login", "event_date": "2026-07-02"},
    {"user_id": "usr_02", "event_name": "Exam Started", "event_date": "2026-07-09"}, # W1
    
    {"user_id": "usr_03", "event_name": "Login", "event_date": "2026-07-03"},
    {"user_id": "usr_03", "event_name": "Login", "event_date": "2026-07-17"}, # W2
    
    # Cohort Week 2: Users signing up between 2026-07-08 and 2026-07-14
    {"user_id": "usr_04", "event_name": "Login", "event_date": "2026-07-08"},
    {"user_id": "usr_04", "event_name": "Exam Completed", "event_date": "2026-07-15"}, # W1
    {"user_id": "usr_04", "event_name": "Login", "event_date": "2026-07-22"}, # W2
    
    {"user_id": "usr_05", "event_name": "Login", "event_date": "2026-07-09"},
    {"user_id": "usr_05", "event_name": "Login", "event_date": "2026-07-10"}, # W0 (same week)
]

class CohortAnalyzer:
    def __init__(self, logs: List[Dict[str, Any]]):
        self.logs = logs
        
    def analyze_retention(self) -> Dict[str, Dict[int, int]]:
        # 1. Identify first activity (signup) date for each user
        user_signups: Dict[str, datetime] = {}
        for log in self.logs:
            uid = log["user_id"]
            date_val = datetime.strptime(log["event_date"], "%Y-%m-%d")
            if uid not in user_signups:
                user_signups[uid] = date_val
            else:
                if date_val < user_signups[uid]:
                    user_signups[uid] = date_val
                    
        # 2. Group cohorts by signup week (represent as date string of the cohort start)
        # We will define Cohort "Week 1" starting 2026-07-01 and Cohort "Week 2" starting 2026-07-08
        cohorts: Dict[str, List[str]] = {"2026-07-01": [], "2026-07-08": []}
        for uid, signup_date in user_signups.items():
            signup_str = signup_date.strftime("%Y-%m-%d")
            if signup_str <= "2026-07-07":
                cohorts["2026-07-01"].append(uid)
            else:
                cohorts["2026-07-08"].append(uid)
                
        # 3. Calculate weekly activity deltas
        # retention_grid: cohort -> {week_index -> set(active_users)}
        retention_grid: Dict[str, Dict[int, set]] = {
            "2026-07-01": {0: set(), 1: set(), 2: set(), 3: set()},
            "2026-07-08": {0: set(), 1: set(), 2: set(), 3: set()}
        }
        
        for log in self.logs:
            uid = log["user_id"]
            event_date = datetime.strptime(log["event_date"], "%Y-%m-%d")
            signup_date = user_signups[uid]
            
            # Calculate difference in weeks
            delta_days = (event_date - signup_date).days
            week_idx = delta_days // 7
            
            # Find which cohort this user belongs to
            for cohort_start, uids in cohorts.items():
                if uid in uids:
                    if week_idx in retention_grid[cohort_start]:
                        retention_grid[cohort_start][week_idx].add(uid)
                    break
                    
        # Convert user sets to counts
        final_grid = {}
        for cohort_start, weeks in retention_grid.items():
            final_grid[cohort_start] = {
                "size": len(cohorts[cohort_start]),
                "retention": {w: len(uids) for w, uids in weeks.items()}
            }
        return final_grid

    def calculate_stickiness(self, target_date: str) -> Tuple[int, int, float]:
        # DAU: Unique users active on target_date
        dau_users = set()
        for log in self.logs:
            if log["event_date"] == target_date:
                dau_users.add(log["user_id"])
        dau = len(dau_users)
        
        # MAU: Unique users active across the entire log
        mau_users = set(log["user_id"] for log in self.logs)
        mau = len(mau_users)
        
        # Stickiness = DAU / MAU
        stickiness = (dau / max(1, mau)) * 100.0
        return dau, mau, stickiness

if __name__ == "__main__":
    analyzer = CohortAnalyzer(activity_logs)
    
    print("=" * 65)
    print("             VIVAEXAMS COHORT RETENTION ENGINE")
    print("=" * 65)
    
    # 1. Calculate Retention grid
    grid = analyzer.analyze_retention()
    
    print("Cohort Weekly Retention Grid:")
    print("Cohort Week | Size | Week 0 | Week 1 | Week 2 | Week 3")
    print("-" * 65)
    for cohort, data in grid.items():
        size = data["size"]
        ret = data["retention"]
        
        # Convert counts to percentages
        w0 = (ret[0] / size) * 100
        w1 = (ret[1] / size) * 100
        w2 = (ret[2] / size) * 100
        w3 = (ret[3] / size) * 100
        
        print(f"{cohort} | {size:<4} | {w0:>5.1f}% | {w1:>5.1f}% | {w2:>5.1f}% | {w3:>5.1f}%")
    print("-" * 65)
    
    # 2. Calculate Stickiness metrics for a target peak date
    target = "2026-07-08"
    dau, mau, stickiness = analyzer.calculate_stickiness(target)
    
    print("\n" + "=" * 65)
    print("                 PRODUCT STICKINESS AUDIT")
    print("=" * 65)
    print(f"Target Date Analyzed:  {target}")
    print(f"Daily Active Users:    {dau} DAU")
    print(f"Monthly Active Users:  {mau} MAU")
    print(f"User Stickiness Ratio: {stickiness:.1f}%")
    print("-" * 65)
    if stickiness >= 20.0:
        print("  [BENCHMARK OK]: User Stickiness is above 20.0% target.")
        print("  Indicates healthy daily habits and product retention.")
    else:
        print("  [BENCHMARK WARNING]: Stickiness is below 20.0% target.")
        print("  Review onboarding sequences or trigger weekly retention emails.")
    print("=" * 65)
