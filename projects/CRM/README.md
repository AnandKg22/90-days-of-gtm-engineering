# Day 008: CRM Fundamentals

## Objective
Understand CRM core databases structures (Contacts, Companies, Deals, Activities), design structured relational schemas, and build in-memory SQL engines to query B2B sales pipelines.

## Topics Covered
- CRM core databases
- Contact & Company objects
- Deal & Activity records
- Notes & Pipelines

## Subtopics (Developed in Notes)
- Object Relationships (Associations)
- Properties (Fields)
- Objects (Standard vs. Custom)
- CRM Automation (Workflows)

---

## 🛠️ Practical Exercise: CRM Relational Schema Design

In this exercise, we designed a robust relational schema for a CRM replica:
*   **Companies Table**: Tracks organizational profiles.
*   **Contacts Table**: Individuals linked to companies (1:N).
*   **Deals Table**: Open sales opportunities linked to companies (1:N).
*   **Contacts-Deals Table**: Junction table resolving Many-to-Many buying committee roles (e.g. Primary Buyer, Blocker).
*   **Activities Table**: Time-stamped logs of client communications (calls, emails, meetings).

*View complete schema outlines in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Mini CRM Database Engine

We built an executable Python/SQLite in-memory CRM engine in [Code/mini_crm.py](Code/mini_crm.py):
*   Executes SQL DDL queries to construct the five CRM relational tables.
*   Seeds records representing shipping schools (AMET University, Tolani Maritime, IMSGOA), their staff contacts, deals, and communication history.
*   Executes complex SQL `JOIN` queries to generate Pipeline Deal reports, Contact lists, and Activity logs directly to the console.

*View project requirements in [Assignment.md](Assignment.md) and the entity relationship diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 8 Study Notes](Notes.md) — CRM objects definitions and relationship cardinalities.
*   📝 [CRM Schema Spec](Exercises.md) — Relational table designs.
*   📝 [Mini CRM Spec](Assignment.md) — SQL project requirements.
*   📊 [CRM ERD Diagram](Architecture.md) — Entity relationship schema.
*   💻 [Mini CRM Engine Script](Code/mini_crm.py) — Executable SQLite database replica.

---

## 📝 Notes & Reflection
*   **Key Insight**: Mirroring CRM records into a local SQL replica allows sales operations teams to run complex cohort analyses and data cleansing queries that are slow or impossible inside Salesforce/HubSpot UI.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).

---

## 👤 Author & Connect

Developed by **Anand Kumar** — Go-To-Market Architect & Revenue Engineer.
*   **Website**: [akstack.com](https://akstack.com)
*   **GitHub**: [github.com/AnandKg22](https://github.com/AnandKg22)
*   **LinkedIn**: [linkedin.com/in/anandkg22](https://www.linkedin.com/in/anandkg22/)
