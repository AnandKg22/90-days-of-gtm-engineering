# Google BigQuery Query & Cost Simulator
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock BigQuery dataset: `vivaexams_gtm.leads_partitioned`
# Table is partitioned by: `created_date`
mock_bigquery_table = [
    {
        "email": "dean@imsgoa.org",
        "company_name": "IMSGOA Maritime College",
        "created_date": "2026-07-10",
        "touchpoints": [
            {"source": "google", "medium": "cpc", "url": "/features"},
            {"source": "newsletter", "medium": "email", "url": "/pricing"}
        ]
    },
    {
        "email": "registrar@ametuniv.edu.in",
        "company_name": "AMET University",
        "created_date": "2026-07-12",
        "touchpoints": [
            {"source": "direct", "medium": "none", "url": "/home"},
            {"source": "direct", "medium": "none", "url": "/pricing"}
        ]
    },
    {
        "email": "sharma.r@tolani.edu",
        "company_name": "Tolani Maritime Institute",
        "created_date": "2026-07-13",
        "touchpoints": [
            {"source": "google", "medium": "cpc", "url": "/pricing"}
        ]
    }
]

class BigQuerySimulator:
    def __init__(self, table_data: List[Dict[str, Any]]):
        self.table = table_data
        
    def execute_unnest_query(self, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        # 1. Cost Optimizer Audit: check if query filters by partition key `created_date`
        print("\n" + "-" * 65)
        print("[BIGQUERY QUERY PLANNER AUDIT]")
        if "created_date" in filters:
            print("  [SUCCESS] Partition Pruning Active!")
            print(f"  Query filters by 'created_date' = '{filters['created_date']}'. Scanned only 1 partition.")
            print("  Estimated Query Cost: 0.02 Slot-Seconds (99% reduction).")
        else:
            print("  [WARNING] Full Table Scan Detected!")
            print("  No filter found on partitioned key 'created_date'. BigQuery scanned all partitions.")
            print("  Estimated Query Cost: 4.80 Slot-Seconds (Full scan billing penalty).")
        print("-" * 65)
        
        # 2. Execute Query Simulation
        flattened_rows = []
        for doc in self.table:
            # Check partition filter if present
            if "created_date" in filters and doc["created_date"] != filters["created_date"]:
                continue
                
            # Flatten repeated struct array (UNNEST)
            touchpoints = doc.get("touchpoints", [])
            for tp in touchpoints:
                row = {
                    "email": doc["email"],
                    "company_name": doc["company_name"],
                    "created_date": doc["created_date"],
                    "tp_source": tp["source"],
                    "tp_medium": tp["medium"],
                    "tp_url": tp["url"]
                }
                
                # Apply further filters
                matched = True
                for filter_key, filter_val in filters.items():
                    if filter_key == "created_date":
                        continue # Already checked
                    if row.get(filter_key) != filter_val:
                        matched = False
                        break
                        
                if matched:
                    flattened_rows.append(row)
                    
        return flattened_rows

if __name__ == "__main__":
    bq = BigQuerySimulator(mock_bigquery_table)
    
    print("=" * 65)
    print("             GOOGLE BIGQUERY QUERY SIMULATOR")
    print("=" * 65)
    print(f"Dataset:  vivaexams_gtm")
    print(f"Table:    leads_partitioned (Partition Key: created_date)")
    print(f"Rows:     {len(mock_bigquery_table)}")
    
    # Query 1: Unoptimized Query (No date partition filter)
    # Target: Find all users who visited '/pricing'
    print("\n[RUNNING QUERY 1] Find users who visited '/pricing' (Unoptimized)")
    query1_filters = {"tp_url": "/pricing"}
    results1 = bq.execute_unnest_query(query1_filters)
    print("Query Results:")
    for row in results1:
        print(f"  - {row['email']} ({row['company_name']}) | Source: {row['tp_source']} | URL: {row['tp_url']}")
        
    # Query 2: Optimized Query (Date partition filter active)
    # Target: Find users who signed up on '2026-07-13' and visited '/pricing'
    print("\n[RUNNING QUERY 2] Find users who signed up on 2026-07-13 and visited '/pricing' (Optimized)")
    query2_filters = {"created_date": "2026-07-13", "tp_url": "/pricing"}
    results2 = bq.execute_unnest_query(query2_filters)
    print("Query Results:")
    for row in results2:
        print(f"  - {row['email']} ({row['company_name']}) | Date: {row['created_date']} | URL: {row['tp_url']}")
        
    print("\n" + "=" * 65)
