# Exercises - Day 042: Model Context Protocol (MCP)

This document details practical exercises on writing MCP tool specifications, logging JSON-RPC handshakes, and extending server capabilities.

---

## 📋 Exercise 1: Writing MCP Tool JSON-Schemas

### Goal:
Translate a GTM database operation into a valid MCP `inputSchema` definition.

### Task:
Draft the `inputSchema` for a tool named `update_lead_status` that takes two parameters:
1.  `lead_id` (integer, required) - The unique ID of the target lead.
2.  `new_status` (string, required) - The target status (must be one of: 'New', 'Enriched', 'Synced', 'Contacted').

### Resulting JSON Schema:
```json
{
  "name": "update_lead_status",
  "description": "Updates a lead's stage status in the GTM database.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "lead_id": {
        "type": "integer",
        "description": "The unique identifier of the target lead."
      },
      "new_status": {
        "type": "string",
        "enum": ["New", "Enriched", "Synced", "Contacted"],
        "description": "The new GTM status to set for the lead."
      }
    },
    "required": ["lead_id", "new_status"]
  }
}
```

---

## ⚙️ Exercise 2: Tracing stdio Handshake Exchange Logs

Analyze this actual startup log trace from Claude Desktop connecting to a local MCP server:

```text
[CLIENT -> SERVER]: 
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "claude-desktop", "version": "1.2.0"}
  }
}

[SERVER -> CLIENT]: 
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {"tools": {}},
    "serverInfo": {"name": "gtm-crm-server", "version": "1.0.0"}
  }
}
```

### Analysis:
*   The client issues request `id: 1` with method `initialize` containing its protocol version.
*   The server responds with an identical transaction ID (`id: 1`) and announces that its capabilities support `tools`.

---

## 📊 Exercise 3: Adding Resources to the MCP Server

### Goal:
Extend the stdio server to expose static documentation as a read-only **Resource**.

### Task:
Implement the `resources/list` method. When called, the server should return a URI link to a local pricing guidelines document:
```python
def handle_resources_list(req_id):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "resources": [
                {
                    "uri": "gtm://documentation/pricing-rules",
                    "name": "SaaS Pricing Guidelines",
                    "mimeType": "text/markdown",
                    "description": "GTM Rules and contract values models for SaaS tiers."
                }
            ]
        }
    }
```
If the client issues `resources/read` with URI `gtm://documentation/pricing-rules`, return the file content as text.
```python
def handle_resources_read(req_id, params):
    uri = params.get("uri")
    if uri == "gtm://documentation/pricing-rules":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/markdown",
                        "text": "# SaaS Pricing Tiers\n- SMB: $5,000/yr\n- Mid-Market: $25,000/yr\n- Enterprise: Custom"
                    }
                ]
            }
        }
```