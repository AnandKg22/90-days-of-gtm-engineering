# Retrieval-Augmented Generation (RAG) & Vector Stores

To answer questions about product features, pricing, or security compliance dynamically during sales, AI systems need access to internal documentation. This is accomplished via RAG.

---

## 1. RAG Processing Pipeline

```
[Doc PDF/Word] ──> [Text Chunking] ──> [Embedding Model] ──> [Vector DB (pgvector)]
                                                                  ▲
[User Search Query] ──> [Query Embedding] ──> [Cosine Similarity Search] 
```

1.  **Chunking**: Break documents down into manageable text chunks.
2.  **Embeddings**: Convert text chunks into numerical vectors using models (e.g. OpenAI `text-embedding-3-small`).
3.  **Vector Store**: Store vectors in PostgreSQL using `pgvector`.
4.  **Retrieval**: Convert search queries to vectors, query the store for the closest match, and feed that context to the LLM.

---

## 2. PostgreSQL `pgvector` Schema & Queries

Below is the DDL to create a vector store inside a Postgres instance:

```sql
-- 1. Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Create chunks table
CREATE TABLE document_chunks (
    id SERIAL PRIMARY KEY,
    document_name VARCHAR(255) NOT NULL,
    chunk_index INT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536) -- size matches OpenAI embedding dimensions
);

-- 3. Create HNSW Index for rapid search at scale
CREATE INDEX idx_chunks_embedding ON document_chunks 
USING hnsw (embedding vector_cosine_ops);
```

### Similarity Query (Cosine Distance)

```sql
-- Select top 3 chunks closest to a query embedding
SELECT document_name, chunk_index, content, 
       1 - (embedding <=> :query_vector) AS similarity_score
FROM document_chunks
WHERE 1 - (embedding <=> :query_vector) > 0.75
ORDER BY embedding <=> :query_vector
LIMIT 3;
```
*Note: `<=>` computes cosine distance. `1 - distance` converts it to cosine similarity.*

---

## 3. Python Embedding & Retrieval Code

```python
import numpy as np
from openai import OpenAI

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[text]
    )
    return response.data[0].embedding

# Example documents
documents = [
    "Our enterprise plan costs $499/month and includes unlimited SSO integrations.",
    "Our basic plan costs $49/month and includes 5 team seats with 2GB storage.",
    "For HIPAA compliance options, contact sales for dedicated VPS pricing."
]

# Simple semantic search search (in-memory mock)
def search_docs(query_text):
    query_vector = np.array(get_embedding(query_text))
    
    # Store documents and mock vector database
    db_embeddings = [np.array(get_embedding(doc)) for doc in documents]
    
    # Calculate cosine similarity manually: dot(A, B) / (norm(A)*norm(B))
    scores = []
    for doc, doc_vector in zip(documents, db_embeddings):
        similarity = np.dot(query_vector, doc_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(doc_vector))
        scores.append((doc, similarity))
        
    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores

print("Best match:", search_docs("How much is the enterprise plan with SSO?")[0])
```
