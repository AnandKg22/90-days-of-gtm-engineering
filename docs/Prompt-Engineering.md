# Prompt Engineering & Structured Outputs for Sales

This guide details frameworks, structured output techniques, and prompt templates to build reliable automated copywriters and lead qualifiers.

---

## 1. Prompt Engineering Frameworks

*   **AIDA (Attention, Interest, Desire, Action)**:
    *   *Attention*: Open with a specific, positive hook about their recent company milestone.
    *   *Interest*: State a problem they likely face based on their company profile.
    *   *Desire*: Offer a low-friction solution with a social proof metric.
    *   *Action*: Close with a call-to-action (CTA) asking for interest, not a meeting (e.g. "Do you have open bandwidth for a 2-line overview?").
*   **PAS (Problem, Agitation, Solution)**:
    *   *Problem*: Identify a pain point (e.g. manual data entry in CRM).
    *   *Agitation*: Explain the consequences (e.g. sales reps wasting 10 hours/week, missing pipeline forecast accuracy).
    *   *Solution*: Introduce your automation capabilities.

---

## 2. Structured Outputs & Pydantic Validation

To feed LLM outputs directly into a CRM or database, the JSON must conform to a strict schema. We use **Pydantic** in Python to guarantee this.

```python
from pydantic import BaseModel, Field, EmailStr
from openai import OpenAI
from typing import List, Optional

# 1. Define target structure
class LeadEnrichmentResult(BaseModel):
    company_name: str
    inferred_pain_points: List[str] = Field(description="List of 3 primary pain points of the company")
    technologies_detected: List[str]
    suggested_email_hook: str = Field(description="A 1-sentence personalized hook for outreach")
    confidence_score: float = Field(description="Score between 0 and 1 indicating suitability")

# 2. Call OpenAI Structured Outputs API
client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Analyze company website and extract metadata."},
        {"role": "user", "content": "Stripe provides developer payment APIs. They are hiring React devs."}
    ],
    response_format=LeadEnrichmentResult,
)

# Parsed result is guaranteed to follow LeadEnrichmentResult model structure
parsed_data = completion.choices[0].message.parsed
print(parsed_data.company_name)
print(parsed_data.inferred_pain_points)
```

---

## 3. Production Prompt Templates

### System Prompt for Lead Scoring Engine

```markdown
You are a Lead Scoring AI Engine. Evaluate incoming lead profiles against the provided Ideal Customer Profile (ICP).

ICP Criteria:
- Target Industry: B2B SaaS, FinTech, E-commerce
- Company Size: 50 - 500 employees
- Location: North America, Europe
- Key Technology: Salesforce, React, Stripe

Inputs:
- Industry: {lead_industry}
- Employee Count: {lead_size}
- Location: {lead_location}
- Technologies: {lead_tech}

Output JSON format:
{
  "fit_status": "HIGH" | "MEDIUM" | "LOW",
  "weighted_score": float, // 0 to 100
  "justification": "Clear explanation of score fit"
}
```
