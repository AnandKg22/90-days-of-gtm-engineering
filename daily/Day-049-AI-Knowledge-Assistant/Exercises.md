# Exercises - Day 049: Text Chunking & Cosine Similarity

This document details practical exercises on writing sliding window chunking functions, tokenizers, and cosine similarity calculators.

---

## 📋 Exercise 1: Sliding Window Text Chunking

### Goal:
Write a Python function that splits a long string of text into character chunks of size `chunk_size` with a sliding overlap window.

### Script Implementation:
```python
def chunk_document_text(text: str, chunk_size: int, overlap: int) -> list:
    chunks = []
    start = 0
    
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_slice = text[start:end].strip()
        chunks.append(chunk_slice)
        
        # Shift start point back by overlap
        start += (chunk_size - overlap)
        
    return chunks

# Test validation check:
doc_text = "The platform is fully SOC 2 Type II certified. All data in transit is encrypted using TLS 1.3."
res = chunk_document_text(doc_text, 50, 15)
for idx, c in enumerate(res):
    print(f"Chunk {idx}: '{c}'")
```

---

## ⚙️ Exercise 2: Pure Python Cosine Similarity

### Goal:
Write a term-frequency vectorizer and cosine similarity calculator without using external libraries (like NumPy or SciPy).

### Script Implementation:
```python
import math

def calculate_cosine_similarity(vec1: dict, vec2: dict) -> float:
    # 1. Intersection of terms
    common_terms = set(vec1.keys()) & set(vec2.keys())
    numerator = sum(vec1[x] * vec2[x] for x in common_terms)
    
    # 2. Magnitude of vectors
    magnitude_1 = sum(val ** 2 for val in vec1.values())
    magnitude_2 = sum(val ** 2 for val in vec2.values())
    denominator = math.sqrt(magnitude_1) * math.sqrt(magnitude_2)
    
    if not denominator:
        return 0.0
    return numerator / denominator

# Test check:
vector_a = {"soc": 1.0, "compliance": 1.0, "security": 1.0}
vector_b = {"security": 1.0, "compliance": 1.0}
sim = calculate_cosine_similarity(vector_a, vector_b)
print(f"Cosine Similarity: {sim:.3f}") # Expected: 0.816
```