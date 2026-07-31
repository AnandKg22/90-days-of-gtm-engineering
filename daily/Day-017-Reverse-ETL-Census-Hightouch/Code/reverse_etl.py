# Reverse ETL Sync Engine
import json
import time
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. Mock Data Warehouse View (company_gtm_metrics)
warehouse_db = [
    {
        "company_domain": "tolani.edu",
        "total_exams_completed": 850,
        "average_pass_rate": 78.50,
        "health_status": "Good",
        "updated_at": 1783948800  # Sync target time
    },
    {
        "company_domain": "imsgoa.org",
        "total_exams_completed": 120,
        "average_pass_rate": 62.40,
        "health_status": "At Risk",
        "updated_at": 1783948800  # Sync target time
    },
    {
        "company_domain": "ametuniv.edu.in",
        "total_exams_completed": 2100,
        "average_pass_rate": 84.10,
        "health_status": "Good",
        "updated_at": 1783900000  # Older timestamp (already synced)
    }
]

class ReverseETLEngine:
    def __init__(self, schema_mapping: Dict[str, str], last_sync_time: int):
        self.schema_mapping = schema_mapping
        self.last_sync_time = last_sync_time
        
    def get_incremental_records(self, warehouse_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Filter for records modified AFTER the last sync timestamp (Incremental Sync)
        changed_records = []
        for record in warehouse_data:
            if record["updated_at"] > self.last_sync_time:
                changed_records.append(record)
        return changed_records
        
    def transform_records(self, source_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        transformed = []
        for record in source_records:
            mapped_payload = {}
            for source_col, target_field in self.schema_mapping.items():
                if source_col in record:
                    mapped_payload[target_field] = record[source_col]
            transformed.append(mapped_payload)
        return transformed

class HubSpotClientMock:
    @staticmethod
    def batch_upsert_companies(payloads: List[Dict[str, Any]]) -> Dict[str, Any]:
        time.sleep(0.1) # Simulate API latency
        return {
            "status": "success",
            "synced_count": len(payloads),
            "synced_records": payloads,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    # Define CRM sync schema mapping
    crm_mapping = {
        "company_domain": "domain",
        "total_exams_completed": "cadet_exams_completed",
        "average_pass_rate": "exam_pass_rate_percent",
        "health_status": "customer_health_status"
    }
    
    # Last sync happened at 1783920000.
    # Records updated after this timestamp need to be synced (Incremental).
    sync_watermark = 1783920000 
    
    print("=" * 65)
    print("           INITIALIZING REVERSE ETL PIPELINE RUN")
    print("=" * 65)
    print(f"Sync Watermark Timestamp:  {sync_watermark}")
    print(f"Total Warehouse Records:   {len(warehouse_db)}")
    print("-" * 65)
    
    engine = ReverseETLEngine(crm_mapping, sync_watermark)
    
    # 1. Fetch changed records only
    print("[*] Extracting incremental records since last sync...")
    incremental_data = engine.get_incremental_records(warehouse_db)
    print(f"  Incremental Rows Found:  {len(incremental_data)}")
    for r in incremental_data:
        print(f"    - Domain: {r['company_domain']} | Updated: {r['updated_at']}")
    print("-" * 65)
    
    if not incremental_data:
        print("[-] No updates detected. Sync skipped.")
        sys.exit(0)
        
    # 2. Transform columns to CRM properties
    print("[*] Applying schema mapping rules to transform payloads...")
    mapped_payloads = engine.transform_records(incremental_data)
    print("Mapped payloads to sync:")
    print(json.dumps(mapped_payloads, indent=4))
    print("-" * 65)
    
    # 3. Push to HubSpot REST API
    print("[*] Uploading batch payloads to HubSpot CRM endpoint...")
    hubspot = HubSpotClientMock()
    response = hubspot.batch_upsert_companies(mapped_payloads)
    
    print("\nCRM Sync API Response:")
    print(json.dumps(response, indent=4))
    print("=" * 65)
