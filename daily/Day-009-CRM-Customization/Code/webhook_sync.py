# Webhook Integration & Data Mapper Engine
import json
import time
from typing import Dict, Any

# 1. Mock Stripe Webhook Event Payload
mock_stripe_webhook = {
    "event_id": "evt_stripe_8821",
    "type": "checkout.session.completed",
    "created_at": 1783948800,
    "data": {
        "customer_email": "dean@tolani.edu",
        "quantity": 250,
        "sponsors": "SYNERGY, FLEET, MAERSK",
        "compliance_verified": True,
        "amount_total": 8000.00
    }
}

class CRMDataMapper:
    def __init__(self):
        # Maps Stripe variables to CRM Internal API Property Tags
        self.mapping_rules = {
            "customer_email": "email",
            "quantity": "cadet_seats_purchased",
            "sponsors": "sponsoring_shipping_lines",
            "compliance_verified": "proctoring_compliance_approved"
        }
        
    def transform(self, stripe_data: Dict[str, Any]) -> Dict[str, Any]:
        crm_payload = {}
        for source_key, target_key in self.mapping_rules.items():
            if source_key in stripe_data:
                val = stripe_data[source_key]
                
                # Apply transformations
                if source_key == "sponsors":
                    # Convert comma-separated string to list
                    val = [s.strip() for s in val.split(",")]
                    
                crm_payload[target_key] = val
        return crm_payload

class HubSpotAPIMock:
    def post_company_update(self, email: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        # Simulates HubSpot REST API POST request
        time.sleep(0.2) # Simulate network lag
        return {
            "status": "success",
            "hubspot_id": "hs_comp_998102",
            "updated_properties": properties,
            "synced_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    print("=" * 65)
    print("           INITIALIZING WEBHOOK INTEGRATION SYNC")
    print("=" * 65)
    print(f"Stripe Webhook Received: {mock_stripe_webhook['event_id']}")
    print(f"Event Type:             {mock_stripe_webhook['type']}")
    print("-" * 65)
    
    # Extract raw data block
    raw_billing_data = mock_stripe_webhook["data"]
    
    # 1. Transform Payload via CRMDataMapper
    mapper = CRMDataMapper()
    mapped_properties = mapper.transform(raw_billing_data)
    
    print("Mapped CRM Custom Fields Payload:")
    print(json.dumps(mapped_properties, indent=4))
    print("-" * 65)
    
    # 2. Sync to Mock HubSpot API
    print("[*] Posting updates to HubSpot REST API endpoint /companies/v1/custom-update...")
    api = HubSpotAPIMock()
    target_email = mapped_properties["email"]
    
    # Separate email lookup from properties block
    fields_to_sync = {k: v for k, v in mapped_properties.items() if k != "email"}
    
    response = api.post_company_update(target_email, fields_to_sync)
    
    print("\nHubSpot API Response:")
    print(json.dumps(response, indent=4))
    print("=" * 65)
