# GTM PII Masking & Compliance Engine
import sys
import hashlib
import json
import os
from datetime import datetime, timezone
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock Customer contact records containing PII
crm_contacts_db = [
    {"user_id": "usr_01", "name": "Vikram Singh", "email": "dean@imsgoa.org", "phone": "+91-98765-43210", "total_purchases_usd": 15000.00},
    {"user_id": "usr_02", "name": "Rajesh Sharma", "email": "sharma.r@tolani.edu", "phone": "+91-99887-76655", "total_purchases_usd": 8000.00},
    {"user_id": "usr_03", "name": "Amit Kumar", "email": "registrar@ametuniv.edu.in", "phone": "+91-91234-56789", "total_purchases_usd": 25000.00}
]

class CRMComplianceEngine:
    def __init__(self, database: List[Dict[str, Any]]):
        self.db = database
        self.audit_log = []
        
    def hash_email(self, email: str) -> str:
        # Generate SHA-256 hash of email for compliant joins
        return hashlib.sha256(email.strip().lower().encode("utf-8")).hexdigest()
        
    def mask_email(self, email: str) -> str:
        # Mask email, keeping only first and last character of the username
        try:
            name, domain = email.split("@")
            if len(name) <= 2:
                masked_name = name[0] + "***"
            else:
                masked_name = name[0] + "*" * (len(name) - 2) + name[-1]
            return f"{masked_name}@{domain}"
        except Exception:
            return "masked_email@error.com"
            
    def mask_phone(self, phone: str) -> str:
        # Mask phone, keeping country code and last 4 digits
        # Format assumed: +XX-XXXXX-XXXXX
        try:
            parts = phone.split("-")
            if len(parts) >= 3:
                return f"{parts[0]}-*****{parts[-1]}"
            return "******" + phone[-4:]
        except Exception:
            return "redacted_phone"

    def process_gdpr_deletion(self, user_id: str) -> bool:
        # Right to be Forgotten: Anonymize identifiers, keep financial aggregates
        for record in self.db:
            if record["user_id"] == user_id:
                old_email = record["email"]
                hashed_email = self.hash_email(old_email)
                
                # Overwrite PII fields with anonymized tokens
                record["name"] = "ANONYMIZED_USER"
                record["email"] = f"ANON_{hashed_email[:16]}"
                record["phone"] = "REDACTED"
                # record["total_purchases_usd"] remains unchanged!
                
                # Log compliance receipt
                audit_entry = {
                    "audit_id": len(self.audit_log) + 301,
                    "action": "ANONYMIZE_USER_GDPR_REQUEST",
                    "user_id": user_id,
                    "hashed_identifier": hashed_email,
                    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                }
                self.audit_log.append(audit_entry)
                return True
        return False

if __name__ == "__main__":
    engine = CRMComplianceEngine(crm_contacts_db)
    
    print("=" * 65)
    print("             VIVAEXAMS CRM DATA COMPLIANCE ENGINE")
    print("=" * 65)
    
    # 1. Print Masked Data (Simulating Looker Dashboard presentation)
    print("Masked User Directory (Dashboard View):")
    for r in engine.db:
        m_email = engine.mask_email(r["email"])
        m_phone = engine.mask_phone(r["phone"])
        hashed = engine.hash_email(r["email"])
        print(f"  - User: {r['name']:<15} | Email: {m_email:<26} | Phone: {m_phone:<16} | Hash: {hashed[:12]}...")
    print("-" * 65)
    
    # 2. Process GDPR Deletion Request for Vikram Singh (usr_01)
    target_user = "usr_01"
    print(f"Processing GDPR 'Right to be Forgotten' Request for User: {target_user}...")
    success = engine.process_gdpr_deletion(target_user)
    
    if success:
        print(f"  [SUCCESS] Anonymization complete for user: {target_user}")
    print("-" * 65)
    
    # 3. Print Database State (Confirming PII is gone but financial metrics exist)
    print("Post-Anonymization Database State (Finance View):")
    for r in engine.db:
        print(f"  - User ID: {r['user_id']} | Name: {r['name']:<15} | Email: {r['email']:<21} | Spent: ${r['total_purchases_usd']:,.2f}")
    print("-" * 65)
    
    # Write compliance audit log to file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "compliance_audit.json")
    
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(engine.audit_log, f, indent=2, ensure_ascii=False)
        
    print(f"Compliance Audit Log written to: {log_path}")
    print(json.dumps(engine.audit_log, indent=2))
    print("=" * 65)
