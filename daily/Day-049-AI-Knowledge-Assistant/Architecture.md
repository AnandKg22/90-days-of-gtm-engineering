# GTM Architecture - Day 049: AI Knowledge Assistant

This document details the RAG architecture, sliding window text splitters, and vector similarity calculators supporting document retrieval.

---

## 🔄 RAG Indexing & Retrieval Pipelines

The diagrams below outline the indexing pipeline (offline document ingestion) and the retrieval pipeline (live query search):

### 1. Ingestion & Indexing Pipeline (Offline)
```mermaid
graph TD
    Docs[(Raw Document Files)] -->|1. Load| Loader[Document Ingestor]
    Loader -->|2. Split Text| Splitter[Sliding Window Chunker]
    
    subgraph Chunk Processing
        Splitter -->|Size: 150, Overlap: 30| C1[Chunk 1 + Metadata]
        Splitter -->|Size: 150, Overlap: 30| C2[Chunk 2 + Metadata]
    end
    
    C1 -->|3. Tokenize & Clean| Indexer[Term Vector Indexer]
    C2 -->|3. Tokenize & Clean| Indexer
    Indexer -->|4. Store Vectors| VectorDB[(Local Vector Store)]
```

### 2. Query & Retrieval Pipeline (Live)
```mermaid
graph TD
    Query[User Query String] -->|1. Parse| Tokenizer[Query Tokenizer]
    Tokenizer -->|2. Build query vector| Search[Search Engine]
    VectorDB[(Local Vector Store)] -->|3. Load chunk vectors| Search
    
    Search -->|4. Calculate Cosine Similarity| Scorer[Scorer Engine]
    Scorer -->|5. Retrieve top 2 chunks| Ranker[Matches Selector]
    
    Ranker -->|6. Compile Text| Prompt[Prompt Synthesizer]
    Ranker -->|6. Map Sources| Attributor[Citations Builder]
    
    Prompt -->|7. Generate Answer| Output[Synthesized Response with Footnotes]
    Attributor -->|7. Generate Answer| Output
```

---

## ⚙️ Core Retrieval Components

1.  **Sliding Window Chunker**: Splits long documents into overlapping character/token blocks to prevent losing context at chunk boundaries.
2.  **Query Tokenizer**: Cleans input strings, filters out stop words, and builds term vectors.
3.  **Vector Store**: Database holding document chunks, metadata (source titles, chunk indices), and term-frequency vectors.
4.  **Cosine Similarity Scorer**: Calculates vector alignment angles, ranking chunks by relevance.
5.  **Prompt Synthesizer**: Combines retrieved chunks into a prompt template, forcing the LLM to base its answers on the provided context.
