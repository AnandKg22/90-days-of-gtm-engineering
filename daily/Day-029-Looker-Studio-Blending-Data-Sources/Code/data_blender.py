# Looker Data Blender & Join Simulator
import sys
import time
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Source 1: HubSpot CRM Leads
hubspot_contacts = [
    {"email": "dean@imsgoa.org", "lead_source": "google"},
    {"email": "registrar@ametuniv.edu.in", "lead_source": "newsletter"},
    {"email": "sharma.r@tolani.edu", "lead_source": "google"},
    {"email": "captain.raw@navy.gov", "lead_source": "organic"}, # Unconverted lead
    {"email": "student.demo@maritime.com", "lead_source": "direct"} # Unconverted lead
]

# Source 2: Stripe Billing Transactions
stripe_payments = [
    {"customer_email": "dean@imsgoa.org", "amount_usd": 8000.00},
    {"customer_email": "registrar@ametuniv.edu.in", "amount_usd": 15000.00},
    {"customer_email": "sharma.r@tolani.edu", "amount_usd": 12000.00}
]

class LookerDataBlender:
    def __init__(self, contacts: List[Dict[str, Any]], payments: List[Dict[str, Any]]):
        self.contacts = contacts
        self.payments = payments
        
    def inner_join(self) -> List[Dict[str, Any]]:
        joined = []
        for contact in self.contacts:
            for payment in self.payments:
                if contact["email"] == payment["customer_email"]:
                    joined.append({
                        "email": contact["email"],
                        "lead_source": contact["lead_source"],
                        "amount_usd": payment["amount_usd"]
                    })
        return joined
        
    def left_outer_join(self) -> List[Dict[str, Any]]:
        joined = []
        for contact in self.contacts:
            match_found = False
            for payment in self.payments:
                if contact["email"] == payment["customer_email"]:
                    joined.append({
                        "email": contact["email"],
                        "lead_source": contact["lead_source"],
                        "amount_usd": payment["amount_usd"]
                    })
                    match_found = True
                    break
            if not match_found:
                # Retain lead, populate null payment
                joined.append({
                    "email": contact["email"],
                    "lead_source": contact["lead_source"],
                    "amount_usd": None
                })
        return joined

if __name__ == "__main__":
    blender = LookerDataBlender(hubspot_contacts, stripe_payments)
    
    print("=" * 65)
    print("             LOOKER STUDIO DATA BLENDING ENGINE SIMULATOR")
    print("=" * 65)
    print(f"HubSpot Raw Contacts: {len(hubspot_contacts)}")
    print(f"Stripe Raw Payments:  {len(stripe_payments)}")
    print("-" * 65)
    
    # 1. Run Inner Join
    inner_results = blender.inner_join()
    print("Inner Join Output (Paying Customers Only):")
    for r in inner_results:
        print(f"  - {r['email']} | Source: {r['lead_source']} | Paid: ${r['amount_usd']:,.2f}")
    print(f"  Total Rows: {len(inner_results)}")
    print("-" * 65)
    
    # 2. Run Left Outer Join
    left_results = blender.left_outer_join()
    print("Left Outer Join Output (Complete Lead Funnel):")
    for r in left_results:
        paid_str = f"${r['amount_usd']:,.2f}" if r['amount_usd'] is not None else "NULL (Unconverted)"
        print(f"  - {r['email']:<26} | Source: {r['lead_source']:<10} | Paid: {paid_str}")
    print(f"  Total Rows: {len(left_results)}")
    
    # 3. Data Integrity Audit
    print("\n" + "=" * 65)
    print("                 DATA INTEGRITY AUDITING DIGEST")
    print("=" * 65)
    print(f"Left Join Rows (True funnel size):  {len(left_results)}")
    print(f"Inner Join Rows (Biased funnel):   {len(inner_results)}")
    
    lost_records = len(left_results) - len(inner_results)
    print(f"Unconverted Leads Dropped:         {lost_records} records lost")
    print("-" * 65)
    if lost_records > 0:
        print("  [CRITICAL WARNING]: Inner Joins drop non-paying prospects.")
        print("  This biases conversions: you cannot calculate Lead-to-Customer conversion rates.")
        print("  Use LEFT OUTER JOINs as the default join operator for GTM dashboards.")
    print("=" * 65)
    
    # 4. Performance Audit
    print("\n" + "[*] Simulating client-side rendering latency...")
    # Client-side data blending runs joins in JavaScript, causing lag on larger sets
    start_time = time.perf_counter()
    time.sleep(0.02) # Simulated browser join thread lag
    duration_ms = (time.perf_counter() - start_time) * 1000.0
    
    print(f"  Client-side browser join time: {duration_ms:.2f} ms")
    print("  [RECOMMENDATION]: Avoid client-side Data Blending inside Looker.")
    print("  Pre-join datasets in the warehouse using dbt or SQL Views.")
    print("=" * 65)
