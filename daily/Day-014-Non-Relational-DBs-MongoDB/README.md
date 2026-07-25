# Day 014: Non-Relational DBs (MongoDB)

## Objective
Understand NoSQL document store databases (JSON/BSON models), design denormalized schemas with nested arrays for clickstream activity logging, and build query filter and aggregation pipelines.

## Topics Covered
- JSON & BSON representations
- Collections & Documents
- Schema-less database advantages
- MongoDB queries & aggregations

## Subtopics (Developed in Notes)
- NoSQL Database Design (Denormalization)
- NoSQL Query Syntax (Filters & Projections)
- Document Query Optimization (Compound Indexes)

---

## 🛠️ Practical Exercise: MongoDB Document Schema Design

In this exercise, we designed a MongoDB document schema to log user profiles and activity clickstreams:
*   **Root Document Fields**: Store email, company name, employee counts, and location.
*   **Nested Array (`touchpoints`)**: Embeds chronological user page views (source, medium, timestamp, url) directly inside the lead document, bypassing SQL join requirements.
*   **Metadata Object (`integrations_metadata`)**: Stores dynamic Integration details (Stripe ID, Apollo tech tags) that can change format at any time.

*View complete document models and aggregation pipelines in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: NoSQL GTM Document Store

We built an executable Python document engine in [Code/mongo_gtm.py](Code/mongo_gtm.py):
*   Implements an in-memory `NoSQLDocumentStore` collection class.
*   Loads nested JSON-like records representing maritime academy click histories.
*   Executes array matching queries (filtering contacts who visited the `/pricing` page).
*   Runs aggregation pipelines summing total traffic hits across all leads.

*View project requirements in [Assignment.md](Assignment.md) and the system diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 14 Study Notes](Notes.md) — Document models, denormalization, and array indexing.
*   📝 [MongoDB Document Schema](Exercises.md) — JSON document models and aggregations.
*   📝 [NoSQL DB Spec](Assignment.md) — Project requirements.
*   📊 [Document Store Diagram](Architecture.md) — Telemetry flow and multikey indexes.
*   💻 [NoSQL Store Script](Code/mongo_gtm.py) — Executable JSON query engine.

---

## 📝 Notes & Reflection
*   **Key Insight**: Using document databases to store raw click events eliminates schema migration friction when new web tracking tools are added or removed.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
