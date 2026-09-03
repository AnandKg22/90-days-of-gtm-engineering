# Project Assignment - Day 038: OAuth Scope & RBAC Simulator

This project requires developing a Python Access Control & OAuth RBAC Simulator. It models users, roles, and allowed scopes, generates scoped access tokens, validates permissions on incoming API requests, and logs security audits to the console.

---

## 🎯 Requirements

Your Python application must:
1.  Define the RBAC directory model containing:
    *   `users`: ID and name mapping.
    *   `user_roles`: User ID to Role name mapping (Admin, Sales, Marketing).
    *   `role_scopes`: Role to allowed permission scopes mapping.
2.  Implement **OAuth Token Issuance**:
    *   `request_scoped_token(user_id, requested_scopes)`:
        *   Verify the user's role.
        *   Compare requested scopes against the role's allowed scopes.
        *   Issue a mock token string (e.g. `mock_token_123`) containing the allowed scopes.
3.  Implement **API Gateway Validation**:
    *   `verify_api_access(token, required_scope)`:
        *   Validate the token exists and contains the required scope.
        *   Return `True` (Access Granted) or `False` (Access Denied).
4.  Test and log security scenarios:
    *   Admin requesting full access (allowed).
    *   Sales AE requesting `billing:write` (scope stripped, write denied).
    *   Marketing Rep requesting `contacts:write` (denied).
5.  Print the token issuance events and access logs to the console.

---

## 💻 Deliverable Code

A complete, working security simulator has been created and placed in [Code/access_control.py](Code/access_control.py). It models the roles, executes the validation loops, and prints the audit logs.
