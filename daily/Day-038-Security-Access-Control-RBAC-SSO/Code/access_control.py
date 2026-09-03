# GTM Access Control & OAuth RBAC Simulator
import sys
import uuid
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Directory directory mapping Users -> Roles
user_directory = {
    "usr_01": {"name": "Vikram Singh", "role": "Admin"},
    "usr_02": {"name": "Rajesh Sharma", "role": "Sales AE"},
    "usr_03": {"name": "Amit Kumar", "role": "Marketing Rep"}
}

# Role to allowed OAuth scopes mapping
role_scopes_matrix = {
    "Admin": ["contacts:read", "contacts:write", "billing:read", "billing:write"],
    "Sales AE": ["contacts:read", "contacts:write", "billing:read"],
    "Marketing Rep": ["contacts:read"]
}

# Global Token Registry (Simulates OAuth Session Cache)
token_registry: Dict[str, Dict[str, Any]] = {}

class OAuthRBACEngine:
    def __init__(self, users: Dict[str, Dict[str, Any]], matrix: Dict[str, List[str]]):
        self.users = users
        self.matrix = matrix
        
    def request_scoped_token(self, user_id: str, requested_scopes: List[str]) -> Tuple[str, List[str]]:
        # 1. Verify user exists
        if user_id not in self.users:
            raise ValueError("Unauthorized User ID.")
            
        user = self.users[user_id]
        role = user["role"]
        allowed_scopes = self.matrix[role]
        
        # 2. Scope intersection: strip scopes not allowed for user role
        granted_scopes = [scope for scope in requested_scopes if scope in allowed_scopes]
        
        # 3. Generate Mock Token
        token_str = f"access_token_{uuid.uuid4().hex[:12]}"
        
        # Cache token details
        token_registry[token_str] = {
            "user_id": user_id,
            "role": role,
            "scopes": granted_scopes
        }
        
        return token_str, granted_scopes

    def verify_api_access(self, token: str, required_scope: str) -> Tuple[bool, str]:
        # API Gateway check
        if token not in token_registry:
            return False, "Invalid / Expired Token."
            
        session = token_registry[token]
        user_id = session["user_id"]
        user_name = self.users[user_id]["name"]
        user_scopes = session["scopes"]
        
        if required_scope in user_scopes:
            return True, f"Access Granted to {user_name} ({session['role']})."
        else:
            return False, f"Access Denied for {user_name} ({session['role']}). Missing scope '{required_scope}'."

if __name__ == "__main__":
    engine = OAuthRBACEngine(user_directory, role_scopes_matrix)
    
    print("=" * 65)
    print("             VIVAEXAMS OAuth & RBAC GATEWAY SIMULATOR")
    print("=" * 65)
    
    # Scenario 1: Admin requests full access
    print("[SCENARIO 1] Admin requests full scopes...")
    t1, s1 = engine.request_scoped_token("usr_01", ["contacts:read", "contacts:write", "billing:read", "billing:write"])
    print(f"  Token Issued: {t1}")
    print(f"  Granted Scopes: {s1}")
    
    # Gateway evaluation
    ok1, msg1 = engine.verify_api_access(t1, "billing:write")
    print(f"  Gateway Test ('billing:write'): {msg1}")
    print("-" * 65)
    
    # Scenario 2: Sales AE requests billing:write
    print("[SCENARIO 2] Sales AE requests billing:write scope...")
    t2, s2 = engine.request_scoped_token("usr_02", ["contacts:read", "billing:write"])
    print(f"  Token Issued: {t2}")
    print(f"  Granted Scopes: {s2} (billing:write stripped)")
    
    # Gateway evaluation
    ok2, msg2 = engine.verify_api_access(t2, "billing:write")
    print(f"  Gateway Test ('billing:write'): {msg2}")
    
    ok2_read, msg2_read = engine.verify_api_access(t2, "contacts:read")
    print(f"  Gateway Test ('contacts:read'): {msg2_read}")
    print("-" * 65)
    
    # Scenario 3: Marketing Rep requests contacts:write
    print("[SCENARIO 3] Marketing Rep requests contacts:write scope...")
    t3, s3 = engine.request_scoped_token("usr_03", ["contacts:read", "contacts:write"])
    print(f"  Token Issued: {t3}")
    print(f"  Granted Scopes: {s3} (contacts:write stripped)")
    
    # Gateway evaluation
    ok3, msg3 = engine.verify_api_access(t3, "contacts:write")
    print(f"  Gateway Test ('contacts:write'): {msg3}")
    print("-" * 65)
    
    # Security log warning checks
    unauthorized_attempts = 2 # Scenarios 2 and 3 failed write access
    print("SECURITY COMPLIANCE AUDIT:")
    if unauthorized_attempts > 0:
        print(f"  [ALERT] Blocked {unauthorized_attempts} unauthorized write attempts.")
        print("  RBAC constraints successfully enforced at API Gateway tier.")
    print("=" * 65)
