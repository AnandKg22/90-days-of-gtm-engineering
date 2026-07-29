# Project Assignment - Day 016: Webhook to CRM Sync Workflow

This project requires creating a fully functional n8n JSON workflow schema definition that integrates a webhook trigger, data transformation, HTTP request enrichment, IF routing logic, HubSpot company creation, and Slack alerts.

---

## 🎯 Requirements

Your JSON schema must:
1.  Target version-controlled n8n workflow configurations.
2.  Expose six connected node definitions:
    *   `Webhook` node (listening for checkout events).
    *   `Code` node (calculating email domains via JavaScript).
    *   `HTTP Request` node (fetching mock Apollo profiles).
    *   `IF` node (filtering company sizes above 50 employees).
    *   `HubSpot` node (upserting Company custom properties).
    *   `Slack` node (posting deal alerts).
3.  Format connection logic defining the workflow graph edges linking source outputs to target inputs.

---

## 💻 Deliverable Code

A complete, working n8n JSON schema has been generated and placed in [Code/n8n_workflow_schema.json](Code/n8n_workflow_schema.json). It contains the complete set of parameters and node connections, ready to be copied and pasted directly into the n8n UI canvas.
