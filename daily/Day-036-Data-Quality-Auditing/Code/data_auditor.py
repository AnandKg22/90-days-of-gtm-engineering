# GTM Data Auditing & Quality Cleaner
import sys
import json
import os
from datetime import datetime
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Raw, dirty GTM lead dataset
dirty_crm_leads = [
    # 1. Valid record
    {"lead_id": 201, "email": "dean@imsgoa.org", "company_name": "IMSGOA Maritime", "deal_amount": 8000.00, "timestamp": "2026-07-01"},
    
    # 2. Duplicate email (older timestamp than record 1) -> should be flagged as duplicate
    {"lead_id": 202, "email": "dean@imsgoa.org", "company_name": "IMSGOA Maritime Inc", "deal_amount": 8000.00, "timestamp": "2026-06-15"},
    
    # 3. Invalid email format (missing '.') -> should be quarantined
    {"lead_id": 203, "email": "sharma@tolani", "company_name": "Tolani Maritime", "deal_amount": 12000.00, "timestamp": "2026-07-03"},
    
    # 4. Negative deal value -> should be quarantined
    {"lead_id": 204, "email": "registrar@ametuniv.edu.in", "company_name": "AMET University", "deal_amount": -1500.00, "timestamp": "2026-07-05"},
    
    # 5. Missing company name (None) -> should be quarantined
    {"lead_id": 205, "email": "student@maritime.com", "company_name": None, "deal_amount": 3000.00, "timestamp": "2026-07-08"},
    
    # 6. Valid record
    {"lead_id": 206, "email": "captain.raw@navy.gov", "company_name": "Navy Academy", "deal_amount": 0.00, "timestamp": "2026-07-10"}
]

class CRMDataAuditor:
    def __init__(self, raw_leads: List[Dict[str, Any]]):
        self.raw_leads = raw_leads
        
    def audit_and_clean(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, int]]:
        cleaned_leads = []
        quarantined_leads = []
        
        # Performance trackers
        stats = {
            "total_rows": len(self.raw_leads),
            "passed_rows": 0,
            "quarantined_rows": 0,
            "duplicate_rows": 0,
            "error_invalid_email": 0,
            "error_negative_amount": 0,
            "error_missing_company": 0
        }
        
        # 1. Resolve duplicates by email (keep latest timestamp)
        email_map: Dict[str, Dict[str, Any]] = {}
        duplicates_to_quarantine: List[Dict[str, Any]] = []
        
        for lead in self.raw_leads:
            email = lead["email"]
            if not email:
                continue
                
            lead_date = datetime.strptime(lead["timestamp"], "%Y-%m-%d")
            
            if email not in email_map:
                email_map[email] = lead
            else:
                existing_lead = email_map[email]
                existing_date = datetime.strptime(existing_lead["timestamp"], "%Y-%m-%d")
                
                # Compare timestamps
                if lead_date > existing_date:
                    # Current lead is newer, discard the older one
                    duplicates_to_quarantine.append(existing_lead)
                    email_map[email] = lead
                else:
                    # Existing lead is newer, discard current lead
                    duplicates_to_quarantine.append(lead)
                    
        # Process duplicate statistics
        for dup in duplicates_to_quarantine:
            stats["duplicate_rows"] += 1
            stats["quarantined_rows"] += 1
            dup_copy = dup.copy()
            dup_copy["quarantine_reason"] = "Duplicate lead record; older timestamp superseded."
            quarantined_leads.append(dup_copy)
            
        # 2. Validate non-duplicate leads
        active_leads = email_map.values()
        for lead in active_leads:
            errors = []
            
            # Check constraint: email validation
            email = lead.get("email", "")
            if not email or "@" not in email or "." not in email:
                errors.append("Invalid email format (must contain '@' and '.')")
                stats["error_invalid_email"] += 1
                
            # Check constraint: deal amount validation
            amount = lead.get("deal_amount")
            if amount is None or amount < 0.0:
                errors.append("Invalid deal amount (value must be >= 0.0)")
                stats["error_negative_amount"] += 1
                
            # Check constraint: missing company validation
            company = lead.get("company_name")
            if not company:
                errors.append("Missing company name (field cannot be null or empty)")
                stats["error_missing_company"] += 1
                
            # Direct to Clean or Quarantine
            if errors:
                stats["quarantined_rows"] += 1
                lead_copy = lead.copy()
                lead_copy["quarantine_reason"] = " | ".join(errors)
                quarantined_leads.append(lead_copy)
            else:
                stats["passed_rows"] += 1
                cleaned_leads.append(lead)
                
        return cleaned_leads, quarantined_leads, stats

if __name__ == "__main__":
    auditor = CRMDataAuditor(dirty_crm_leads)
    clean, quarantine, summary = auditor.audit_and_clean()
    
    # Write quarantine log to JSON
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "quarantine_log.json")
    
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(quarantine, f, indent=2, ensure_ascii=False)
        
    print("=" * 65)
    print("             VIVAEXAMS CRM DATA AUDIT SCORECARD")
    print("=" * 65)
    print(f"Total Records Inspected:  {summary['total_rows']}")
    print(f"Passed Clean Rows:        {summary['passed_rows']}")
    print(f"Quarantined Error Rows:   {summary['quarantined_rows']}")
    print("-" * 65)
    print("Anomaly Breakdown Log:")
    print(f"  - Duplicate Records:    {summary['duplicate_rows']}")
    print(f"  - Malformed Emails:     {summary['error_invalid_email']}")
    print(f"  - Negative Amounts:     {summary['error_negative_amount']}")
    print(f"  - Missing Company Name: {summary['error_missing_company']}")
    print("-" * 65)
    print(f"Quarantined Records Exported: {log_path}")
    print("-" * 65)
    
    # Print Quarantined details
    print("Quarantine Registry Details:")
    for r in quarantine:
        print(f"  - Lead ID {r['lead_id']} | Reason: {r['quarantine_reason']}")
    print("-" * 65)
    
    # Financial data validity warning
    if summary["quarantined_rows"] > 0:
        pct = (summary["quarantined_rows"] / summary["total_rows"]) * 100.0
        print(f"  [ALERT] Dataset error rate is {pct:.1f}%.")
        print("  Cleanse source webhooks and verify HubSpot input forms.")
    print("=" * 65)
