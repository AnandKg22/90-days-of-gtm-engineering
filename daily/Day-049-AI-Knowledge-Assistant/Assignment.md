# Project Assignment - Day 049: Internal Knowledge Bot

This project requires developing a Python Internal Knowledge Bot. It processes corporate documentation, implements sliding window chunking, indexes term frequency vectors, executes semantic vector space queries, and returns answers backed by citations.

---

## 🎯 Requirements

Your Knowledge Bot must:
1.  **Index Documents**:
    *   Accept a structured database containing document IDs, titles, and body content text.
2.  **Slide Window Chunking**:
    *   Split document bodies into overlapping chunks (e.g. size 150 characters, overlap 30), preserving document IDs and indices.
3.  **Tokenization & Stop Words Filtering**:
    *   Clean inputs and query terms, removing common stop words (e.g. the, and, our) to build clean term-frequency vectors.
4.  **Vector Similarity Search**:
    *   Calculate cosine similarity between query vectors and chunk vectors using pure Python math.
5.  **Compile Citations Footnotes**:
    *   Retrieve the top-2 matching chunks.
    *   Compile a response showing document sources, chunk indexes, and similarity percentages.

---

## 💻 Deliverable Code

A complete, working Internal Knowledge Bot has been created and is available in [Code/knowledge_bot.py](Code/knowledge_bot.py). It runs vector searches on security policies and billing guides, displaying results and attributions in the terminal.