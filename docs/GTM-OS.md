# GTM-OS: Flagship Revenue Operating System Specifications

GTM-OS is a unified, multi-tenant SaaS operating system designed for commercial departments, integrating marketing, sales pipeline automation, AI-native outreach, customer health metrics, and executive charts.

---

## 1. Core Service Architecture

GTM-OS is built as a modular architecture consisting of these key service layers:

```
                  ┌──────────────────────┐
                  │    REACT FRONTEND    │
                  │ (Tailwind Dashboard) │
                  └──────────┬───────────┘
                             │
     ┌───────────────────────┼───────────────────────┐
     ▼                       ▼                       ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│  Auth Serv.  │        │ CRM Gateway  │        │  Agent Engine│
│ (Clerk/Auth) │        │ (Hubspot/SF) │        │  (AI SDR/RAG)│
└──────────────┘        └──────────────┘        └──────────────┘
```

*   **Auth Service**: Handles multi-tenant organization isolation and Role-Based Access Control (RBAC) (Owner, Admin, Sales Rep, CS Rep).
*   **CRM Gateway**: Unifies HubSpot and Salesforce API client wrappers, offering a standard, single-endpoint CRUD interface for contacts, companies, and deals.
*   **AI Agent Engine**: Orchestrates lead enrichment, RAG semantic search, email copywriting, and call transcripts analytics.
*   **Analytics Engine**: Powers executive dashboard metrics (Pipeline Velocity, Cohorts, NRR) based on raw SQL aggregate tables.

---

## 2. Production Deployment Blueprint

GTM-OS is containerized using Docker and routed securely via Traefik.

### Docker Compose Production Template (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  reverse-proxy:
    image: traefik:v2.10
    command:
      - "--providers.docker=true"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
    ports:
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

  gtm-api-server:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://db_user:password@postgres:5432/gtm_os
      - REDIS_URL=redis://redis:6379/0
    labels:
      - "traefik.http.routers.api.rule=Host(`api.gtmos.com`)"
      - "traefik.http.routers.api.entrypoints=websecure"
      - "traefik.http.routers.api.tls.certresolver=myresolver"
    depends_on:
      - postgres
      - redis

  postgres:
    image: pgvector/pgvector:pg16
    environment:
      - POSTGRES_USER=db_user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=gtm_os
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redisdata:/data

volumes:
  pgdata:
  redisdata:
```

---

## 3. FinOps & AI Token Cost Optimization

Operating LLMs (GPT-4o, Claude 3.5 Sonnet) at scale for daily outreach can become very expensive. GTM-OS integrates token cost-control features:

1.  **Prompt Caching**: Structure prompts to place static instructions and context at the beginning of the API request so that models (like Anthropic or GPT-4o) can cache prompt fragments, reducing token cost by up to $50\%$.
2.  **Model Tier Routing**: Route simple tasks (lead cleaning, format checks) to lightweight models (GPT-4o-mini) and reserve premium models (Claude 3.5 Sonnet) only for complex personalizations.
3.  **Batch Processing API**: Run non-real-time agent jobs using OpenAI's Batch API to receive a $50\%$ discount on token pricing.
