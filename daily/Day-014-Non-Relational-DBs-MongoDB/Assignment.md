# Project Assignment - Day 014: NoSQL GTM Document Store

This project requires developing a Python document store simulation that acts as an in-memory NoSQL database, loading nested JSON records, running array filter queries, and generating traffic aggregations.

---

## 🎯 Requirements

Your Python simulation must:
1.  Create a `NoSQLDocumentStore` class to hold database documents.
2.  Insert nested JSON-like dictionary records containing:
    *   `email`, `company_name`, `employee_count`
    *   `touchpoints` (nested array of objects containing: `source`, `medium`, `url`)
3.  Implement query methods to:
    *   **Find by nested array value**: Query and return email addresses of users who visited the `url` value `/pricing`.
    *   **Aggregate page views**: Sum the total count of page views logged across all leads in the database.
4.  Print a clean console log showing query matching results and traffic volume stats.

---

## 💻 Deliverable Code

A complete, working database simulator has been created and placed in [Code/mongo_gtm.py](Code/mongo_gtm.py). It builds the NoSQL store, runs nested query filters, aggregates metrics, and prints the reports to the console.
