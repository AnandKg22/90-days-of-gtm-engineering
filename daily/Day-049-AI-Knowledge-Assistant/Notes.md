# Study Notes - Day 049: AI Knowledge Assistants (RAG & Search)

Today's studies focused on Retrieval-Augmented Generation (RAG) architectures, text chunking strategies, tokenization, vector space modeling, cosine similarity search, and source attribution.

---

## 1. Retrieval-Augmented Generation (RAG)

**RAG** is a design pattern that extends an LLM's capabilities by fetching relevant context from external databases before generating a response:

```
[User Query] ──> [Vector Search (Retrieval)] ──> [Inject Context into Prompt] ──> [LLM Generation] ──> [Answer + Citations]
```

### Why RAG?
*   **Accuracy**: Prevents hallucinations by forcing the LLM to base its answers on retrieved facts.
*   **Up-to-Date**: Avoids the need to retrain models for every new document; simply update the database index.
*   **Auditability**: Provides clear source citations, allowing users to verify outputs.

---

## 2. Text Chunking Strategies

Raw documents are too long to fit in a model's context window or make vector matching difficult. We split documents into **Chunks**:

### Chunking Strategies:
1.  **Fixed-size Chunking**: Split text at a set character or token count (e.g., 200 tokens). Can cut sentences in half.
2.  **Sliding Window (Overlap)**: Split text into fixed sizes with an overlap (e.g., 200 tokens with 40 overlapping tokens). Ensures context isn't lost at chunk boundaries.
3.  **Semantic/Sentence Chunking**: Split text at sentence boundaries or paragraph markers. Preserves semantic meaning but results in variable chunk sizes.

---

## 3. Vector Space Search & Cosine Similarity

To perform semantic searches, documents and queries are converted into term vectors:

### 1. Vector Representation
Text is tokenized, stop words are removed, and a term-frequency vector is built for each chunk.

### 2. Cosine Similarity Formula
Measures the cosine of the angle between two vectors, indicating directional alignment (range: 0.0 to 1.0):

$$\text{similarity}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

### 3. Fallback Threshold Gates
If the cosine similarity of the top match is below a threshold (e.g., $< 0.15$), the query is flagged as out-of-domain. This prevents retrieving unrelated GTM documents for queries about cooking, weather, or sports.
