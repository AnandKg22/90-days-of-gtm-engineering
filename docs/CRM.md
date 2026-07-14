# CRM Concepts, Data Modeling & Architecture

A CRM (Customer Relationship System) is the source of truth for all business operations. This guide covers relational modeling, HubSpot vs Salesforce architectures, and standard CRM replica design.

---

## 1. Relational Data Modeling in CRMs

A standard CRM uses a highly relational schema structured around core Entity types (Objects):

```
       ┌───────────────┐
       │   COMPANIES   │
       └───────┬───────┘
               │ 1:N
       ┌───────┴───────┐
       │   CONTACTS    ├──────────────┐
       └───────┬───────┘              │
               │ N:M (Associations)   │ 1:N
       ┌───────┴───────┐       ┌──────┴──────┐
       │     DEALS     │       │  ACTIVITIES │
       └───────────────┘       └─────────────┘
```

*   **Contacts**: Individual people (email, phone, job title).
*   **Companies**: Business organizations (domain, industry, location, size).
*   **Deals / Opportunities**: Sales pipelines tracking revenue amounts and deal stages.
*   **Activities / Tasks**: Interactions (emails sent, meetings booked, calls, notes).
*   **Associations**: The link tables connecting these objects (e.g. Contact "John" works at Company "Acme" and is associated with Deal "Acme Enterprise License").

---

## 2. HubSpot vs. Salesforce Architectures

| Dimension | HubSpot Architecture | Salesforce Architecture |
| :--- | :--- | :--- |
| **Data Engine** | Multi-tenant Elasticsearch + relational. Highly flexible custom properties. | Multi-tenant relational (Oracle/Postgres custom stack). Strict database tables. |
| **Object Model** | Standard Objects (Contacts, Companies, Deals, Tickets) + Custom Objects. | Standard Objects (Lead, Account, Contact, Opportunity, Case) + Custom Objects. |
| **Customization** | Standard property creation via UI or API. Easy associations. | Heavy schema custom fields (Suffix `__c` for custom objects/fields, e.g. `Custom_Field__c`). |
| **Automation** | Event-based workflows, easy n8n/Zapier triggers. | Apex code, Flow Builder, Process Builder (heavy and complex). |
| **APIs** | Simple REST API with token/OAuth. | SOQL (Salesforce Object Query Language), Composite APIs, Bulk APIs. |

---

## 3. PostgreSQL CRM Replica Schema (DDL)

To build automations, we often mirror CRM data to an internal PostgreSQL database. Below is a production-ready CRM schema design:

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. COMPANIES TABLE
CREATE TABLE companies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    crm_company_id VARCHAR(100) UNIQUE, -- ID from HubSpot/Salesforce
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255),
    industry VARCHAR(100),
    employee_count INT,
    annual_revenue NUMERIC(15, 2),
    country VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. CONTACTS TABLE
CREATE TABLE contacts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    crm_contact_id VARCHAR(100) UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    job_title VARCHAR(150),
    company_id UUID REFERENCES companies(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. DEALS TABLE
CREATE TABLE deals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    crm_deal_id VARCHAR(100) UNIQUE,
    name VARCHAR(255) NOT NULL,
    amount NUMERIC(15, 2),
    stage VARCHAR(100) NOT NULL, -- e.g., Qualification, Proposal, Won, Lost
    close_date DATE,
    company_id UUID REFERENCES companies(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. CONTACTS-DEALS ASSOCIATION TABLE (Many-to-Many)
CREATE TABLE contacts_deals (
    contact_id UUID REFERENCES contacts(id) ON DELETE CASCADE,
    deal_id UUID REFERENCES deals(id) ON DELETE CASCADE,
    association_type VARCHAR(50) DEFAULT 'influence', -- e.g. Primary Buyer, Blocker, Influencer
    PRIMARY KEY (contact_id, deal_id)
);

-- 5. ACTIVITIES TABLE
CREATE TABLE activities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    crm_activity_id VARCHAR(100) UNIQUE,
    type VARCHAR(50) NOT NULL, -- e.g., Email, Meeting, Call, Note
    subject VARCHAR(255),
    body TEXT,
    contact_id UUID REFERENCES contacts(id) ON DELETE SET NULL,
    deal_id UUID REFERENCES deals(id) ON DELETE SET NULL,
    activity_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- INDEXES FOR HIGH-PERFORMANCE QUEUES
CREATE INDEX idx_contacts_email ON contacts(email);
CREATE INDEX idx_deals_stage ON deals(stage);
CREATE INDEX idx_companies_domain ON companies(domain);
```
