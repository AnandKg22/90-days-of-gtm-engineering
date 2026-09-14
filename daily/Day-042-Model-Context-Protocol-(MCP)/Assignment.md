# Project Assignment - Day 042: CRM MCP Server

This project requires developing a Model Context Protocol (MCP) server that connects to an external CRM database mockup. It handles JSON-RPC 2.0 requests over standard I/O (stdio) and exposes multiple tools for contact queries, deal listing, and note creation.

---

## 🎯 Requirements

Your MCP Server must:
1.  **Transport Protocol**:
    *   Communicate over stdio (reading lines from `sys.stdin`, writing lines to `sys.stdout`).
    *   Encode payloads strictly as single-line JSON-RPC 2.0 messages.
2.  **Separate Logs (Stderr)**:
    *   Ensure that all debugging, warnings, and trace logs are written to `sys.stderr`. Any raw text printed to `sys.stdout` will corrupt the channel and crash client hosts (like Claude Desktop).
3.  **Implement Handshake & Discovery**:
    *   Handle the `initialize` method returning server specifications.
    *   Handle `tools/list` returning registered tool schemas.
4.  **Register Tools**:
    *   `get_crm_contact`: Queries mock contact details (names, companies, status, and ARR) by email.
    *   `list_recent_deals`: Lists current active/won deal objects in the GTM pipeline.
    *   `add_crm_note`: Creates and appends note logs to target companies in the database.
5.  **Harness Verification**:
    *   Provide a client test harness script to programmatically launch the server, perform handshakes, list tools, and verify output formats.

---

## 💻 Deliverable Code

*   **MCP Server**: Exposes CRM tools, written in [Code/mcp_crm_server.py](Code/mcp_crm_server.py).
*   **Verification Client**: Verifies server compliance, written in [Code/test_mcp_client.py](Code/test_mcp_client.py).