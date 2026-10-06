# Cheat Sheet - AI Knowledge Assistant

This cheat sheet compiles RAG terminology, similarity math, and vector database connection templates.

---

## 1. Key Terminology

*   **RAG (Retrieval-Augmented Generation)**: Fetching relevant documents to supply context to an LLM prompt.
*   **Vector Embeddings**: Numerical arrays representing the semantic meaning of words, sentences, or documents.
*   **Cosine Similarity**: Measures the directional similarity between two vectors (independent of magnitude).
*   **Stop Words**: Common words (the, a, and, to) filtered out during tokenization to improve match accuracy.
*   **Chunk Overlap**: Shared text between consecutive chunks to preserve context at boundaries.

---

## 2. Cosine Similarity Formula (Math & NumPy)

$$\text{Similarity}(A, B) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|}$$

### Python NumPy Implementation:
```python
import numpy as np

def cosine_similarity_numpy(a: np.ndarray, b: np.ndarray) -> float:
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(dot_product / (norm_a * norm_b))
```

---

## 3. PGVector Connection Template (PostgreSQL)

To store vector embeddings directly in PostgreSQL, use the `pgvector` extension:

### SQL Schema:
```sql
-- Enable vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table with 1536-dimensional embeddings (OpenAI standard)
CREATE TABLE documentation_chunks (
    id SERIAL PRIMARY KEY,
    doc_title VARCHAR(255) NOT NULL,
    chunk_index INT NOT NULL,
    content TEXT NOT NULL,
    embedding vector(1536)
);

-- Query using Cosine Distance operator (<=>)
SELECT content, 1 - (embedding <=> '[0.012, -0.043, ...]') AS similarity
FROM documentation_chunks
ORDER BY similarity DESC
LIMIT 3;
```
---

## 4. ChromaDB Connection Template (Python)
```python
import chromadb

# Initialize local vector database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("gtm_docs")

# Add documents
collection.add(
    documents=["Fully SOC 2 Type II certified. Encryption via AES-256."],
    metadatas=[{"source": "security_policy"}],
    ids=["chunk_id_001"]
)

# Query
results = collection.query(
    query_texts=["Is data encrypted?"],
    n_results=1
)
print(results["documents"])
```
