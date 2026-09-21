# Cheat Sheet - AI Research Agents

This cheat sheet compiles web crawling commands, regex pattern lists, and extraction snippets for GTM research.

---

## 1. BeautifulSoup Selection Guide (Python)

### Initialize parser
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
```

### Common Elements Queries
```python
# 1. Get Page Title
title = soup.title.string if soup.title else ""

# 2. Get Meta Description
meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
description = meta_desc_tag['content'] if meta_desc_tag else ""

# 3. Find all links (URLs)
links = [a['href'] for a in soup.find_all('a', href=True)]

# 4. Search for scripts (e.g. HubSpot tracking)
scripts = [s['src'] for s in soup.find_all('script', src=True)]
has_hubspot = any('hs-scripts' in src for src in scripts)
```

---

## 2. GTM Regular Expression Patterns

| Target Data | Regular Expression Pattern | Description |
| :--- | :--- | :--- |
| **Email Address** | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Standard email search |
| **Meta Description** | `<meta name="description" content="(.*?)"` | Extract content attribute |
| **Google Analytics** | `UA-\d+-\d+` or `G-[A-Z0-9]+` | Detect Google tags |
| **Pricing values** | `\$\d+(?:,\d{3})*(?:\.\d{2})?` | Detect dollar pricing strings |

---

## 3. Python HTTP Request Boilerplate
When crawling, always include a custom `User-Agent` header and set a strict `timeout` threshold to avoid hanging threads:
```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 GTMRecon/1.0"
}

try:
    response = requests.get("https://stripe.com", headers=headers, timeout=5.0)
    html = response.text
except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print(f"Network error: {str(e)}")
```
---

## 4. Confidence Score Formula
```python
def calculate_confidence(facts):
    score = 0
    if facts.get("description"): score += 25
    if facts.get("tech_stack"): score += 25
    if facts.get("pricing"): score += 25
    if facts.get("competitors"): score += 25
    return score
```
