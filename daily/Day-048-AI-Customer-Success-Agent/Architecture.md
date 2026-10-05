# GTM Architecture - Day 048: AI Customer Success Agent

This document details the account health auditing pipeline, metrics databases, and CSM escalation hooks supporting retention engineering.

---

## 🔄 CS Portfolio Auditing Pipeline

The diagram below details the pipeline, showing how telemetry data is calculated to compile customer health rankings and trigger mitigation processes:

```mermaid
graph TD
    Telemetry[Product Usage Telemetry] -->|1. Ingest| CSMAgent[CS Assistant Scorer]
    Tickets[Help Desk: Zendesk / Jira] -->|1. Ingest| CSMAgent
    CRM[HubSpot Opportunity Data] -->|1. Ingest| CSMAgent
    
    subgraph Customer Health Score Compiler
        CSMAgent -->|2. Compute metrics| Scorer[CHS Scorer Engine]
        Scorer -->|Check score thresholds| Threshold{Identify Tier}
    end
    
    subgraph Red Tier: Churn Escalation
        Threshold -->|Score < 50| RedFlow[Trigger Churn Playbook]
        RedFlow -->|Push Slack alert| Slack[CSM Slack Channel]
        RedFlow -->|Flag priority ticket| Jira[Jira Escalation Ticket]
        RedFlow -->|Draft outreach| Email1[Executive Health Review Email]
    end
    
    subgraph Green Tier: Expansion Upgrades
        Threshold -->|Score >= 80 & Usage >= 90%| GreenFlow[Trigger Upsell Playbook]
        GreenFlow -->|Draft proposal| Email2[Seat License Upsell Email]
    end
    
    subgraph Yellow Tier: Monitoring
        Threshold -->|50 <= Score < 80| YellowFlow[Check Onboarding Milestones]
        YellowFlow -->|If incomplete| Warn[Log Onboarding Pending Warning]
    end
```

---

## ⚙️ Core Architecture Components

1.  **Telemetry Ingestor**: Connects to product databases to pull active seat utilization, login counts, and api credit balances.
2.  **Help Desk Listener**: Queries ticket APIs (e.g. Zendesk) to fetch open customer tickets and calculate sentiment penalties.
3.  **CHS Scorer Engine**: Calculates a 100-point health score by weighting adoption, onboarding progress, and support tickets.
4.  **Escalation Router**: Evaluates health tiers, triggering CSM warning notifications to Slack and prioritizing support queues.
5.  **Dossier Email Writer**: Drafts customized outreach templates for CSMs (addressing tickets for at-risk accounts or pitching upgrades for healthy accounts).
