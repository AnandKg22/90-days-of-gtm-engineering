# Reflection - Day 014: Non-Relational DBs (MongoDB)

A personal log reflecting on the learning outcomes and concepts mastered on Day 14.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Denormalization simplifies clickstream retrieval**: In SQL, listing all of a user's page views requires joining a `contacts` table and an `activities` table. In MongoDB, embedding the `touchpoints` array directly inside the contact document allows us to retrieve the complete user history in a single, fast read operation.
2.  **NoSQL handles API schema changes effortlessly**: Webhook payloads from marketing platforms frequently add or remove properties. MongoDB's schema-less nature stores these changing attributes inside nested metadata sub-objects without requiring DDL migration scripts.
3.  **Array Indexing (Multikey indexes) is mandatory**: Searching nested lists (like checking if a user has visited `/pricing` inside the `touchpoints` array) becomes slow as lists grow. We must create multikey indexes on array keys to keep searches optimized.

---

## 💻 Script Verification

I ran the `Code/mongo_gtm.py` script to verify our NoSQL document store simulation.
*   **Result**: 
    *   Documents are successfully loaded into the collection.
    *   `Nested Array Query`: Successfully identifies leads who viewed the `/pricing` page (dean@imsgoa.org and registrar@ametuniv.edu.in).
    *   `Aggregation Query`: Correctly sums the total page views across all documents (6 Page Views).
*   **Insight**: This demonstrates how a document store simplifies event log data retrieval compared to writing complex SQL relational joins.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 15: **APIs & Webhooks**. I will focus on understanding HTTP methods (GET, POST, PUT, DELETE), headers, authentication tokens, status codes, and designing custom webhook receivers.
