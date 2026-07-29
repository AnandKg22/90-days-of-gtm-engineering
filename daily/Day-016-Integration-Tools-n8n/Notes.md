# Study Notes - Day 016: Integration Tools (n8n Workflows)

Today's studies focused on node-based workflow orchestration (n8n), trigger/action mechanics, conditional branching, HTTP Request node designs, and version-controlling n8n workflow schemas.

---

## 1. n8n in GTM Engineering

Writing raw Python scripts for every system integration is time-consuming and difficult to monitor. GTM Engineers use orchestrators like n8n to:

*   **Build visually, run programmatically**: n8n provides a visual node-based editor while executing pipelines as optimized JavaScript workflows.
*   **Simplify Auth**: Standard nodes handle OAuth2 tokens, credential storage, and refreshing keys automatically.
*   **Monitor Failures**: Provides visual execution histories showing exactly which node failed, along with payload error logs.

---

## 2. Deep-Dive: n8n Subtopics

To construct enterprise-grade workflows in n8n, a GTM Engineer must master these three subtopics:

### 1. Workflow Automation (Conditional Branching & Loops)
*   **Definition**: Building robust pipelines that handle conditional logic (IF/Switch nodes), loops (Split In Batches), and custom code scripts (Code nodes).
*   **GTM Application**: You configure n8n IF nodes to split routing:
    *   *If company size > 50*: Route to sales reps (HubSpot Deals).
    *   *If company size <= 50*: Route to B2C self-serve emails (ActiveCampaign).

### 2. API Integration (HTTP Request & Webhook Nodes)
*   **Definition**: Custom HTTP calls using generic nodes when native app nodes are missing or lack features.
    *   **Webhook Node**: Exposes an HTTP URL endpoint (active or testing) that receives external JSON payloads (Stripe events).
    *   **HTTP Request Node**: Makes REST requests (GET/POST/PUT) with custom auth headers, body parameters, and SSL verifications.
*   **GTM Application**: Setting up generic HTTP Request nodes to query Apollo.io's person-matching REST endpoint.

### 3. Schema Configuration (Workflow JSON Export)
*   **Definition**: Representing and storing n8n workflows as standard JSON configuration files.
*   **GTM Application**: n8n workflows can be fully exported, imported, and modified as JSON. A GTM Engineer keeps these JSON files in git repositories, enabling version control and CI/CD pipelines to deploy workflows between staging and production n8n instances.
