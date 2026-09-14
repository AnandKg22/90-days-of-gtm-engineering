# Study Notes - Day 042: Model Context Protocol (MCP)

Today's studies focused on the Model Context Protocol (MCP) specification developed by Anthropic, exploring standard architectures (Hosts, Clients, Servers), JSON-RPC 2.0 transports, tool discovery schemas, resource lifecycles, and security protocols.

---

## 1. What is the Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open standard that allows LLM applications (clients/hosts) to connect to external data sources and tools (servers) via a unified API. 

### Why MCP?
Before MCP, developers had to write custom tool wrappers for every LLM SDK (OpenAI, Anthropic, LangChain). MCP standardizes this interface; you write a single MCP server, and any MCP-compliant client (e.g. Claude Desktop, Cursor, Custom Agent Orchestrators) can immediately discover and run its tools.

---

## 2. MCP Core Architecture & Roles

MCP operates on a three-tier model:

```
[ LLM Host App (e.g. Claude Desktop) ] ──> [ MCP Client Wrapper ] <══ JSON-RPC 2.0 (stdio/SSE) ══> [ MCP Server ] ──> [ CRM/Database ]
```

1.  **Host**: The application that manages the LLM context and prompts (e.g. IDEs, agent orchestrators).
2.  **Client**: The component in the host that communicates with the MCP server, passing tool definitions and handling execution requests.
3.  **Server**: A standalone process that exposes tools, resources, and prompts to the client.

---

## 3. Transports: Stdio vs. SSE

MCP supports two primary transport communication channels:

### 1. Stdio (Standard Input/Output)
*   **Mechanism**: The client launches the server as a subprocess and writes JSON lines to its `stdin`, while reading responses from `stdout`.
*   **Scope**: Ideal for local integrations (e.g., local filesystems, database connections, and locally run scripts).
*   **Critical Constraint**: The server *must* write all logs, errors, and debug notices to `stderr`. Printing anything other than clean JSON-RPC lines to `stdout` breaks the communication channel and crashes the client.

### 2. SSE (Server-Sent Events / HTTP)
*   **Mechanism**: The client connects to an HTTP endpoint on the server. The server streams events via SSE, and the client sends command payloads back via POST requests.
*   **Scope**: Essential for remote integrations, microservices, and cloud databases.

---

## 4. MCP JSON-RPC Handshake Protocol

When an MCP client initiates a connection, it performs a 3-step handshake:

1.  **Initialize**:
    *   Client sends `method: initialize` with its protocol version.
    *   Server replies with its capabilities (e.g., "I support tools and resources") and details.
2.  **Initialized Notification**:
    *   Client sends `method: notifications/initialized` to confirm it is ready to receive requests.
3.  **Discovery**:
    *   Client requests available tools via `method: tools/list`.
    *   Client requests available resources via `method: resources/list`.

---

## 5. Security & Permission Considerations

When running MCP servers, engineers must enforce security barriers:
*   **Sandboxing Subprocesses**: When running stdio servers, restrict their access scopes (e.g. read-only filesystems).
*   **Input Validation**: MCP servers receive raw strings/JSON from the LLM. Server tools must strictly parse and validate these inputs (e.g. sanitizing SQL queries) to prevent injection attacks.
*   **OAuth Scopes**: Remote SSE servers should require Bearer tokens in headers to authenticate requests before executing tools.
