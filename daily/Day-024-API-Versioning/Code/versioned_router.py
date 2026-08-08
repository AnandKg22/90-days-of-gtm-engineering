# Versioned GTM API Router Simulator
import sys
from typing import Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class VersionedRouter:
    def __init__(self):
        # Database mimicking V2 storage requirements
        self.database: Dict[str, Dict[str, Any]] = {}
        
    def resolve_version(self, path: str, headers: Dict[str, str]) -> str:
        # 1. Resolve via URL path
        if "/v1/" in path:
            return "v1"
        elif "/v2/" in path:
            return "v2"
            
        # 2. Resolve via Header
        header_version = headers.get("X-API-Version", "")
        if header_version == "2026-07-13" or header_version == "v2":
            return "v2"
        elif header_version == "v1":
            return "v1"
            
        # Default to v2 (Current)
        return "v2"

    def process_request(self, path: str, headers: Dict[str, str], payload: Dict[str, Any]) -> Tuple[int, Dict[str, str], Dict[str, Any]]:
        version = self.resolve_version(path, headers)
        response_headers = {"Content-Type": "application/json"}
        
        print(f"\n[*] Routing request: '{path}' (Detected Version: {version})")
        
        # Inject deprecation warning headers if V1 is used
        if version == "v1":
            response_headers["Deprecation"] = "true"
            response_headers["Sunset"] = "Mon, 13 Jul 2026 10:00:00 GMT"
            print("  [DEPRECATION WARNING] Client is querying legacy V1 endpoint. Sunset set for Mon, 13 Jul 2026.")
            
            # Translate V1 payload to V2 format (Backward Compatibility)
            print("  [TRANSLATION] Converting V1 payload to V2 format...")
            fullname = payload.get("fullname", "")
            company = payload.get("company", "")
            
            name_parts = fullname.split(" ", 1)
            first_name = name_parts[0] if len(name_parts) > 0 else ""
            last_name = name_parts[1] if len(name_parts) > 1 else ""
            
            normalized_payload = {
                "first_name": first_name,
                "last_name": last_name,
                "organization": company
            }
        else:
            normalized_payload = payload
            
        # Save to database (mimicking v2 schema ingest)
        email = payload.get("email", "unknown@email.com")
        self.database[email] = normalized_payload
        
        print(f"  [SAVED TO DATABASE]: {normalized_payload}")
        return 200, response_headers, {"status": "success", "resolved_version": version}

if __name__ == "__main__":
    router = VersionedRouter()
    
    print("=" * 65)
    print("             VIVAEXAMS VERSIONED API ROUTER ENGINE")
    print("=" * 65)
    
    # Test Case 1: Legacy V1 Path Request
    # Payload matches v1 keys (fullname, company)
    req1_path = "/api/v1/prospect"
    req1_headers = {}
    req1_payload = {
        "email": "dean@imsgoa.org",
        "fullname": "Vikram Singh",
        "company": "IMSGOA Maritime College"
    }
    code1, resp_hdrs1, resp_body1 = router.process_request(req1_path, req1_headers, req1_payload)
    print(f"  Response Status:  {code1}")
    print(f"  Response Headers: {resp_hdrs1}")
    print(f"  Response Body:    {resp_body1}")
    print("-" * 65)
    
    # Test Case 2: V2 Header Request (Resource URL remains clean)
    # Payload matches v2 keys (first_name, last_name, organization)
    req2_path = "/api/prospect"
    req2_headers = {"X-API-Version": "2026-07-13"}
    req2_payload = {
        "email": "sharma.r@tolani.edu",
        "first_name": "Rajesh",
        "last_name": "Sharma",
        "organization": "Tolani Maritime Institute"
    }
    code2, resp_hdrs2, resp_body2 = router.process_request(req2_path, req2_headers, req2_payload)
    print(f"  Response Status:  {code2}")
    print(f"  Response Headers: {resp_hdrs2}")
    print(f"  Response Body:    {resp_body2}")
    print("-" * 65)
    
    # Test Case 3: Default V2 Request (No version tags)
    req3_path = "/api/prospect"
    req3_headers = {}
    req3_payload = {
        "email": "registrar@ametuniv.edu.in",
        "first_name": "Amit",
        "last_name": "Kumar",
        "organization": "AMET University"
    }
    code3, resp_hdrs3, resp_body3 = router.process_request(req3_path, req3_headers, req3_payload)
    print(f"  Response Status:  {code3}")
    print(f"  Response Headers: {resp_hdrs3}")
    print(f"  Response Body:    {resp_body3}")
    print("=" * 65)
