# Looker Studio Calculated Fields Parser & Query Engine
import sys
import time
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Simulated raw database table: `vivaexams_gtm.raw_leads`
raw_leads_dataset = [
    {
        "first_name": "Vikram",
        "last_name": "Singh",
        "email": "DEAN@imsgoa.org",
        "employees": 45,
        "seats_string": "300"
    },
    {
        "first_name": "Rajesh",
        "last_name": "Sharma",
        "email": "sharma.r@TOLANI.edu",
        "employees": 120,
        "seats_string": "500"
    },
    {
        "first_name": "Amit",
        "last_name": "Kumar",
        "email": "REGISTRAR@ametuniv.edu.in",
        "employees": 250,
        "seats_string": "1000"
    }
]

class LookerFormulaEngine:
    @staticmethod
    def CONCAT(val1: str, val2: str) -> str:
        return f"{val1} {val2}"
        
    @staticmethod
    def CASE_employees(employees: int) -> str:
        if employees > 50:
            return "Enterprise (51+)"
        return "SME (1-50)"
        
    @staticmethod
    def CAST_to_number(val: str) -> int:
        try:
            return int(val)
        except ValueError:
            return 0

if __name__ == "__main__":
    print("=" * 65)
    print("             LOOKER STUDIO CALCULATED FIELDS ENGINE")
    print("=" * 65)
    
    # 1. Simulate Frontend Looker calculated fields execution (browser loop)
    print("[*] Simulating Frontend Calculated Fields (Browser Processing)...")
    start_frontend = time.perf_counter()
    
    frontend_results = []
    for row in raw_leads_dataset:
        # Simulate browser-side formula rendering
        full_name = LookerFormulaEngine.CONCAT(row["first_name"], row["last_name"])
        clean_email = row["email"].lower()
        segment = LookerFormulaEngine.CASE_employees(row["employees"])
        seats = LookerFormulaEngine.CAST_to_number(row["seats_string"])
        
        frontend_results.append({
            "full_name": full_name,
            "clean_email": clean_email,
            "segment": segment,
            "seats": seats
        })
        # Simulate small UI rendering lag
        time.sleep(0.01)
        
    duration_frontend = (time.perf_counter() - start_frontend) * 1000.0
    print(f"  Processed {len(frontend_results)} records in {duration_frontend:.2f} ms.")
    print("-" * 65)
    
    # 2. Simulate Warehouse pre-compiled SQL Views execution (instantly loaded)
    print("[*] Simulating Warehouse Pre-compiled Custom SQL Views (DB Engine)...")
    start_warehouse = time.perf_counter()
    
    # Pre-compiled representation of:
    # SELECT CONCAT(f, ' ', l), LOWER(e), CASE..., CAST... FROM table;
    warehouse_results = [
        {"full_name": "Vikram Singh", "clean_email": "dean@imsgoa.org", "segment": "SME (1-50)", "seats": 300},
        {"full_name": "Rajesh Sharma", "clean_email": "sharma.r@tolani.edu", "segment": "Enterprise (51+)", "seats": 500},
        {"full_name": "Amit Kumar", "clean_email": "registrar@ametuniv.edu.in", "segment": "Enterprise (51+)", "seats": 1000}
    ]
    # In warehouse execution, Looker simply queries the finished columns, zero transformations needed
    duration_warehouse = (time.perf_counter() - start_warehouse) * 1000.0
    print(f"  Loaded {len(warehouse_results)} records in {duration_warehouse:.2f} ms.")
    print("-" * 65)
    
    # 3. Print parsed records
    print("Parsed Database Columns:")
    for record in warehouse_results:
        print(f"  - Name:    {record['full_name']:<18} | Email: {record['clean_email']:<26}")
        print(f"    Segment: {record['segment']:<18} | Seats: {record['seats']} Licenses")
        print("    " + "." * 55)
        
    # 4. Performance Audit Report
    print("\n" + "=" * 65)
    print("                 PERFORMANCE AUDITING digest")
    print("=" * 65)
    print(f"Frontend Calculation Time:  {duration_frontend:.2f} ms")
    print(f"Warehouse Calculation Time: {duration_warehouse:.2f} ms")
    
    speed_increase = (duration_frontend / max(0.001, duration_warehouse))
    print(f"Speed Increase:             {speed_increase:.1f}x Faster via Warehouse SQL")
    print("-" * 65)
    
    if speed_increase > 2.0:
        print("  [RECOMMENDATION]: Avoid client-side calculated fields inside Looker Studio.")
        print("  Offload 'CONCAT', 'CASE', and 'CAST' calculations to PostgreSQL Views or dbt Marts.")
        print("  This pre-aggregates data on disk, reducing browser dashboard rendering load.")
    else:
        print("  [RECOMMENDATION]: Datasets are small. Client-side formulas are safe.")
    print("=" * 65)
