# Reflection - Day 049: AI Knowledge Assistant

A personal log reflecting on the learning outcomes and concepts mastered on Day 49.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Semantic search matches context**: Unlike basic keyword searches, vector-based term matching calculates the angle between query and document vectors, allowing the engine to identify conceptually related documents.
2.  **Overlapping chunks preserve context**: Fixed-size text splitting can cut sentences or parameters in half. Implementing a sliding window chunking strategy ensures key details are retained.
3.  **Source attributions build user trust**: Returning chunk indices, document IDs, and match similarity percentages allows users to verify answers against the source documentation.
4.  **Retrieval gates prevent hallucinations**: Out-of-domain queries (like "How do I cook a pepperoni pizza?") can match GTM docs with low similarity scores (e.g. 9.9%). Setting a minimum similarity threshold (e.g. $\ge 15\%$) prevents the engine from returning irrelevant results.

---

## 💻 Script Verification

I ran the `Code/knowledge_bot.py` script to test sliding window chunking, TF vectorizing, and similarity retrieval:
*   **Security Query ("Is the platform SOC 2 certified?")**:
    *   *Result*: Located `doc_sec_001` (Security Policy) chunks.
    *   *Attribution*: Mapped Chunk 0 (53.5% similarity) and Chunk 1 (33.3% similarity) directly to the source.
*   **Pricing Query ("What are the pricing rates for Enterprise contracts?")**:
    *   *Result*: Located `doc_sec_001` Chunk 2 (VPC details, 34.1% similarity) and `doc_bill_003` Chunk 2 (Enterprise baseline pricing $95k, 18.3% similarity).
*   **Out-of-Domain Query ("How do I cook a pepperoni pizza?")**:
    *   *Result*: Returned a Salesforce Integration Guide match with a low similarity score of **9.9%**.
    *   *Improvement Plan*: In production, implement a minimum similarity filter of $15\%$ to reject this query as out-of-domain, rather than returning irrelevant GTM documents.
*   **Insight**: This verifies how RAG search engines index text, calculate cosine similarity, and attribute sources.

---

## 🎯 Plan for Tomorrow

Tomorrow is Day 50: **AI Call Analysis**. I will complete the transition into advanced conversational analytics, constructing an agent that parses sales call transcripts to extract buyer sentiment, track competitor mentions, and identify follow-up action items.
