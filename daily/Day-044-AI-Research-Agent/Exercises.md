# Exercises - Day 044: Web Scraping & Technographics

This document details practical exercises on writing Python scrapers to extract company metadata, tracking competitor mentions, and evaluating data confidence levels.

---

## 📋 Exercise 1: Scraping Technographics with BeautifulSoup

### Goal:
Write a Python script that parses a web page's HTML to check for the presence of common B2B marketing tools (Google Analytics, HubSpot, and Stripe).

### Script Implementation:
```python
from bs4 import BeautifulSoup

def audit_marketing_stack(html_content: str) -> dict:
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Look for tracking script URLs
    scripts = [s['src'] for s in soup.find_all('script', src=True)]
    
    results = {
        "hubspot_detected": any("hs-scripts" in src for src in scripts),
        "stripe_detected": any("js.stripe.com" in src for src in scripts),
        "google_analytics_detected": False
    }
    
    # 2. Check for GA Tracking ID in text/regex
    for s in soup.find_all('script'):
        if s.string and ("UA-" in s.string or "G-" in s.string):
            results["google_analytics_detected"] = True
            break
            
    return results
```

---

## ⚙️ Exercise 2: Mapping Competitor Mentions in PR Headlines

### Goal:
Write a python logic that scans a press release body for target competitor names to deduce the company's competitive positioning.

### Script Implementation:
```python
def map_competitors(news_text: str, target_competitors: list) -> list:
    detected = []
    text_lower = news_text.lower()
    
    for comp in target_competitors:
        if comp.lower() in text_lower:
            detected.append(comp)
            
    return detected

# Example usage:
pr_text = "Today Snowflake announced expanded table support, placing it in direct competition with Databricks lakehouses."
rivals = map_competitors(pr_text, ["Databricks", "Redshift", "Google BigQuery"])
# Output: ['Databricks']
```

---

## 📊 Exercise 3: Confidence Score Evaluation Matrix

Calculate the information confidence score for a crawled startup:
*   **Facts Found**: Title resolved, Description resolved, Tech stack (Next.js) resolved.
*   **Missing**: No pricing table detected on site; no competitor matches found.

### Calculation:
*   Description Meta: **+25%**
*   Tech stack: **+25%**
*   Pricing: **+0%** (missing)
*   Competitors: **+0%** (missing)

$$\text{Final Confidence Score} = 25\% + 25\% = 50\%$$

*   **Status**: *Medium confidence*. The record should be flagged for human review or enrichment validation (e.g. Crunchbase API) rather than running fully automated outbound emails.