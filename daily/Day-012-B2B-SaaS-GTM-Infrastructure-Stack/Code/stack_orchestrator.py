# B2B SaaS GTM Stack Orchestrator Engine
import json
import time
import sys
from typing import Dict, Any

# Ensure standard output uses UTF-8 to prevent Windows terminal character set crashes
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class MockStripeCheckout:
    @staticmethod
    def get_event() -> Dict[str, Any]:
        return {
            "event_id": "evt_stripe_99011",
            "customer_email": "dean@imsgoa.org",
            "quantity": 150,
            "amount_total": 4500.00
        }

class MockApolloAPI:
    @staticmethod
    def enrich_domain(email_domain: str) -> Dict[str, Any]:
        # Simulates enrichment API response
        return {
            "company_name": "IMSGOA Maritime College",
            "employee_count": 85,
            "tech_stack": ["Moodle", "Stripe", "Postgres"],
            "country": "IN"
        }

class MockHubSpotAPI:
    @staticmethod
    def upsert_company(properties: Dict[str, Any]) -> str:
        # Returns simulated HubSpot internal ID
        return "hs_comp_887012"

class MockOutreachAPI:
    @staticmethod
    def add_to_sequence(email: str, sequence_id: str) -> bool:
        return True

class MockSlackWebhook:
    @staticmethod
    def send_message(markdown_text: str):
        print(f"\n[SLACK BOT ROUTED]:\n{markdown_text}")

class MockPostgresDB:
    def __init__(self):
        self.logs = []
    def log_transaction(self, entry: Dict[str, Any]):
        self.logs.append(entry)

class GTMOrchestrator:
    def __init__(self):
        self.db = MockPostgresDB()
        
    def process_purchase(self, stripe_payload: Dict[str, Any]):
        email = stripe_payload["customer_email"]
        domain = email.split("@")[-1]
        
        print(f"Step 1: Webhook Received from Stripe (Email: {email}, Seats: {stripe_payload['quantity']})")
        
        # Step 2: Query Apollo Enrichment
        print(f"Step 2: Querying Apollo Enrichment API for domain '{domain}'...")
        enrichment_data = MockApolloAPI.enrich_domain(domain)
        print(f"  Enrichment Success: Resolved '{enrichment_data['company_name']}' with {enrichment_data['employee_count']} employees.")
        
        # Step 3: Map & Sync to HubSpot CRM
        print("Step 3: Transforming and posting company payload to HubSpot CRM Custom Fields...")
        hubspot_properties = {
            "name": enrichment_data["company_name"],
            "cadet_seats_purchased": stripe_payload["quantity"],
            "sponsoring_shipping_lines": enrichment_data["tech_stack"]
        }
        hs_id = MockHubSpotAPI.upsert_company(hubspot_properties)
        print(f"  HubSpot Sync Success: Updated company record ID: {hs_id}")
        
        # Step 4: Add to Outreach Sequence
        print("Step 4: Triggering Outreach onboarding campaign sequence 'seq_1190'...")
        outreach_status = MockOutreachAPI.add_to_sequence(email, "seq_1190")
        print(f"  Outreach Sync Success: Account Added status: {outreach_status}")
        
        # Step 5: Send Slack Alert
        print("Step 5: Sending alert to team Slack channel...")
        slack_msg = (
            f"[DEAL CLOSED WON]\n"
            f"- Company: {enrichment_data['company_name']}\n"
            f"- Seats:   {stripe_payload['quantity']}\n"
            f"- Value:   ${stripe_payload['amount_total']:,.2f} USD\n"
            f"- Owner:   Sales Automation Bot"
        )
        MockSlackWebhook.send_message(slack_msg)
        
        # Step 6: Log transaction to Postgres DB
        print("\nStep 6: Recording transaction in GTM replica database...")
        db_record = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "company_name": enrichment_data["company_name"],
            "hubspot_id": hs_id,
            "seats": stripe_payload["quantity"],
            "amount_usd": stripe_payload["amount_total"]
        }
        self.db.log_transaction(db_record)
        print("  Database Sync Success. Log appended.")

if __name__ == "__main__":
    print("=" * 65)
    print("        INITIALIZING B2B SAAS GTM STACK ORCHESTRATOR")
    print("=" * 65)
    
    # Ingest mock event
    stripe_event = MockStripeCheckout.get_event()
    
    # Process through orchestrator
    orchestrator = GTMOrchestrator()
    orchestrator.process_purchase(stripe_event)
    
    print("\n" + "=" * 65)
    print("                 POSTGRES ANALYTICS LOGS")
    print("=" * 65)
    for log in orchestrator.db.logs:
        print(json.dumps(log, indent=4))
    print("=" * 65)
