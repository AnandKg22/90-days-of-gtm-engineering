# Project Assignment - Day 008: Mini CRM Database

This project requires creating a functional SQLite relational database that models a CRM data schema, seeds sample records, and runs SQL join queries to retrieve pipeline and contact reports.

---

## 🎯 Requirements

Your Python/SQLite application must:
1.  Initialize an in-memory SQLite database instance.
2.  Run DDL SQL commands to construct five related tables:
    *   `companies` (company metadata)
    *   `contacts` (individual records linked to companies)
    *   `deals` (sales opportunities linked to companies)
    *   `contacts_deals` (many-to-many link resolving buying roles)
    *   `activities` (touchpoint logs linked to contacts/deals)
3.  Seed mock CRM records representing shipping schools (Tolani Maritime, AMET, IMSGOA), their staff contacts, active deals, and sales emails.
4.  Execute SQL `JOIN` queries to generate:
    *   A list of all contacts and their employer companies.
    *   A pipeline deal report showing company name, deal amount, and stage.
    *   An activity audit log showing contact names and logged actions.

---

## 💻 Deliverable Code

A complete, working database script has been created and placed in [Code/mini_crm.py](Code/mini_crm.py). It builds the schema, seeds the records, executes queries, and prints the reports to the console.