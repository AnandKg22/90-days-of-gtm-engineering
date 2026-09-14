# GTM Architecture - Day 042: Model Context Protocol (MCP)

This document details the architecture, communications pipelines, and data mapping schemas supporting Model Context Protocol (MCP) servers.

---

## 🔄 MCP Communication Architecture

The diagram below details the architecture, showing how messages are parsed and responses are piped between the host client and the server:

```mermaid
graph TD
    subgraph Host Application (Claude Desktop)
        Client[LLM Client Host] -->|1. Formulate Thought| Planner[Agent Planner]
        Planner -->|2. Generate Tool Call JSON| Transport[Stdio JSON-RPC Client]
    end
    
    subgraph Stdio Communication Pipeline
        Transport -->|3. Write JSON Line to stdin| PipeIn[sys.stdin Pipe]
        PipeOut[sys.stdout Pipe] -->|9. Read JSON Line from stdout| Transport
    end
    
    subgraph GTM MCP Server (Code/mcp_crm_server.py)
        PipeIn -->|4. Parse JSON| Parser{JSON-RPC Parser}
        Parser -->|5. Match Method| Route{initialize / tools list / tools call}
        
        Route -->|tools/call| Execute[Execute Registered Tool Function]
        Route -->|tools/list| Tools[Load JSON Tool Schemas]
        Route -->|initialize| Handshake[Verify Protocol Version]
        
        Execute -->|Read/Write CRM Data| CRM[(CRM Mock DB)]
        Execute -->|6. Log progress to stderr| Stderr[sys.stderr Log]
        
        CRM -->|7. Compile Content Output| Serialize[Serialize Result JSON]
        Tools -->|7. Compile Content Output| Serialize
        Handshake -->|7. Compile Content Output| Serialize
        
        Serialize -->|8. Write JSON Line to stdout| PipeOut
    end
```

---

## ⚙️ Stderr Logging Segregation

A critical constraint in MCP architecture over standard I/O (stdio) is the separation of data transport from log output:

*   **`stdout` (Piped)**: Reserved exclusively for clean JSON-RPC 2.0 messages. Any unexpected text (e.g. `print("Server started")`) corrupts the stream, breaking the client host's JSON parser and crashing the connection.
*   **`stderr` (Printed)**: Redirects all debugging logs, trace statements, warnings, and error messages. Host applications capture `stderr` logs and write them to system files (e.g., Claude Desktop logs in AppData) for developer auditing without interfering with the JSON-RPC interface.

---

## 🛠️ registered CRM Tool Schemas

The MCP server exposes three tools with their parameter schemas:

1.  **`get_crm_contact`**: Retrieves contact info, ARR, and sync status by `email` (string, required).
2.  **`list_recent_deals`**: Retrieves the list of active sales deals in the pipeline.
3.  **`add_crm_note`**: Appends note annotations to target company accounts. Takes two arguments: `company` (string, required) and `note` (string, required).
