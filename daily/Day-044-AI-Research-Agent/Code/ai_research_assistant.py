# Day 044: AI Company Research Assistant - Firmographic Scraper & Analyzer
import sys
import time
import re
from typing import Dict, Any, List, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock Web Server containing raw HTML pages for target research companies
MOCK_WEB_SERVER = {
    "stripe.com": {
        "homepage": """
            <html>
                <head>
                    <title>Stripe | Financial Infrastructure for the Internet</title>
                    <meta name="description" content="Stripe is a suite of APIs powering online payment processing and commerce solutions for internet businesses of all sizes.">
                    <meta name="generator" content="React, Next.js, Next-SEO">
                </head>
                <body>
                    <h1>Payments infrastructure for the internet</h1>
                    <p>Millions of businesses of all sizes—from startups to large enterprises—use Stripe's software and APIs to accept payments, send payouts, and manage their businesses online.</p>
                </body>
            </html>
        """,
        "pricing": """
            <html>
                <head><title>Stripe Pricing | Simple and Transparent</title></head>
                <body>
                    <h2>Pay as you go pricing</h2>
                    <div class="pricing-card">
                        <h3>Integrated Tier</h3>
                        <p class="price">2.9% + 30c per successful card charge</p>
                    </div>
                    <div class="pricing-card">
                        <h3>Custom Enterprise</h3>
                        <p>Volume discounts, multi-product pricing, and custom contract models.</p>
                    </div>
                </body>
            </html>
        """,
        "news": """
            <html>
                <head><title>Stripe Press Room | Latest News</title></head>
                <body>
                    <h2>Stripe launches billing automation tools for B2B platforms</h2>
                    <p>SAN FRANCISCO - July 2026. Stripe today announced the release of new automated revenue reconciliation and usage-based billing features to compete with specialized billing players like Maxio and Chargebee.</p>
                </body>
            </html>
        """
    },
    "snowflake.com": {
        "homepage": """
            <html>
                <head>
                    <title>Snowflake | AI Data Cloud Platform</title>
                    <meta name="description" content="Snowflake enables every organization to mobilize their data and execute AI workloads with the AI Data Cloud.">
                    <meta name="tech" content="Apache Iceberg, Kubernetes, Java, React, AWS">
                </head>
                <body>
                    <h1>Mobilize your Data, Apps, and AI workloads</h1>
                    <p>Snowflake's single, unified platform breaks down data silos, enabling businesses to query massive datasets with sub-second latency.</p>
                </body>
            </html>
        """,
        "pricing": """
            <html>
                <head><title>Snowflake Pricing | Consumption-Based</title></head>
                <body>
                    <h2>On-demand consumption pricing</h2>
                    <p>Pay only for the compute and storage resources you use. Storage starts at $23 per TB per month. Compute credits start at $2.00 per credit (Standard Tier).</p>
                </body>
            </html>
        """,
        "news": """
            <html>
                <head><title>Snowflake News & Press Releases</title></head>
                <body>
                    <h2>Snowflake announces deep integration with Apache Iceberg</h2>
                    <p>LAS VEGAS - June 2026. Snowflake announced expanded support for Iceberg tables, allowing customers to query external object stores directly. Databricks remains their primary rival in open format lakehouse spaces.</p>
                </body>
            </html>
        """
    }
}

class AICompanyResearchAssistant:
    def __init__(self, domain: str):
        self.domain = domain
        self.raw_pages = MOCK_WEB_SERVER.get(domain, {})
        self.citations: List[str] = []
        self.extracted_facts: Dict[str, Any] = {}

    def run_research_pipeline(self) -> str:
        """Executes crawlers, extracts facts, maps citations, scores confidence, and synthesizes report."""
        print(f"[*] Starting AI Research Pipeline for domain: '{self.domain}'...")
        time.sleep(0.5)

        if not self.raw_pages:
            return f"[ERROR] Crawl failed. Target domain '{self.domain}' was unreachable (404/DNS timeout)."

        # 1. CRAWL & EXTRACT INFORMATION
        self._extract_homepage_details()
        self._extract_pricing_details()
        self._extract_news_details()

        # 2. CALCULATE CONFIDENCE SCORE
        confidence_score, audit_factors = self.calculate_confidence()

        # 3. GENERATE POSITIONING & SYNTHESIS REPORT
        report = self.generate_dossier_report(confidence_score, audit_factors)
        return report

    def _add_citation(self, source: str, fact: str):
        citation_id = len(self.citations) + 1
        self.citations.append(f"[{citation_id}] Source: {source} -> '{fact}'")
        return citation_id

    def _extract_homepage_details(self):
        """Extracts background meta description and technographics from homepage HTML."""
        html = self.raw_pages.get("homepage", "")
        
        # Extract title
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else "Unknown Title"
        c_title = self._add_citation("Homepage &lt;title&gt; tag", title)
        
        # Extract description meta tag
        desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.IGNORECASE)
        desc = desc_match.group(1).strip() if desc_match else "Background description missing"
        c_desc = self._add_citation("Homepage Description Meta Tag", desc)
        
        # Extract technographics
        tech_match = re.search(r'<meta name="(generator|tech)" content="(.*?)"', html, re.IGNORECASE)
        tech_list = [t.strip() for t in tech_match.group(2).split(",")] if tech_match else []
        c_tech = self._add_citation("Homepage Generator/Tech Meta Tag", ", ".join(tech_list))

        self.extracted_facts["title"] = (title, c_title)
        self.extracted_facts["description"] = (desc, c_desc)
        self.extracted_facts["tech_stack"] = (tech_list, c_tech)

    def _extract_pricing_details(self):
        """Extracts pricing tables and estimates contract models."""
        html = self.raw_pages.get("pricing", "")
        
        # Scan for pricing values
        price_patterns = [
            (r"(\d+\.?\d*%\s*\+\s*\d+c)", "Transactional percentage pricing model"),
            (r"(\$\d+\.?\d* per credit)", "Consumption-based credit model"),
            (r"(Custom Enterprise)", "Custom enterprise contract negotiation tier")
        ]
        
        detected_pricing = []
        for pattern, desc in price_patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                cit_id = self._add_citation("Pricing Page HTML Scraping", f"Found pricing schema: {match.group(1)}")
                detected_pricing.append((match.group(1), desc, cit_id))
                
        self.extracted_facts["pricing"] = detected_pricing

    def _extract_news_details(self):
        """Extracts news announcements and competitor mentions."""
        html = self.raw_pages.get("news", "")
        
        # Extract headline
        headline_match = re.search(r"<h2>(.*?)</h2>", html, re.IGNORECASE)
        headline = headline_match.group(1).strip() if headline_match else "No recent headlines"
        c_head = self._add_citation("Press Release headline tag", headline)
        
        # Scan for competitor mentions
        competitors_list = ["Databricks", "Maxio", "Chargebee", "Adyen", "PayPal"]
        detected_competitors = []
        for comp in competitors_list:
            if comp.lower() in html.lower():
                c_comp = self._add_citation("Press Release competitor mention", f"Found rival: {comp}")
                detected_competitors.append((comp, c_comp))
                
        self.extracted_facts["headline"] = (headline, c_head)
        self.extracted_facts["competitors"] = detected_competitors

    def calculate_confidence(self) -> Tuple[float, List[str]]:
        """Calculates information confidence score (0 to 100) based on extraction coverage."""
        score = 0.0
        factors = []

        # 1. Background description resolved
        if self.extracted_facts.get("description") and "missing" not in self.extracted_facts["description"][0]:
            score += 25.0
            factors.append("Homepage Description Meta Resolved: +25%")
        else:
            factors.append("Homepage Description Missing: +0%")
            
        # 2. Technographics resolved
        tech = self.extracted_facts.get("tech_stack", ([], 0))[0]
        if tech:
            score += 25.0
            factors.append(f"Technographics Extracted successfully ({len(tech)} tech nodes): +25%")
        else:
            factors.append("Technographics Unavailable: +0%")
            
        # 3. Pricing models resolved
        pricing = self.extracted_facts.get("pricing", [])
        if pricing:
            score += 25.0
            factors.append(f"Pricing Schema Extracted successfully ({len(pricing)} points): +25%")
        else:
            factors.append("Pricing Data Unresolved: +0%")
            
        # 4. Press Release & Competitors resolved
        comps = self.extracted_facts.get("competitors", [])
        if comps:
            score += 25.0
            factors.append(f"Competitive Rivals Mapped successfully ({len(comps)} rivals): +25%")
        else:
            factors.append("Competitive Competitors Mapped: +0%")

        return score, factors

    def generate_dossier_report(self, confidence_score: float, audit_factors: List[str]) -> str:
        """Assembles research facts and citations into a formatted dossier."""
        title, c_title = self.extracted_facts["title"]
        desc, c_desc = self.extracted_facts["description"]
        tech, c_tech = self.extracted_facts["tech_stack"]
        headline, c_headline = self.extracted_facts["headline"]
        
        pricing_items = self.extracted_facts.get("pricing", [])
        competitors_items = self.extracted_facts.get("competitors", [])

        # Format Pricing
        pricing_str = ""
        for p_val, p_desc, cit in pricing_items:
            pricing_str += f"      - {p_val} ({p_desc}) [Citation {cit}]\n"
        if not pricing_str:
            pricing_str = "      - No pricing data found.\n"

        # Format Competitors
        comp_str = ""
        for comp_name, cit in competitors_items:
            comp_str += f"{comp_name} [Citation {cit}], "
        comp_str = comp_str.strip(", ") if comp_str else "None detected"

        # Render report
        report = (
            f"========================================================================\n"
            f"          GTM INTELLIGENCE DOSSIER: {self.domain.upper()}\n"
            f"========================================================================\n"
            f" 📌 COMPANY TITLE: {title} [Citation {c_title}]\n"
            f" 📖 BACKGROUND:    {desc} [Citation {c_desc}]\n"
            f" 🛠️ TECHNOGRAPHICS: {', '.join(tech)} [Citation {c_tech}]\n"
            f" 💰 PRICING PLANS:\n{pricing_str}"
            f" 🎯 RIVALS (MAP):  {comp_str}\n"
            f" 📰 LATEST NEWS:   \"{headline}\" [Citation {c_headline}]\n"
            f"------------------------------------------------------------------------\n"
            f" CONFIDENCE SCORE: {confidence_score:.1f}% / 100.0%\n"
            f" CONFIDENCE AUDIT LOGS:\n"
        )
        for f in audit_factors:
            report += f"   - {f}\n"
            
        report += "\n CITATION FOOTNOTES:\n"
        for cit in self.citations:
            report += f"   {cit}\n"
            
        report += "========================================================================"
        return report

if __name__ == "__main__":
    # Run pipeline on Stripe
    stripe_assistant = AICompanyResearchAssistant("stripe.com")
    stripe_dossier = stripe_assistant.run_research_pipeline()
    print(stripe_dossier)
    print("\n\n")

    # Run pipeline on Snowflake
    snowflake_assistant = AICompanyResearchAssistant("snowflake.com")
    snowflake_dossier = snowflake_assistant.run_research_pipeline()
    print(snowflake_dossier)
    print("\n\n")

    # Run pipeline on invalid company to check error handling
    invalid_assistant = AICompanyResearchAssistant("unreachable-startup.io")
    invalid_dossier = invalid_assistant.run_research_pipeline()
    print(invalid_dossier)
