# Study Notes - Day 044: AI Research Agents

Today's studies focused on building AI-driven web research crawlers, parsing raw HTML using BeautifulSoup and Regular Expressions, mapping citation coordinates, analyzing competitive positioning, and modeling data confidence scores.

---

## 1. Technographic & Firmographic Web Crawling

To enrich lead datasets before sales outreach, GTM engineers build scrapers that extract details from target company websites:

### HTML Extraction Targets:
*   **Homepage Title & Description**: Found in `<title>` and `<meta name="description" content="...">`. Contains the core value proposition of the company.
*   **Technographics (Meta Tags & Scripts)**:
    *   `<meta name="generator" content="...">` identifies frameworks (e.g. WordPress, Next.js).
    *   Searching script tags (`<script src="...">`) for endpoints like `js.hs-scripts.com` (HubSpot) or `js.stripe.com` (Stripe) identifies active software integrations.
*   **Pricing Elements**: Scraping page text for keywords like "per user", "credits", "Enterprise", or billing intervals ("yearly", "monthly").
*   **News & Competitors**: Crawling press rooms to identify product releases and industry competitors.

---

## 2. Citation Tracking (Preventing Hallucinations)

When LLMs summarize crawled websites, they risk introducing **hallucinations** (e.g. inventing a pricing tier or misstating the company's product). 

### Citation Pipelines:
To prevent this, the scraper maps every extracted fact to a specific source block:
1.  **Crawl Phase**: Download raw HTML pages.
2.  **Extraction Phase**: Parse facts (using regex or BeautifulSoup) and associate the raw text with a **Source URI/Tag** (e.g. `homepage.html -> <meta name="description">`).
3.  **Footnote Compilation**: Save findings as tuples containing the fact string and a citation index (e.g., `("React, Next.js", "Homepage Meta Tag")`).
4.  **Sales Verification**: Display these footnote citations in the SDR research drawer, allowing sales reps to verify details before reaching out.

---

## 3. Data Confidence Scoring

To ensure database quality, we run a **Confidence Scorer** that evaluates the completeness and reliability of gathered research:

$$\text{Confidence Score} = \text{Background Resolved} (25\%) + \text{Tech Resolved} (25\%) + \text{Pricing Resolved} (25\%) + \text{Rivals Resolved} (25\%)$$

### Scored Tiers:
*   **90% - 100% (High)**: Fully enriched record containing background description, tech stack, pricing details, and competitor mappings. Safe for automatic email personalization.
*   **50% - 80% (Medium)**: Partial details (e.g., background and tech stack found, but pricing unresolved). Requires human-in-the-loop review.
*   **< 50% (Low)**: Missing critical meta tags or domains returned errors. Flags record for manual enrichment.
