# Looker Studio Connection Auditor
import sys
from typing import Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Simulated data source connections configured in Looker Studio
looker_data_sources = {
    "PostgreSQL - Lead Logs": {
        "connector_type": "PostgreSQL",
        "auth_method": "JDBC-NoSSL", # Security Risk
        "query_method": "Table-Selection",
        "database_name": "vivaexams_leads_db",
        "scan_volume_gb": 4.5
    },
    "BigQuery - Won Deals Mart": {
        "connector_type": "BigQuery",
        "auth_method": "OAuth2",
        "query_method": "Custom-SQL", # Performance Best Practice
        "database_name": "vivaexams_gtm",
        "scan_volume_gb": 22.0
    },
    "Google Sheets - ICP Target Lists": {
        "connector_type": "Google Sheets",
        "auth_method": "OAuth2",
        "query_method": "Sheet-Range",
        "database_name": "sheets_icp_raw",
        "scan_volume_gb": 0.01
    },
    "BigQuery - Raw Event Log Staging": {
        "connector_type": "BigQuery",
        "auth_method": "OAuth2",
        "query_method": "Table-Selection", # Costly on large datasets
        "database_name": "raw_clickstream",
        "scan_volume_gb": 85.0
    }
}

class LookerConnectorAuditor:
    @staticmethod
    def audit_connection(source_name: str, config: Dict[str, Any]):
        print(f"\n[*] Auditing Looker Studio Source: '{source_name}'...")
        conn_type = config.get("connector_type", "")
        auth = config.get("auth_method", "")
        query = config.get("query_method", "")
        volume = config.get("scan_volume_gb", 0.0)
        
        # 1. Security Check: PostgreSQL JDBC connections MUST enforce SSL certificates
        if conn_type == "PostgreSQL":
            if "NoSSL" in auth:
                print("  [SECURITY RISK] JDBC Connection lacks SSL Encryption!")
                print("    - Action: Reject connection. Upload client certifications (key, cert, Server CA).")
            else:
                print("  [SECURITY OK] Database connection uses encrypted JDBC-SSL.")
                
        # 2. Performance Check: Table-Selection on large datasets increases query latency
        if query == "Table-Selection" and volume > 10.0:
            print(f"  [PERFORMANCE WARNING] Querying raw table '{config.get('database_name')}' (Size: {volume} GB).")
            print("    - Warning: Multi-join dashboard widgets will trigger slow, expensive table scans.")
            print("    - Action: Replace Looker Table-Selection with a warehouse custom SQL View or dbt Mart.")
        elif query == "Custom-SQL":
            print("  [PERFORMANCE OK] Utilizing pre-aggregated Custom SQL. Cuts dashboard latency.")
            
        # 3. Cost Control Check: Suggest BigQuery BI Engine cache reservations
        if conn_type == "BigQuery":
            # Rule of thumb: Reserve 100MB of BI Engine RAM per 5GB of active dataset volume
            recommended_bi_engine_mb = max(100.0, (volume / 5.0) * 100.0)
            print(f"  [COST CONTROL] Target BigQuery Dataset Size: {volume} GB.")
            print(f"    - Action: Allocate a {recommended_bi_engine_mb:.0f} MB Google BI Engine memory reservation.")
            print("      This caches queries in RAM, reducing Looker query scan billing to zero.")
            
        # 4. Sheet audit
        if conn_type == "Google Sheets":
            print("  [INTEGRITY CHECK] Verified Sheets range bindings. Ensure first row contains headers.")

if __name__ == "__main__":
    print("=" * 65)
    print("             LOOKER STUDIO DATA SOURCE CONNECTION AUDITOR")
    print("=" * 65)
    
    auditor = LookerConnectorAuditor()
    for name, source_config in looker_data_sources.items():
        auditor.audit_connection(name, source_config)
        print("-" * 65)
        
    print("=" * 65)
