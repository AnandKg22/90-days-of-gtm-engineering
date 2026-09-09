# Study Notes - Day 041: AI Agent Fundamentals

Today's studies focused on AI Agent Architectures, distinguishing agents from simple chat completion prompts, exploring ReAct (Reasoning and Acting) loops, and mapping memory systems, planning frameworks, and human-in-the-loop structures.

---

## 1. What Defines an AI Agent?

An **AI Agent** is an autonomous entity driven by an LLM core that perceives an environment, makes decisions, and executes actions using tools to achieve a predefined goal. Unlike a static prompt that generates a single response, an agent runs in an active loop.

### Core Architectural Pillars:
1.  **Goal**: The target state or instructions (e.g. "Acquire contact details for company X").
2.  **Planning Engine**: The reasoning framework that breaks down the goal into sub-tasks (e.g. CoT, ReAct).
3.  **Memory**: The state-tracker that stores historical observations and progress.
4.  **Tools**: Executable APIs or functions that the agent can call to interact with the external world (e.g. search web, CRM write).
5.  **Execution Loop**: The loop that runs: Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Reflection $\rightarrow$ Repeat.

---

## 2. Reasoning vs. Action (The ReAct Framework)

Developed by Yao et al. (2022), **ReAct** (Reasoning and Acting) is a paradigm that prompts LLMs to generate both reasoning traces and task-specific actions in an alternating manner.

```
[Thought] ────> [Action] ────> [Observation] ────> [Thought (Reflection)] ────> [Repeat/Done]
```

*   **Thought**: "I need to find company X's CEO. I should search for 'company X CEO' on the web." (Reasoning)
*   **Action**: `search_web("company X CEO")` (Executing tool)
*   **Observation**: "Search returned: John Doe is the CEO of company X." (Environment feedback)
*   **Next Thought**: "I now have the CEO name. Next I need his email. I should scrape the contacts database." (Next iteration planning)

Integrating reasoning and acting prevents compounding errors, as the agent continually adjusts its plan based on actual tool observations rather than hallucinating paths.

---

## 3. Agent Memory Architecture

To solve complex tasks, agents deploy distinct memory registers:

| Memory Type | Scope | Tech Stack / Implementation |
| :--- | :--- | :--- |
| **Short-Term Memory** | In-context state during a single execution loop. | Chat history lists, system prompt history, and local variables. |
| **Long-Term Memory** | Persistent knowledge stored across multiple sessions. | Vector databases (pgvector, Pinecone) for semantic semantic searches. |
| **Relational Memory** | Hard structured facts and logs. | Relational databases (PostgreSQL/SQLite) tracking client IDs and sync statuses. |

---

## 4. GTM Agent Subtopics Deep-Dive

### 1. Planning Engines (CoT vs. ToT)
*   **Chain of Thought (CoT)**: Linear step-by-step reasoning (e.g., "First do A, then do B").
*   **Tree of Thoughts (ToT)**: Explores multiple reasoning branches, evaluating candidate actions before selecting the best branch. Good for advanced problem solving like lead lists deductions.

### 2. Tool Invocation & Schema Mapping
*   **Function Calling**: LLMs do not run code directly; they output structured JSON representing the tool name and argument schema:
    ```json
    {
      "tool": "search_web",
      "argument": "Wayne Enterprises tech stack"
    }
    ```
*   The execution wrapper (orchestrator) intercepts this JSON, runs the local Python/JS API, and returns the result as an `Observation` string back to the LLM.

### 3. State Management & Recovery
*   **State Persistence**: Saving the agent's memory at each step. If a network request fails, the agent can reload the last state and resume.
*   **Error Recovery**: If a tool returns an error, the agent's thought step reflects on the error (e.g. "The pricing scraper was blocked by Cloudflare. Action: fallback to search_web for pricing press releases").

### 4. Human-in-the-Loop (HITL) Workflows
*   For high-risk GTM tasks (e.g. sending outbound emails or updating billing configurations), the agent pauses before execution:
    1.  Agent drafts the email and transitions state to `Pending Approval`.
    2.  An editor reviews and clicks "Approve".
    3.  The agent receives the approval webhook and dispatches the email.
