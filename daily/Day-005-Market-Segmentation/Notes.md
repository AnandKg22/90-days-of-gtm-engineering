# Study Notes - Day 005: Market Segmentation & Positioning

Today's studies focused on analyzing TAM, SAM, and SOM, and segmenting markets based on firmographic, technographic, and geographic attributes.

---

## 1. TAM, SAM, and SOM

To understand the revenue capacity of a business, we divide the market into three layers:

```
┌─────────────────────────────────────────────────────────┐
│              TAM (Total Addressable Market)             │
│   e.g., All Maritime Training Institutes Globally       │
│   ┌─────────────────────────────────────────────────┐   │
│   │         SAM (Serviceable Addressable Market)    │   │
│   │      e.g., DGS-Approved Academies in India      │   │
│   │   ┌─────────────────────────────────────────┐   │   │
│   │   │       SOM (Serviceable Obtainable Market)│   │   │
│   │   │    e.g., Target Colleges in Coastal States│   │   │
│   │   └─────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

1.  **TAM (Total Addressable Market)**: The complete, global revenue opportunity if you captured 100% of the target market (e.g. all 5,000+ maritime academies worldwide).
2.  **SAM (Serviceable Addressable Market)**: The portion of the TAM that fits your current product capabilities and distribution channels (e.g. 500 DGS-approved maritime academies in India).
3.  **SOM (Serviceable Obtainable Market)**: The specific segment of the SAM you can realistically win in the short term, given your resources, geography, and sales team (e.g. 50 maritime colleges in Goa, Mumbai, and Chennai).

---

## 2. Deep-Dive: Market Segmentation Subtopics

To segment lead databases programmatically, a GTM Engineer must apply rules across these six subtopics:

### 1. Industry Niche
*   **Definition**: The specific sub-vertical the company operates in (e.g. separating *Post-Graduate Academies* from *Modular Safety Centres*).
*   **GTM Application**: Different sub-verticals receive different email hooks and product features.

### 2. Employee Count
*   **Definition**: Dividing the market by organization scale (e.g., Small Academies < 50, Mid-Market 50–200, Enterprise > 200).
*   **GTM Application**: Employee counts map to different pricing tiers (Starter vs. Growth vs. Enterprise licenses).

### 3. Revenue
*   **Definition**: Segmenting companies by annual billings or institutional budget.
*   **GTM Application**: Helps calculate average deal size and prioritize high-value contract opportunities.

### 4. Country (Geography)
*   **Definition**: Segmenting markets by geographical boundaries and localized regulatory compliance requirements.
*   **GTM Application**: For VivaExams, different countries have different regulatory bodies (e.g., DGS in India, MPA in Singapore, USCG in the USA). Leads are routed to AEs specializing in those local regulations.

### 5. Technology (Technographics)
*   **Definition**: Segmenting prospects by their tech compatibility (e.g., colleges using legacy LMS vs. colleges with zero digital exam systems).
*   **GTM Application**: Simplifies custom engineering requirements by filtering out incompatible technology users.

### 6. Intent (Behavioral)
*   **Definition**: Segmenting leads by active buying interest (e.g. high intent: viewed pricing page twice; low intent: only read a blog post).
*   **GTM Application**: Directs sales energy toward warm prospects, moving cold prospects to background nurturing.
