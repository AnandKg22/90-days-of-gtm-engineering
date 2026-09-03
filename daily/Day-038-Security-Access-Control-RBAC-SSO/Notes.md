# Study Notes - Day 038: Security & Access Control (RBAC, SSO)

Today's studies focused on Role-Based Access Control (RBAC), Single Sign-On (SSO), OAuth 2.0 flow, token scopes, relational security schemas, SQL access validation, and caching optimization.

---

## 1. Security & Identity Management in GTM

To protect customer data and comply with SOC2, GTM applications enforce strict security controls:
*   **Role-Based Access Control (RBAC)**: Restricts resource access to authorized users based on their assigned roles (e.g., Sales AE, Marketing Rep, Admin).
*   **Single Sign-On (SSO)**: Centralizes credential management via external identity providers (IdP) using SAML or OIDC.
*   **OAuth Scopes**: Restricts API clients to the minimum required permissions (e.g. `contacts.read` allows downloading records, but blocks updates).

---

## 2. Deep-Dive: Security & Access Control Subtopics

To construct secure database and API environments, a GTM Engineer must master these three subtopics:

### 1. Database Design (RBAC Relational Tables)
*   **Definition**: Designing schemas that separate users, roles, and permissions to decouple security logic from application code:
    *   **Users**: Stores user details (`user_id`, `email`).
    *   **Roles**: Stores roles (`role_id`, `role_name` [Admin, Sales, Marketing]).
    *   **Permissions**: Stores scopes (`permission_id`, `scope_key` [contacts:read, contacts:write]).
    *   **User_Roles**: Map users to roles (`user_id`, `role_id`).
    *   **Role_Permissions**: Map roles to permissions (`role_id`, `permission_id`).

### 2. SQL Syntax (Access Verification Queries)
*   **Definition**: Writing SQL queries to verify if a user has the permission required to execute an action:
    ```sql
    SELECT COUNT(1) AS is_authorized
    FROM users u
    JOIN user_roles ur ON u.user_id = ur.user_id
    JOIN role_permissions rp ON ur.role_id = rp.role_id
    JOIN permissions p ON rp.permission_id = p.permission_id
    WHERE u.user_id = @request_user_id
      AND p.scope_key = @required_scope;
    ```
    If `is_authorized = 1`, the API allows the call; otherwise, it returns `403 Forbidden`.

### 3. Query Optimization (Access List Caching)
*   **Definition**: Optimizing permission evaluation speeds.
*   **GTM Application**: Joining five tables to check permissions on every single API request introduces significant database latency.
    *   **Indexing**: Build foreign key indexes on junction tables (`user_roles.user_id`, `role_permissions.role_id`).
    *   **Caching**: Cache the user's active permission list in an in-memory key-value store (like Redis) upon login or SSO token validation. The API checks the Redis cache first, bypassing the database entirely.
