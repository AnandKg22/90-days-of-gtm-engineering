# Looker Parameterized SQL Query Engine Simulator
import sys
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Simulated database table: `vivaexams_gtm.fact_deals`
# Column close_date maps to partitions
db_fact_deals = [
    {"deal_id": 101, "company_name": "Tolani Maritime Institute", "amount_usd": 12000.00, "close_date": "2026-07-01"},
    {"deal_id": 102, "company_name": "IMSGOA Maritime College", "amount_usd": 4000.00, "close_date": "2026-07-05"},
    {"deal_id": 103, "company_name": "AMET University", "amount_usd": 25000.00, "close_date": "2026-07-10"},
    {"deal_id": 104, "company_name": "Global Shipping Corp", "amount_usd": 18000.00, "close_date": "2026-07-12"},
    {"deal_id": 105, "company_name": "Marine Academy Asia", "amount_usd": 3000.00, "close_date": "2026-07-13"}
]

class ParameterizedQueryEngine:
    def __init__(self, database: List[Dict[str, Any]]):
        self.db = database
        
    def run_client_side_filter(self, url_filter: str) -> Tuple[List[Dict[str, Any]], int]:
        # Client-side: Pull ALL rows from DB to Looker first, then filter in browser
        scanned_rows = len(self.db) # Scans the entire table
        filtered_results = [row for row in self.db if row.get("company_name") == url_filter or url_filter == "All"]
        return filtered_results, scanned_rows
        
    def run_parameterized_query(self, min_amount: float, start_date: str, end_date: str) -> Tuple[List[Dict[str, Any]], int]:
        # Server-side: Bind variables to database query planner to prune partitions
        scanned_rows = 0
        filtered_results = []
        
        for row in self.db:
            # Simulate date partition pruning: only scan rows within date range
            if start_date <= row["close_date"] <= end_date:
                scanned_rows += 1 # Increments row scan count
                if row["amount_usd"] >= min_amount:
                    filtered_results.append(row)
                    
        return filtered_results, scanned_rows

if __name__ == "__main__":
    engine = ParameterizedQueryEngine(db_fact_deals)
    
    print("=" * 65)
    print("             LOOKER PARAMETERIZED SQL QUERY SIMULATOR")
    print("=" * 65)
    print(f"Total Rows in DB Table: {len(db_fact_deals)}")
    print("-" * 65)
    
    # Run Case 1: Unoptimized Client-side filter (no parameters passed to DB)
    print("[RUNNING CASE 1] Client-Side Dropdown Filter (All rows pulled)...")
    results1, scanned1 = engine.run_client_side_filter("IMSGOA Maritime College")
    print(f"  Rows Returned: {len(results1)}")
    print(f"  Database Rows Scanned: {scanned1} (100% table scan overhead)")
    print("-" * 65)
    
    # Run Case 2: Optimized Parameterized query (prunes partition dates & values)
    # Parameters set: min_amount = 10000, date range = 2026-07-09 to 2026-07-13
    p_min_amount = 10000.00
    p_start_date = "2026-07-09"
    p_end_date = "2026-07-13"
    
    print(f"[RUNNING CASE 2] Parameterized SQL Query (Partition Pruning Active)...")
    print(f"  Passed Parameters: @ds_min_amount = ${p_min_amount:,.2f}")
    print(f"  Passed Date Range: @DS_START_DATE = '{p_start_date}' to @DS_END_DATE = '{p_end_date}'")
    
    results2, scanned2 = engine.run_parameterized_query(p_min_amount, p_start_date, p_end_date)
    print(f"  Rows Returned: {len(results2)}")
    for r in results2:
        print(f"    - {r['company_name']} | Date: {r['close_date']} | Amount: ${r['amount_usd']:,.2f}")
    print(f"  Database Rows Scanned: {scanned2} (Only matching date partitions scanned)")
    
    # Performance summary
    scan_reduction = ((scanned1 - scanned2) / scanned1) * 100.0
    print("\n" + "=" * 65)
    print("                 QUERY COST AUDITING DIGEST")
    print("=" * 65)
    print(f"Unoptimized Rows Scanned: {scanned1}")
    print(f"Optimized Rows Scanned:   {scanned2}")
    print(f"Database Scan Reduction:   {scan_reduction:.1f}% Cost Savings")
    print("-" * 65)
    if scan_reduction > 50.0:
        print("  [RECOMMENDATION]: Bind Looker parameters directly to custom SQL @ variables.")
        print("  This prunes partitions on disk and reduces BigQuery data scan costs.")
    else:
        print("  [RECOMMENDATION]: Parameter binds provide minor optimizations on small sets.")
    print("=" * 65)
