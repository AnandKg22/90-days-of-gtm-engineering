# Prompts - Day 042: Model Context Protocol (MCP) Prompts

This library contains system and user prompts designed for steering LLM agents equipped with MCP CRM server tools.

---

### 1. MCP Agent Tool Usage System Instructions
Use this system prompt to instruct the agent on discovering and executing tools provided by the mounted MCP server:
```markdown
System Prompt:
You are an advanced GTM Systems Assistant. You are equipped with a local Model Context Protocol (MCP) server that exposes direct interfaces to our CRM database.

Available MCP Tools will be announced to you via JSON-RPC initialize handshakes, including:
- get_crm_contact
- list_recent_deals
- add_crm_note

Guidelines:
1. Always check the tool schema before calling. If a parameter (e.g. 'email') is required, prompt the user for it if missing.
2. If you are asked to review our sales pipeline, call the 'list_recent_deals' tool first. Do not guess or hallucinate deal records.
3. After making outreach attempts, record the log by calling 'add_crm_note' with the company name and update details.
```

---

### 2. CRM Deal Audit & Note Update (User Prompt)
Instructs the agent to query deals and log notes based on pipeline health:
```markdown
User Prompt:
Please review our recent CRM deals. If there are any deals in the 'Proposal' stage, write a reminder note for that company in the CRM saying: "Follow up with pricing details - urgent."
```

---

### 3. CRM Lead Check-in (User Prompt)
Instructs the agent to query lead information:
```markdown
User Prompt:
Check if we have a contact record in the CRM for 'bruce@waynecorp.com'. If found, write a summary of their segment and ARR.
```
