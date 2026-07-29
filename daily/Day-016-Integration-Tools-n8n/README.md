# Day 016: Integration Tools (n8n)

## Objective
Design and implement automated GTM integration workflows inside n8n, configure conditional IF filters and HTTP Request nodes, and export version-controlled JSON schema files representing the visual pipeline.

## Topics Covered
- n8n visual flow programming
- Webhook triggers & App actions
- HTTP Request & JavaScript nodes
- Workflow connections and JSON exports

## Subtopics (Developed in Notes)
- Workflow Automation (Conditional Branching & Loops)
- API Integration (HTTP Request & Webhook Nodes)
- Schema Configuration (Workflow JSON Export)

---

## 🛠️ Practical Exercise: n8n Workflow Design

In this exercise, we designed a complete customer sync pipeline inside n8n:
*   **Trigger Node**: Webhook node listening on `POST /stripe-payment`.
*   **Data Parsing Node**: JavaScript Code node separating email domains.
*   **Enrichment Node**: HTTP Request node matching company details via Apollo.
*   **IF Condition Node**: Filter company sizes above `50` employees.
*   **HubSpot Node**: Create/Update Company profiles with cadet licenses.
*   **Slack Node**: Route Markdown deal alerts to sales channels.
*   **ActiveCampaign Node**: Route B2C leads to automated email nurture lists.

*View complete parameter mapping details in [Exercises.md](Exercises.md).*

---

## 🏫 Daily Project / Assignment: Webhook to CRM Sync Schema

We generated a fully functional n8n JSON workflow template in [Code/n8n_workflow_schema.json](Code/n8n_workflow_schema.json):
*   Implements the official n8n JSON schema contract containing the six integrated nodes.
*   Maps all values dynamically using expression syntax (e.g. `{{$json.organization.name}}`).
*   Declares graph edges connecting the outputs of triggers and mappers directly to downstream inputs.

*View project requirements in [Assignment.md](Assignment.md) and the connection diagram in [Architecture.md](Architecture.md).*

---

## 📂 Expected Deliverables
*   📝 [Day 16 Study Notes](Notes.md) — Node automation rules and JSON exports.
*   📝 [n8n Node Blueprint](Exercises.md) — Node parameters configuration spec.
*   📝 [n8n Sync Schema Spec](Assignment.md) — JSON requirements.
*   📊 [n8n Connection Diagram](Architecture.md) — Visual workflow nodes connections graph.
*   💻 [n8n JSON Schema Template](Code/n8n_workflow_schema.json) — Importable n8n workflow configuration file.

---

## 📝 Notes & Reflection
*   **Key Insight**: Keeping n8n workflow configurations in JSON files inside git repositories allows teams to collaborate on integrations and deploy pipeline updates safely.
*   **Study Log**: Read notes in [Notes.md](Notes.md).
*   **Daily Log**: Read reflections in [Reflection.md](Reflection.md).
