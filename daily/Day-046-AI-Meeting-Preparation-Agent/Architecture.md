# GTM Architecture - Day 046: AI Meeting Preparation Agent

This document details the sales intelligence pipeline, calendar hooks, and dossier compilation supporting pre-call meeting preparation.

---

## 🔄 Meeting Prep Data Pipeline

The diagram below details the pipeline, showing how calendar events trigger the agent to fetch account details and compile a strategic sales dossier:

```mermaid
graph TD
    Cal[Calendar Event: Google Calendar / Outlook] -->|1. Webhook Trigger| Listener[Calendar Listener]
    Listener -->|2. Extract domain/leads| Directory[Lead Database / CRM]
    
    subgraph Data Aggregation
        Directory -->|3. Get firmographics| Account[Account Details]
        Directory -->|3. Get technographics| Tech[Tech Stack Database]
        Directory -->|3. Get LinkedIn bios| Bios[Stakeholder Bio Registry]
    end
    
    subgraph Intelligence Synthesis
        Account -->|4. Map ARR potential| OppSummary[Opportunity Summary Builder]
        Tech -->|4. Detect rivals| BattleCard[Competitive Battle Card compiler]
        Bios -->|4. Persona match| Persona[Stakeholder Persona Analyzer]
    end
    
    OppSummary -->|5. Compile| Dossier[Dossier Compiler]
    BattleCard -->|5. Compile| Dossier
    Persona -->|5. Compile| Dossier
    
    subgraph Diagnostic Generation
        Dossier -->|6. Generate SPIN questions| Discovery[Discovery Questions compiler]
        Dossier -->|6. Generate objections| Objections[Objections Predictor]
        Dossier -->|6. Time block| Agenda[Meeting Agenda Planner]
    end
    
    Discovery -->|7. Assemble| Report[Final Briefing Dossier]
    Objections -->|7. Assemble| Report
    Agenda -->|7. Assemble| Report
    
    Report -->|8. Push notification| Rep[Slack Alert / CRM Event to AE]
```

---

## ⚙️ Core Architecture Components

1.  **Calendar Listener**: Webhook receiver that listens for incoming sales calendar events (e.g. Google Calendar meetings). Extracts company domains and stakeholder email addresses.
2.  **Account & Technographics Profiler**: Queries internal and external database pools to compile firmographic profiles (size, industry, ARR) and technographic parameters.
3.  **Battle Card Compiler**: Checks prospect technologies against ours to map competitive gaps and highlight why we win.
4.  **Objection Predictor**: Analyzes stakeholder personas (e.g. CEO vs. CTO) and pain points to anticipate objections and compile reframing scripts.
5.  **SPIN Question Planner**: Synthesizes open-ended, diagnostic discovery questions mapped to the prospect's industry and pain points.
