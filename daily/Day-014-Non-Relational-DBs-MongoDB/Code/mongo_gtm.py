# NoSQL Document Store Simulator
import json
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class NoSQLDocumentStore:
    def __init__(self):
        self.collection: List[Dict[str, Any]] = []
        
    def insert_one(self, document: Dict[str, Any]):
        self.collection.append(document)
        
    def find_leads_by_page_view(self, target_url: str) -> List[Dict[str, Any]]:
        results = []
        for doc in self.collection:
            # Check if any touchpoint has the target URL
            touchpoints = doc.get("touchpoints", [])
            for tp in touchpoints:
                if tp.get("url") == target_url:
                    results.append({
                        "email": doc.get("email"),
                        "company_name": doc.get("company_name")
                    })
                    break # Match found for this doc
        return results
        
    def aggregate_total_page_views(self) -> int:
        total = 0
        for doc in self.collection:
            total += len(doc.get("touchpoints", []))
        return total

# Mock GTM Document Dataset (NoSQL nested structures)
mock_leads_data = [
    {
        "email": "dean@imsgoa.org",
        "company_name": "IMSGOA Maritime College",
        "employee_count": 85,
        "touchpoints": [
            {"source": "google", "medium": "cpc", "url": "/features"},
            {"source": "newsletter", "medium": "email", "url": "/pricing"}
        ]
    },
    {
        "email": "registrar@ametuniv.edu.in",
        "company_name": "AMET University",
        "employee_count": 250,
        "touchpoints": [
            {"source": "direct", "medium": "none", "url": "/home"},
            {"source": "direct", "medium": "none", "url": "/pricing"},
            {"source": "direct", "medium": "none", "url": "/checkout"}
        ]
    },
    {
        "email": "sharma.r@tolani.edu",
        "company_name": "Tolani Maritime Institute",
        "employee_count": 120,
        "touchpoints": [
            {"source": "google", "medium": "cpc", "url": "/features"}
        ]
    }
]

if __name__ == "__main__":
    store = NoSQLDocumentStore()
    
    # 1. Insert documents
    for doc in mock_leads_data:
        store.insert_one(doc)
        
    print("=" * 65)
    print("             VIVAEXAMS NoSQL DOCUMENT ENGINE")
    print("=" * 65)
    print(f"Total Documents Loaded: {len(store.collection)}")
    print("-" * 65)
    
    # 2. Run nested array query
    target = "/pricing"
    print(f"[QUERY] FINDING ACCOUNTS THAT VISITED: {target}")
    matching_accounts = store.find_leads_by_page_view(target)
    for acc in matching_accounts:
        print(f"  - Lead: {acc['email']} ({acc['company_name']})")
    print("-" * 65)
    
    # 3. Run aggregation query
    total_views = store.aggregate_total_page_views()
    print("[AGGREGATION] TOTAL CLICKSTREAM TRAFFIC VOLUME")
    print(f"  Sum of all touchpoint hits: {total_views} Page Views")
    print("=" * 65)
