# GTM Architecture - Day 008: CRM Entity Relationship Diagram

This document contains the Entity Relationship Diagram (ERD) mapping CRM tables, custom fields, and key relations.

---

## 🗄️ CRM Schema Entity Relationship Diagram (ERD)

The diagram below details how Contacts, Companies, Deals, and Activities are linked via relational database foreign keys:

```mermaid
erDiagram
    COMPANIES {
        int id PK
        varchar crm_company_id UK
        varchar name
        varchar domain UK
        int employee_count
    }

    CONTACTS {
        int id PK
        varchar crm_contact_id UK
        int company_id FK
        varchar first_name
        varchar last_name
        varchar email UK
    }

    DEALS {
        int id PK
        varchar crm_deal_id UK
        int company_id FK
        varchar name
        numeric amount
        varchar stage
    }

    CONTACTS_DEALS {
        int contact_id PK, FK
        int deal_id PK, FK
        varchar role
    }

    ACTIVITIES {
        int id PK
        int contact_id FK
        varchar type
        varchar subject
        timestamp logged_at
    }

    COMPANIES ||--o{ CONTACTS : "has"
    COMPANIES ||--o{ DEALS : "contains"
    CONTACTS ||--o{ CONTACTS_DEALS : "associated_with"
    DEALS ||--o{ CONTACTS_DEALS : "associated_with"
    CONTACTS ||--o{ ACTIVITIES : "performs"
```

---

## ⚙️ Relationship Cardinality Definitions

*   **Companies to Contacts (One-to-Many)**: A Company record can contain multiple related contacts (e.g. `AMET University` links to Anil, Ravi, and Sunil).
*   **Companies to Deals (One-to-Many)**: A single organization account can have multiple deals open over time (e.g., first license purchase, followed by an expansion deal).
*   **Contacts to Deals (Many-to-Many)**: Resolved via the junction table `CONTACTS_DEALS`. It links multiple buying committee members (such as Champions, Economic Buyers, and Technical Evaluators) to a single deal.
