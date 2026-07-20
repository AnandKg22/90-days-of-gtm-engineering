# Exercises - Day 008: Relational CRM Schema Design

This document details the relational database schema structure designed for a custom CRM replica, including tables, columns, constraints, and relationships.

---

## 🗄️ Relational Database Schema Design

To mirror data from CRM platforms (HubSpot/Salesforce), we design the following PostgreSQL structure:

### 1. Companies Table
Tracks organizational accounts.
*   `id`: INT (Primary Key, Auto-Increment)
*   `crm_company_id`: VARCHAR(100) (Unique, HubSpot/SF Company ID)
*   `name`: VARCHAR(255) (Not Null)
*   `domain`: VARCHAR(255) (Unique Index for fast lookups)
*   `employee_count`: INT
*   `annual_revenue`: NUMERIC(15, 2)

### 2. Contacts Table
Tracks individual records (1:N relationship with Companies).
*   `id`: INT (Primary Key)
*   `crm_contact_id`: VARCHAR(100) (Unique)
*   `company_id`: INT (Foreign Key referencing `companies.id` ON DELETE SET NULL)
*   `first_name`: VARCHAR(100)
*   `last_name`: VARCHAR(100)
*   `email`: VARCHAR(255) (Unique, Not Null)
*   `phone`: VARCHAR(50)

### 3. Deals Table
Tracks commercial opportunities (1:N relationship with Companies).
*   `id`: INT (Primary Key)
*   `crm_deal_id`: VARCHAR(100) (Unique)
*   `company_id`: INT (Foreign Key referencing `companies.id` ON DELETE CASCADE)
*   `name`: VARCHAR(255) (Not Null)
*   `amount`: NUMERIC(15, 2)
*   `stage`: VARCHAR(100) (Not Null, e.g. "Proposal Sent")
*   `close_date`: DATE

### 4. Contacts-Deals Association Table (Many-to-Many)
Resolves N:M links between contacts and deals.
*   `contact_id`: INT (Foreign Key referencing `contacts.id` ON DELETE CASCADE)
*   `deal_id`: INT (Foreign Key referencing `deals.id` ON DELETE CASCADE)
*   `role`: VARCHAR(50) (e.g. "Primary Buyer", "Technical Evaluation", "Blocker")
*   *Constraint*: Composite Primary Key (`contact_id`, `deal_id`)

### 5. Activities Table
Logs touchpoints (1:N with Contacts and Deals).
*   `id`: INT (Primary Key)
*   `contact_id`: INT (Foreign Key referencing `contacts.id` ON DELETE CASCADE)
*   `deal_id`: INT (Foreign Key referencing `deals.id` ON DELETE SET NULL)
*   `type`: VARCHAR(50) (e.g. "Email", "Call", "Meeting")
*   `subject`: VARCHAR(255)
*   `logged_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP