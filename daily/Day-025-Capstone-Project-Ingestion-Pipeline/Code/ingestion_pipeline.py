# Capstone Ingestion Pipeline Orchestrator
import json
import sqlite3
import sys
import time
from typing import Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

INGEST_TOKEN = "vivaexams_secure_token_99"

class GTMOrchestrator:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self._init_db()
        self.rate_limit_attempts = 0 # Track rate limit counts for simulation
        
    def _init_db(self):
        cursor = self.conn.cursor()
        
        # 1. Dimension Table
        cursor.execute("""
        CREATE TABLE dim_companies (
            company_key INTEGER PRIMARY KEY,
            company_name TEXT NOT NULL,
            industry TEXT,
            size_tier TEXT NOT NULL
        );
        """)
        
        # 2. Fact Table
        cursor.execute("""
        CREATE TABLE fact_deals (
            deal_key INTEGER PRIMARY KEY,
            company_key INTEGER NOT NULL,
            amount_usd REAL NOT NULL,
            license_seats INTEGER NOT NULL,
            FOREIGN KEY (company_key) REFERENCES dim_companies(company_key)
        );
        """)
        
        # 3. Dead Letter Queue Table
        cursor.execute("""
        CREATE TABLE dead_letter_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            failed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            event_source TEXT,
            error_msg TEXT,
            payload_json TEXT
        );
        """)
        self.conn.commit()
        
    def ingest_webhook(self, token: str, event_name: str, payload: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
        # 1. Token Authorization
        if token != INGEST_TOKEN:
            return 401, {"error": "Unauthorized: Invalid Ingest Token"}
            
        print(f"\n[*] Ingesting Event: '{event_name}'...")
        
        # 2. Event Routing & Schema Validation
        try:
            if event_name == "company.signup":
                return self._process_company_signup(payload)
            elif event_name == "deal.closed":
                return self._process_deal_closed(payload)
            else:
                return 400, {"error": f"Bad Request: Unknown event type '{event_name}'"}
        except Exception as e:
            error_desc = str(e)
            print(f"  [CRITICAL ERROR] Validation failed: {error_desc}")
            self._route_to_dlq(event_name, error_desc, payload)
            return 400, {"status": "rejected", "error": error_desc}

    def _process_company_signup(self, payload: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
        # Validate Required properties
        for prop in ["company_id", "company_name", "employees"]:
            if prop not in payload:
                raise ValueError(f"Missing required property '{prop}'")
                
        # Schema transformations (ETL)
        company_id = int(payload["company_id"])
        company_name = str(payload["company_name"])
        industry = str(payload.get("industry", "Maritime Education"))
        employees = int(payload["employees"])
        
        tier = "SME (1-50)" if employees <= 50 else "Enterprise (51+)"
        
        # Upsert Company Dimension
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO dim_companies (company_key, company_name, industry, size_tier)
        VALUES (?, ?, ?, ?);
        """, (company_id, company_name, industry, tier))
        self.conn.commit()
        
        print(f"  [DIMENSION UPSERT] Registered Company: {company_name} | Tier: {tier}")
        return 200, {"status": "success", "message": "Company signed up successfully"}
        
    def _process_deal_closed(self, payload: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
        # Validate properties
        for prop in ["deal_id", "company_id", "amount", "seats"]:
            if prop not in payload:
                raise ValueError(f"Missing required property '{prop}'")
                
        deal_id = int(payload["deal_id"])
        company_key = int(payload["company_id"])
        amount = float(payload["amount"])
        seats = int(payload["seats"])
        
        # Simulate transient Rate limit on first attempt
        self.rate_limit_attempts += 1
        if self.rate_limit_attempts == 1:
            print("  [API LIMIT] Encountered simulated HTTP 429: Too Many Requests.")
            print("  [RETRYING] Waiting 1.0s (exponential backoff retry 1)...")
            time.sleep(0.1) # Accelerated simulated wait
            # Fallthrough to retry attempt (which will succeed next)
            
        # Verify company exists in dimension table
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM dim_companies WHERE company_key = ?;", (company_key,))
        if not cursor.fetchone():
            raise ValueError(f"Foreign key constraint violation: Company ID '{company_key}' does not exist.")
            
        # Write Fact Table
        cursor.execute("""
        INSERT OR REPLACE INTO fact_deals (deal_key, company_key, amount_usd, license_seats)
        VALUES (?, ?, ?, ?);
        """, (deal_id, company_key, amount, seats))
        self.conn.commit()
        
        print(f"  [FACT LOAD] Registered Deal: ID {deal_id} | Amount: ${amount:,.2f} USD | Seats: {seats}")
        return 200, {"status": "success", "message": "Deal closed loaded successfully"}
        
    def _route_to_dlq(self, source: str, error_msg: str, payload: Dict[str, Any]):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO dead_letter_queue (event_source, error_msg, payload_json)
        VALUES (?, ?, ?);
        """, (source, error_msg, json.dumps(payload)))
        self.conn.commit()
        print(f"  [DLQ ROUTED] Saved failed payload to DLQ table. Slack alert dispatched.")

    def run_sales_report(self):
        print("\n" + "=" * 65)
        print("             CAPSTONE SALES ANALYSIS REPORT")
        print("=" * 65)
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT 
            c.company_name,
            c.size_tier,
            SUM(f.amount_usd) AS total_sales,
            SUM(f.license_seats) AS total_seats
        FROM fact_deals f
        JOIN dim_companies c ON f.company_key = c.company_key
        GROUP BY c.company_name, c.size_tier
        ORDER BY total_sales DESC;
        """)
        for row in cursor.fetchall():
            print(f"Academy: {row[0]:<25} | Tier: {row[1]:<15}")
            print(f"Sales:   ${row[2]:,.2f} USD       | Seats: {row[3]} Licenses")
            print("-" * 65)
            
        # Print DLQ audit logs
        cursor.execute("SELECT id, event_source, error_msg FROM dead_letter_queue;")
        dlq_records = cursor.fetchall()
        print(f"Dead Letter Queue Log Counts: {len(dlq_records)}")
        for dlq in dlq_records:
            print(f"  - Error ID {dlq[0]} | Source: {dlq[1]} | Error: {dlq[2]}")
        print("=" * 65)

if __name__ == "__main__":
    orchestrator = GTMOrchestrator()
    
    print("=" * 65)
    print("         INITIALIZING CAPSTONE GTM DATA INGESTION PIPELINE")
    print("=" * 65)
    
    # 1. Ingestion Event 1: Company Signup (Success)
    e1_payload = {
        "company_id": 1,
        "company_name": "Tolani Maritime Institute",
        "employees": 120,
        "industry": "Maritime Academy"
    }
    orchestrator.ingest_webhook(INGEST_TOKEN, "company.signup", e1_payload)
    
    # 2. Ingestion Event 2: Second Company Signup (Success)
    e2_payload = {
        "company_id": 2,
        "company_name": "IMSGOA Maritime College",
        "employees": 40,
        "industry": "Maritime College"
    }
    orchestrator.ingest_webhook(INGEST_TOKEN, "company.signup", e2_payload)
    
    # 3. Ingestion Event 3: Deal Closed with simulated rate limit retry (Success)
    e3_payload = {
        "deal_id": 501,
        "company_id": 1,
        "amount": 15000.00,
        "seats": 600
    }
    orchestrator.ingest_webhook(INGEST_TOKEN, "deal.closed", e3_payload)
    
    # 4. Ingestion Event 4: Malformed Schema Field (Failure -> DLQ)
    # Missing required company_name parameter
    e4_payload = {
        "company_id": 3,
        "employees": 50
    }
    orchestrator.ingest_webhook(INGEST_TOKEN, "company.signup", e4_payload)
    
    # 5. Ingestion Event 5: Foreign Key Violation (Failure -> DLQ)
    # Trying to link a deal to company 99, which is missing in our dimension table
    e5_payload = {
        "deal_id": 502,
        "company_id": 99,
        "amount": 5000.00,
        "seats": 200
    }
    orchestrator.ingest_webhook(INGEST_TOKEN, "deal.closed", e5_payload)
    
    # Run Capstone Report
    orchestrator.run_sales_report()
