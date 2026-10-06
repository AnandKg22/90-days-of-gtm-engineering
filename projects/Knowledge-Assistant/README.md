# Day 049: AI Knowledge Assistant

## Objective
Design and build an internal **AI Knowledge Assistant** (Internal Knowledge Bot) that processes corporate documents, splits text using a sliding window chunking strategy, indexes term frequency vectors, executes semantic searches using cosine similarity, and returns citations.

## Topics Covered
- Internal Documentation Indexing: Processing FAQ, APIs, and security policy manuals.
- Sliding Window Chunking: Splitting documents into overlapping text blocks.
- Semantic Vector Search: Representing queries and documents in vector spaces.
- Vector Retrieval: Calculating Cosine Similarity scores.
- Source Attribution: Mapping findings to document IDs and chunk indexes.

## Subtopics (Developed in Notes)
- RAG (Retrieval-Augmented Generation) Architectures
- Chunking strategies (character vs word vs sentence boundary)
- Vector Embeddings and Indexing (Pinecone, ChromaDB, PGVector)
- Similarity Math (Cosine, Dot Product, Euclidean distance)
- Hallucination Control Gates (Confidence scoring thresholds)

---

## 🛠️ Practical Exercise: Indexing & Retrieval

In this exercise, we designed document parsing and vector matching pipelines:
*   **Tokenization & Cleaning**: Filtering out common stop words to build clean term-frequency vectors.
*   **Similarity Math**: Writing cosine similarity algorithms in Python.
*   **Threshold Gates**: Preventing out-of-domain queries (e.g. cooking pizzas) from returning irrelevant GTM document matches.

*View complete code snippets and text splitters in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Internal Knowledge Bot

We completed two primary deliverables:
1.  **AI Knowledge Bot**: An executable Python search engine in [Code/knowledge_bot.py](Code/knowledge_bot.py) that tokenizes documentation, indexes sliding window chunks, runs vector similarity checks, and compiles answers.
2.  **RAG Pipeline Layout**: System charts and schemas detailed in [Assignment.md](Assignment.md) and [Architecture.md](Architecture.md).

---

## 📂 Expected Deliverables
*   📝 [Day 49 Study Notes](Notes.md) — RAG systems, tokenization, embeddings, and vector databases.
*   📝 [Search Specs](Exercises.md) — Text splitters and similarity math.
*   📝 [Project Assignment Spec](Assignment.md) — Technical requirements for the Knowledge Bot.
*   📊 [RAG Architecture Flow](Architecture.md) — Mermaid pipeline charting document chunking and vector retrieval.
*   💻 [AI Knowledge Bot](Code/knowledge_bot.py) — Executable Python vector search engine.
*   📋 [Knowledge Cheat Sheet](CheatSheet.md) — Key terms, numpy similarity snippets, and chunking parameters.
*   🤖 [Knowledge Prompts](Prompts.md) — System prompts for RAG answer generation and threshold checks.
*   🔗 [Knowledge Resources](Resources.md) — Links to ChromaDB, Pinecone, Tiktoken, and LangChain.
*   📝 [Daily Reflection](Reflection.md) — Learnings, search verifications, and preview of Day 50.

---

## 📝 Notes & Reflection
*   **Key Insight**: Simple keyword searching misses context. Implementing a semantic search engine using term vectors and cosine similarity enables agents to locate relevant security and billing documentation, providing answers backed by source citations.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).

---

## 👤 Author & Connect

Developed by **Anand Kumar** — Go-To-Market Architect & Revenue Engineer.
*   **Website**: [akstack.com](https://akstack.com)
*   **GitHub**: [github.com/AnandKg22](https://github.com/AnandKg22)
*   **LinkedIn**: [linkedin.com/in/anandkg22](https://www.linkedin.com/in/anandkg22/)
