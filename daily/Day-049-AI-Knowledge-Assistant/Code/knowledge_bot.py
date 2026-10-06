# Day 049: AI Knowledge Assistant - Internal Knowledge Bot
import sys
import math
import re
from typing import List, Dict, Any, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock Internal Knowledge Base (Product Documentation, Security, Billing Policies)
KNOWLEDGE_BASE = [
    {
        "doc_id": "doc_sec_001",
        "title": "GTM Revenue Automation Security Policy",
        "content": (
            "Our platform adheres to strict enterprise security standards. We are fully SOC 2 Type II certified. "
            "All data in transit is encrypted using TLS 1.3, and data at rest is encrypted via AES-256. "
            "To prevent data leakage, customer database contents are processed in memory and are never cached locally on our servers. "
            "Dedicated VPC endpoints are available for Enterprise tier clients."
        )
    },
    {
        "doc_id": "doc_api_002",
        "title": "Salesforce Integration Setup Guide",
        "content": (
            "To connect Salesforce, navigate to settings and select Integrations. Authorize using OAuth 2.0 credentials. "
            "Field mapping configurations determine how Lead stages map to Salesforce Contact statuses. "
            "We support automated bidirectional sync with HubSpot and Salesforce. "
            "Sync operations run every 60 seconds by default, with automatic retry queuing on timeout failures."
        )
    },
    {
        "doc_id": "doc_bill_003",
        "title": "SaaS Billing Tiers & Pricing Policies",
        "content": (
            "We support two contract pricing models. The Standard license is $45,000/year for Mid-Market accounts. "
            "The Enterprise license starts at $95,000/year, which includes custom integration support and dedicated technical CSMs. "
            "Standard implementation setup fees are $7,500 for Mid-Market and $15,000 for Enterprise. "
            "Discounts above 20.0% require VP of Sales approvals."
        )
    }
]

class Chunk:
    def __init__(self, doc_id: str, doc_title: str, text: str, chunk_index: int):
        self.doc_id = doc_id
        self.doc_title = doc_title
        self.text = text
        self.chunk_index = chunk_index

class KnowledgeBotEngine:
    def __init__(self, documents: List[Dict[str, str]]):
        self.documents = documents
        self.chunks: List[Chunk] = []
        self._build_chunks()

    def _build_chunks(self):
        """Splits raw documents into chunks using a sliding window strategy (character-based)."""
        chunk_size = 150 # approx character window
        overlap = 30     # overlap size
        
        for doc in self.documents:
            text = doc["content"]
            doc_id = doc["doc_id"]
            title = doc["title"]
            
            start = 0
            chunk_idx = 0
            while start < len(text):
                end = min(start + chunk_size, len(text))
                chunk_text = text[start:end].strip()
                self.chunks.append(Chunk(doc_id, title, chunk_text, chunk_idx))
                
                # Move start point back by overlap
                start += (chunk_size - overlap)
                chunk_idx += 1

    def _tokenize(self, text: str) -> List[str]:
        """Cleans and tokenizes text into lower-case alphanumeric words."""
        words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
        # Filter out common stop words
        stop_words = {"our", "we", "all", "is", "and", "to", "the", "in", "a", "for", "with", "at", "by", "on"}
        return [w for w in words if w not in stop_words]

    def _compute_cosine_similarity(self, vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
        """Calculates cosine similarity between two term-frequency vectors."""
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum(vec1[x] * vec2[x] for x in intersection)
        
        sum1 = sum(val ** 2 for val in vec1.values())
        sum2 = sum(val ** 2 for val in vec2.values())
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        
        if not denominator:
            return 0.0
        return numerator / denominator

    def search(self, query: str, top_n: int = 2) -> List[Tuple[Chunk, float]]:
        """Executes a semantic vector space search over document chunks using TF vectors."""
        query_tokens = self._tokenize(query)
        # Build query vector
        query_vec = {}
        for token in query_tokens:
            query_vec[token] = query_vec.get(token, 0.0) + 1.0
            
        results = []
        for chunk in self.chunks:
            chunk_tokens = self._tokenize(chunk.text)
            # Build chunk vector
            chunk_vec = {}
            for token in chunk_tokens:
                chunk_vec[token] = chunk_vec.get(token, 0.0) + 1.0
                
            sim = self._compute_cosine_similarity(query_vec, chunk_vec)
            if sim > 0:
                results.append((chunk, sim))
                
        # Sort by similarity descending
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_n]

    def query(self, user_query: str) -> str:
        """Processes the query, retrieves matching chunks, and generates a structured answer with source citations."""
        print(f"[*] Processing user query: \"{user_query}\"...")
        matches = self.search(user_query, top_n=2)
        
        if not matches:
            return (
                "========================================================================\n"
                "               KNOWLEDGE ASSISTANT RESPONSE\n"
                "========================================================================\n"
                " Sorry, I could not find any relevant documentation in the knowledge base.\n"
                "========================================================================"
            )

        # Build answer and citations
        answer_text = ""
        citation_block = "\n SOURCE ATTRIBUTIONS:\n"
        
        for idx, (chunk, score) in enumerate(matches):
            cit_num = idx + 1
            # Build synthesized answer paragraph
            answer_text += f"... {chunk.text} ... "
            # Build citation reference
            citation_block += (
                f"   [{cit_num}] Document: '{chunk.doc_title}' (ID: {chunk.doc_id}) "
                f"| Chunk index: {chunk.chunk_index} | Match Similarity: {score * 100:.1f}%\n"
            )

        # Render report
        response = (
            f"========================================================================\n"
            f"               KNOWLEDGE ASSISTANT ANSWER\n"
            f"========================================================================\n"
            f" Query: \"{user_query}\"\n\n"
            f" Answer:\n"
            f"   Based on our internal product documentation:\n"
            f"   {answer_text}\n"
            f"{citation_block}"
            f"========================================================================"
        )
        return response


if __name__ == "__main__":
    bot = KnowledgeBotEngine(KNOWLEDGE_BASE)

    # Test Query 1: Security compliance
    print("=" * 72)
    print("                 AI KNOWLEDGE ASSISTANT ENGINE")
    print("=" * 72)
    
    ans1 = bot.query("Is the platform SOC 2 certified and data encrypted?")
    print(ans1)
    print("\n\n")

    # Test Query 2: Pricing rules
    ans2 = bot.query("What are the pricing rates for Enterprise contracts?")
    print(ans2)
    print("\n\n")

    # Test Query 3: Out-of-domain query
    ans3 = bot.query("How do I cook a pepperoni pizza?")
    print(ans3)
