# Exercises - Day 038: Security Access Policies

This document details the Role-Based Access Control (RBAC) matrix and OAuth scope validation rules used to secure GTM databases.

---

## 📋 GTM RBAC Permission Matrix

This matrix defines which API scopes are granted to specific team roles:

| Role Name | Scope: `contacts:read` | Scope: `contacts:write` | Scope: `billing:read` | Scope: `billing:write` | Primary Job Function |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Admin`** | **`Allowed`** | **`Allowed`** | **`Allowed`** | **`Allowed`** | Full infrastructure controls. |
| **`Sales AE`** | **`Allowed`** | **`Allowed`** | **`Allowed`** | `Denied` | Customer updates and CRM review. |
| **`Marketing Rep`**| **`Allowed`** | `Denied` | `Denied` | `Denied` | Read-only lead lists for campaigns. |

---

## ⚙️ OAuth Scope Intersection Policy

To enforce the principle of least privilege, GTM Authorization Servers perform a set intersection check:

```
[ Client requests token with: contacts:read, billing:write ]
                            │
              (Intersect with User Role: Sales AE)
                            ▼
[ Resulting Scopes: contacts:read (billing:write stripped) ]
```

### Flow Steps:
1.  **Token Request**: A client requests a token with scopes `contacts:read` and `billing:write`.
2.  **Role Lookup**: The Auth Server checks the client's role (`Sales AE`).
3.  **Scope Validation**: The Auth Server checks if the requested scopes are allowed for that role.
4.  **Token Issuance**: Since `billing:write` is denied for `Sales AE`, the Auth Server strips that scope and issues a token containing only `contacts:read`.
