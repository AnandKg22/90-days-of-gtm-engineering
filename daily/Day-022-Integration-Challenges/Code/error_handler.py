# GTM Integration Retry & Error Handler
import json
import logging
import random
import sys
import time
from typing import Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configure local file logging
LOG_FILE = "integration_failures.log"
logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.ERROR
)

class MockAPI:
    def __init__(self):
        # Tracking request attempts to simulate deterministic responses
        self.request_counters: Dict[str, int] = {}
        
    def call_endpoint(self, payload: Dict[str, Any]) -> Tuple[int, str]:
        endpoint = payload.get("endpoint", "")
        if endpoint not in self.request_counters:
            self.request_counters[endpoint] = 0
        self.request_counters[endpoint] += 1
        
        attempt = self.request_counters[endpoint]
        
        # Scenario 1: Rate Limit on first try, success on second
        if endpoint == "/hubspot/company/upsert":
            if attempt == 1:
                return 429, "Rate Limit Exceeded: Too Many Requests"
            return 200, "Hubspot Company Upsert Successfully Completed"
            
        # Scenario 2: Service down twice, success on third
        elif endpoint == "/stripe/invoice/create":
            if attempt < 3:
                return 503, "Service Temporarily Unavailable: Database locked"
            return 200, "Stripe Invoice Created Successfully"
            
        # Scenario 3: Validation Error (Schema Conflict) - Fails immediately
        elif endpoint == "/outreach/prospect/add":
            return 400, "Bad Request: Custom field 'job_role' does not exist in schema"
            
        # Scenario 4: Critical server down completely (exceeds all retry limits)
        elif endpoint == "/slack/deal/alert":
            return 500, "Internal Server Error: Connection timed out"
            
        return 200, "Success"

class SafeGTMClient:
    def __init__(self):
        self.api = MockAPI()
        
    def send_request(self, payload: Dict[str, Any]) -> bool:
        endpoint = payload.get("endpoint", "")
        print(f"\n[*] Dispatching request to endpoint '{endpoint}'...")
        
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            status_code, response_msg = self.api.call_endpoint(payload)
            
            # Case 1: Success
            if status_code == 200:
                print(f"  [SUCCESS] HTTP 200: {response_msg}")
                return True
                
            # Case 2: Validation Error - Reject immediately, skip retries
            elif status_code == 400:
                print(f"  [CRITICAL ERROR] HTTP 400: {response_msg}")
                print("  Schema Validation Mismatch. Skipping retries to prevent database lockups.")
                self.route_to_dead_letter_queue(payload, status_code, response_msg)
                return False
                
            # Case 3: Retriable Errors (429 Rate limits, 503/500 Server downs)
            else:
                print(f"  [API WARNING] Attempt {attempt} failed with HTTP {status_code}: {response_msg}")
                
                if attempt == max_retries:
                    print(f"  [FATAL] Exceeded maximum retry limit of {max_retries} attempts.")
                    self.route_to_dead_letter_queue(payload, status_code, response_msg)
                    return False
                
                # Calculate Exponential Backoff with Jitter
                # wait_time = 2^attempt + random float between 0 and 1
                jitter = random.uniform(0.1, 0.9)
                wait_time = (2 ** attempt) + jitter
                
                # Scale wait_time down to 0.1s for simulation speed
                simulated_sleep = wait_time * 0.1
                print(f"  [RETRYING] Waiting {wait_time:.2f} seconds (simulated: {simulated_sleep:.2f}s)...")
                time.sleep(simulated_sleep)
                
        return False
        
    def route_to_dead_letter_queue(self, payload: Dict[str, Any], status_code: int, error_msg: str):
        # 1. Simulate routing to DLQ Database
        print(f"  [DLQ ROUTED] Saved failed payload to Dead Letter Queue.")
        print(f"  [SLACK ALERT] sent alert: *Integration Down* Target: {payload.get('endpoint')} | Error: {status_code}")
        
        # 2. Write to local failure log file
        log_entry = {
            "endpoint": payload.get("endpoint"),
            "status_code": status_code,
            "error": error_msg,
            "payload": payload.get("data")
        }
        logging.error(json.dumps(log_entry))
        print(f"  [LOGGED] Details written to file: {LOG_FILE}")

if __name__ == "__main__":
    client = SafeGTMClient()
    
    print("=" * 65)
    print("             VIVAEXAMS FAULT-TOLERANT INTEGRATION CLIENT")
    print("=" * 65)
    
    # 1. Test Rate Limiting (429) -> Succeeds on retry
    payload_m1 = {
        "endpoint": "/hubspot/company/upsert",
        "data": {"domain": "imsgoa.org", "cadet_licenses": 200}
    }
    client.send_request(payload_m1)
    
    # 2. Test Server Error (503) -> Succeeds on retry 2
    payload_m2 = {
        "endpoint": "/stripe/invoice/create",
        "data": {"customer": "dean@imsgoa.org", "amount": 8000.00}
    }
    client.send_request(payload_m2)
    
    # 3. Test Validation Error (400) -> Fails immediately, goes to DLQ
    payload_m3 = {
        "endpoint": "/outreach/prospect/add",
        "data": {"email": "captain@imsgoa.org", "job_role": "Deck Officer"}
    }
    client.send_request(payload_m3)
    
    # 4. Test Permanent Connection Failure (500) -> Exceeds max retries, goes to DLQ
    payload_m4 = {
        "endpoint": "/slack/deal/alert",
        "data": {"channel": "sales-alerts", "message": "Deal Closed Won!"}
    }
    client.send_request(payload_m4)
    
    print("\n" + "=" * 65)
