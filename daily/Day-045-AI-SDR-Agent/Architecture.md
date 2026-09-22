# GTM Architecture - Day 045: AI SDR Agent v2

This document details the campaign scheduling engine, message sequencing structures, and CRM integration gates supporting AI Sales Development Representative (SDR) agents.

---

## 🔄 AI SDR v2 Campaign Pipeline

The diagram below details the pipeline, showing how leads are qualified, compiled into multi-step outreach sequences, and logged in the CRM:

```mermaid
graph TD
    Trigger[Trigger: Lead Enriched] -->|1. Ingest Profile| QualGate{Is Score >= 70?}
    
    QualGate -->|No| Disqual[Mark Disqualified & Skip]
    QualGate -->|Yes| CRM1[HubSpot/Salesforce: Set Outbound-In-Sequence]
    
    subgraph Outbound Sequence Generation
        CRM1 -->|2. Feed Firmographics| Engine[Outbound Sequence Builder]
        Engine -->|3. Generate touch 1| T1[Touch 1: Cold Email - Day 0]
        Engine -->|4. Generate touch 2| T2[Touch 2: LinkedIn Connect - Day 3]
        Engine -->|5. Generate touch 3| T3[Touch 3: Value Email - Day 7]
        Engine -->|6. Generate touch 4| T4[Touch 4: Break-up Email - Day 14]
    end
    
    subgraph Scheduling & CRM Logging
        T1 -->|7. Log Task| CRM2[HubSpot Contact Timeline]
        T2 -->|7. Log Task| CRM2
        T3 -->|7. Log Task| CRM2
        T4 -->|7. Log Task| CRM2
        
        CRM2 -->|8. Push to queue| Queue[Task Queue / SendGrid Scheduler]
    end
    
    subgraph Inbound Reply Loop
        Buyer[Lead / Recipient] -->|9. Reply Email| Webhook[Reply Hook Receiver]
        Webhook -->|10. Match email| Cancel[Cancel Downstream Touchpoints]
        Cancel -->|11. Update CRM status| CRM3[CRM Stage: Contacted-Replied]
    end
```

---

## ⚙️ Outbound State Transitions

The SDR Agent manages five distinct lead statuses on the contact object to maintain pipeline visibility:

*   **`New`**: Ingested but not yet qualified or enriched.
*   **`Qualified`**: Intent score $\ge 70$, ready for outbound campaign injection.
*   **`Outbound-In-Sequence`**: Multi-touch campaign planned and active.
*   **`Contacted-Replied`**: Prospect replied to an email (scheduled touchpoints cancelled immediately).
*   **`Closed-Lost-No-Response`**: Touch 4 executed without response, sequence terminated.
