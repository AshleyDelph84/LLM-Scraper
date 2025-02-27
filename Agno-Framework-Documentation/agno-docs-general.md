
================================================================================
Section 1: Content from https://docs.agno.com/agents/introduction
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/agents/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Introduction
============

[​](https://docs.agno.com/agents/introduction#what-are-agents)

What are Agents?
----------------------------------------------------------------------------------

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Instead of a rigid binary definition, let’s think of Agents in terms of agency and autonomy.

*   **Level 0**: Agents with no tools (basic inference tasks).
*   **Level 1**: Agents with tools for autonomous task execution.
*   **Level 2**: Agents with knowledge, combining memory and reasoning.
*   **Level 3**: Teams of agents collaborating on complex workflows.

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)If you haven’t built your first agent yet, [follow this guide](https://docs.agno.com/agents) and then dive into more advanced concepts.

[​](https://docs.agno.com/agents/introduction#example-research-agent)

Example: Research Agent
------------------------------------------------------------------------------------------------

Let’s create a research agent that can search the web using DuckDuckGo, scrape the top links using Newspaper4k and write a research report for us. Ideally we’ll use specialized tools (like Exa) but let’s start with the free tools first.

The description and instructions are converted to the system message and the input is passed as the user message. Set `debug_mode=True` to view logs behind the scenes.

1

Create Research Agent

Create a file `research_agent.py`

research\_agent.py

Copy

```python
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""
```

2

Run the agent

Install libraries

Copy

```shell
pip install openai exa-py agno
```

Run the agent

Copy

```shell
python research_agent.py
```

[Community](https://docs.agno.com/get-started/community)[Agent.run()](https://docs.agno.com/agents/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [What are Agents?](https://docs.agno.com/agents/introduction#what-are-agents)
*   [Example: Research Agent](https://docs.agno.com/agents/introduction#example-research-agent)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)



================================================================================
Section 2: Content from https://docs.agno.com/
================================================================================

Title: Welcome to Agno - Agno

URL Source: https://docs.agno.com/

Markdown Content:
Welcome to Agno - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Welcome to Agno

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Welcome to Agno
===============

**Agno is a lightweight library for building multi-modal Agents.**

[​](https://docs.agno.com/#simple-fast-and-agnostic)

Simple, Fast, and Agnostic
----------------------------------------------------------------------------------

Agno is designed with three core principles:

*   **Simplicity**: No graphs, chains, or convoluted patterns — just pure python.
*   **Uncompromising Performance**: Blazing fast agents with a minimal memory footprint.
*   **Truly Agnostic**: Any model, any provider, any modality. Agno is designed to be the container for AGI.

[​](https://docs.agno.com/#key-features)

Key features
--------------------------------------------------------

Here’s why you should build Agents with Agno:

*   **Lightning Fast**: Agent creation is 5000x faster than LangGraph (see [performance](https://github.com/agno-agi/agno#performance)).
*   **Model Agnostic**: Use any model, any provider, no lock-in.
*   **Multi Modal**: Native support for text, image, audio and video.
*   **Multi Agent**: Delegate tasks across a team of specialized agents.
*   **Memory Management**: Store user sessions and agent state in a database.
*   **Knowledge Stores**: Use vector databases for Agentic RAG or dynamic few-shot.
*   **Structured Outputs**: Make Agents respond with structured data.
*   **Monitoring**: Track agent sessions and performance in real-time on [agno.com](https://app.agno.com/).

[​](https://docs.agno.com/#get-started)

Get Started
------------------------------------------------------

If you’re new to Agno, start here to build your first Agent.

[Build your first Agent ---------------------- Learn how to build Agents with Agno](https://docs.agno.com/get-started/agents)[Agent Playground ---------------- Chat with your Agents using a beautiful Agent UI](https://docs.agno.com/get-started/playground)[Agent Observability ------------------- Monitor your Agents on [agno.com](https://app.agno.com/)](https://docs.agno.com/get-started/monitoring)

After that, checkout the [Examples Gallery](https://docs.agno.com/examples) to discover real-world applications built with Agno.

[​](https://docs.agno.com/#build-with-agno)

Build with Agno
--------------------------------------------------------------

Agno is a battle-tested framework with best-in-class performance, checkout the following guides to dive-in:

[Agents ------ Learn core Agent concepts](https://docs.agno.com/agents)[Models ------ Use any model, any provider, no lock-in](https://docs.agno.com/models)[Tools ----- Use 100s of tools to extend your Agents](https://docs.agno.com/tools)[Knowledge --------- Add domain-specific knowledge to your Agents](https://docs.agno.com/knowledge)[Vector Databases ---------------- Add semantic search and retrieval to your Agents](https://docs.agno.com/vectordb)[Storage ------- Persist agent states and conversations in a database](https://docs.agno.com/storage)[Memory ------ Remember user details and session summaries](https://docs.agno.com/agents/memory)[Embeddings ---------- Generate embeddings for your knowledge base](https://docs.agno.com/embedder)[Workflows --------- Build complex workflows with Agents](https://docs.agno.com/workflows)

[Your first Agent](https://docs.agno.com/get-started/agents)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Simple, Fast, and Agnostic](https://docs.agno.com/#simple-fast-and-agnostic)
*   [Key features](https://docs.agno.com/#key-features)
*   [Get Started](https://docs.agno.com/#get-started)
*   [Build with Agno](https://docs.agno.com/#build-with-agno)



================================================================================
Section 3: Content from https://docs.agno.com/introduction
================================================================================

Title: Welcome to Agno - Agno

URL Source: https://docs.agno.com/introduction

Markdown Content:
Welcome to Agno - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Welcome to Agno

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Welcome to Agno
===============

**Agno is a lightweight library for building multi-modal Agents.**

[​](https://docs.agno.com/introduction#simple-fast-and-agnostic)

Simple, Fast, and Agnostic
----------------------------------------------------------------------------------------------

Agno is designed with three core principles:

*   **Simplicity**: No graphs, chains, or convoluted patterns — just pure python.
*   **Uncompromising Performance**: Blazing fast agents with a minimal memory footprint.
*   **Truly Agnostic**: Any model, any provider, any modality. Agno is designed to be the container for AGI.

[​](https://docs.agno.com/introduction#key-features)

Key features
--------------------------------------------------------------------

Here’s why you should build Agents with Agno:

*   **Lightning Fast**: Agent creation is 5000x faster than LangGraph (see [performance](https://github.com/agno-agi/agno#performance)).
*   **Model Agnostic**: Use any model, any provider, no lock-in.
*   **Multi Modal**: Native support for text, image, audio and video.
*   **Multi Agent**: Delegate tasks across a team of specialized agents.
*   **Memory Management**: Store user sessions and agent state in a database.
*   **Knowledge Stores**: Use vector databases for Agentic RAG or dynamic few-shot.
*   **Structured Outputs**: Make Agents respond with structured data.
*   **Monitoring**: Track agent sessions and performance in real-time on [agno.com](https://app.agno.com/).

[​](https://docs.agno.com/introduction#get-started)

Get Started
------------------------------------------------------------------

If you’re new to Agno, start here to build your first Agent.

[Build your first Agent ---------------------- Learn how to build Agents with Agno](https://docs.agno.com/get-started/agents)[Agent Playground ---------------- Chat with your Agents using a beautiful Agent UI](https://docs.agno.com/get-started/playground)[Agent Observability ------------------- Monitor your Agents on [agno.com](https://app.agno.com/)](https://docs.agno.com/get-started/monitoring)

After that, checkout the [Examples Gallery](https://docs.agno.com/examples) to discover real-world applications built with Agno.

[​](https://docs.agno.com/introduction#build-with-agno)

Build with Agno
--------------------------------------------------------------------------

Agno is a battle-tested framework with best-in-class performance, checkout the following guides to dive-in:

[Agents ------ Learn core Agent concepts](https://docs.agno.com/agents)[Models ------ Use any model, any provider, no lock-in](https://docs.agno.com/models)[Tools ----- Use 100s of tools to extend your Agents](https://docs.agno.com/tools)[Knowledge --------- Add domain-specific knowledge to your Agents](https://docs.agno.com/knowledge)[Vector Databases ---------------- Add semantic search and retrieval to your Agents](https://docs.agno.com/vectordb)[Storage ------- Persist agent states and conversations in a database](https://docs.agno.com/storage)[Memory ------ Remember user details and session summaries](https://docs.agno.com/agents/memory)[Embeddings ---------- Generate embeddings for your knowledge base](https://docs.agno.com/embedder)[Workflows --------- Build complex workflows with Agents](https://docs.agno.com/workflows)

[Your first Agent](https://docs.agno.com/get-started/agents)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Simple, Fast, and Agnostic](https://docs.agno.com/introduction#simple-fast-and-agnostic)
*   [Key features](https://docs.agno.com/introduction#key-features)
*   [Get Started](https://docs.agno.com/introduction#get-started)
*   [Build with Agno](https://docs.agno.com/introduction#build-with-agno)



================================================================================
Section 4: Content from https://docs.agno.com/examples/introduction
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/examples/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Examples

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Examples

*   [Introduction](https://docs.agno.com/examples/introduction)
*   Getting Started
    
*   Agents
    
*   Workflows
    
*   Applications
    

##### Agent Concepts

*   Multimodal
    
*   RAG
    
*   Knowledge
    
*   Memory
    
*   Teams
    
*   Async
    
*   Hybrid Search
    
*   Storage
    
*   Tools
    
*   Vector Databases
    
*   Embedders
    

##### Models

*   Anthropic
    
*   AWS Bedrock
    
*   AWS Bedrock Claude
    
*   Azure AI Foundry
    
*   Azure OpenAI
    
*   Cohere
    
*   DeepSeek
    
*   Fireworks
    
*   Gemini
    
*   Groq
    
*   Hugging Face
    
*   Mistral
    
*   NVIDIA
    
*   Ollama
    
*   OpenAI
    
*   Perplexity
    
*   Together
    
*   xAI
    

Examples

Introduction
============

Welcome to Agno’s example gallery! Here you’ll discover examples showcasing everything from **single-agent tasks** to sophisticated **multi-agent workflows**. You can either:

*   Run the examples individually
*   Clone the entire [Agno cookbook](https://github.com/agno-agi/agno/tree/main/cookbook)

Have an interesting example to share? Please consider [contributing](https://github.com/agno-agi/agno-docs) to our growing collection.

[​](https://docs.agno.com/examples/introduction#getting-started)

Getting Started
-----------------------------------------------------------------------------------

If you’re just getting started, follow the [Getting Started](https://docs.agno.com/examples/getting-started) guide for a step-by-step tutorial. The examples build on each other, introducing new concepts and capabilities progressively.

[​](https://docs.agno.com/examples/introduction#use-cases)

Use Cases
-----------------------------------------------------------------------

Build real-world applications with Agno.

[Simple Agents ------------- Simple agents for web scraping, data processing, financial analysis, etc.](https://docs.agno.com/examples/agents)[Advanced Workflows ------------------ Advanced workflows for creating blog posts, investment reports, etc.](https://docs.agno.com/examples/workflows)[Full stack Applications ----------------------- Full stack applications like the LLM OS that come with a UI, database etc.](https://docs.agno.com/examples/apps)

[​](https://docs.agno.com/examples/introduction#agent-concepts)

Agent Concepts
---------------------------------------------------------------------------------

Explore Agent concepts with detailed examples.

[Multimodal ---------- Learn how to use multimodal Agents](https://docs.agno.com/examples/concepts/multimodal)[RAG --- Learn how to use Agentic RAG](https://docs.agno.com/examples/concepts/rag)[Knowledge --------- Add domain-specific knowledge to your Agents](https://docs.agno.com/examples/concepts/knowledge)[Teams ----- Scale your Agents with teams](https://docs.agno.com/examples/concepts/teams)[Async ----- Run Agents asynchronously](https://docs.agno.com/examples/concepts/async)[Hybrid search ------------- Combine semantic and keyword search](https://docs.agno.com/examples/concepts/hybrid-search)[Memory ------ Let Agents remember past conversations](https://docs.agno.com/examples/concepts/memory)[Tools ----- Extend your Agents with 100s or tools](https://docs.agno.com/examples/concepts/tools)[Storage ------- Store Agents sessions in a database](https://docs.agno.com/examples/concepts/storage)[Vector Databases ---------------- Store Knowledge in Vector Databases](https://docs.agno.com/examples/concepts/vectordb)[Embedders --------- Convert text to embeddings to store in VectorDbs](https://docs.agno.com/examples/concepts/embedders)

[​](https://docs.agno.com/examples/introduction#models)

Models
-----------------------------------------------------------------

Explore different models with Agno.

[OpenAI ------ Examples using OpenAI GPT models](https://docs.agno.com/examples/models/openai)[Ollama ------ Examples using Ollama models locally](https://docs.agno.com/examples/models/ollama)[Anthropic --------- Examples using Anthropic models like Claude](https://docs.agno.com/examples/models/anthropic)[Cohere ------ Examples using Cohere command models](https://docs.agno.com/examples/models/cohere)[DeepSeek -------- Examples using DeepSeek models](https://docs.agno.com/examples/models/deepseek)[Gemini ------ Examples using Google Gemini models](https://docs.agno.com/examples/models/gemini)[Groq ---- Examples using Groq’s fast inference](https://docs.agno.com/examples/models/groq)[Mistral ------- Examples using Mistral models](https://docs.agno.com/examples/models/mistral)[Azure ----- Examples using Azure OpenAI](https://docs.agno.com/examples/models/azure)[Fireworks --------- Examples using Fireworks models](https://docs.agno.com/examples/models/fireworks)[AWS --- Examples using Amazon Bedrock](https://docs.agno.com/examples/models/aws)[Hugging Face ------------ Examples using Hugging Face models](https://docs.agno.com/examples/models/huggingface)[NVIDIA ------ Examples using NVIDIA models](https://docs.agno.com/examples/models/nvidia)[Together -------- Examples using Together AI models](https://docs.agno.com/examples/models/together)[Vertex AI --------- Examples using Google Vertex AI models](https://docs.agno.com/examples/models/vertexai)[xAI --- Examples using xAI models](https://docs.agno.com/examples/models/xai)

[Introduction](https://docs.agno.com/examples/getting-started/introduction)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Getting Started](https://docs.agno.com/examples/introduction#getting-started)
*   [Use Cases](https://docs.agno.com/examples/introduction#use-cases)
*   [Agent Concepts](https://docs.agno.com/examples/introduction#agent-concepts)
*   [Models](https://docs.agno.com/examples/introduction#models)



================================================================================
Section 5: Content from https://docs.agno.com/reference/agents/agent
================================================================================

Title: Agent - Agno

URL Source: https://docs.agno.com/reference/agents/agent

Markdown Content:
| `model` | `Optional[Model]` | `None` | Model to use for this Agent |
| `name` | `Optional[str]` | `None` | Agent name |
| `agent_id` | `Optional[str]` | `None` | Agent UUID (autogenerated if not set) |
| `agent_data` | `Optional[Dict[str, Any]]` | `None` | Metadata associated with this agent |
| `introduction` | `Optional[str]` | `None` | Agent introduction. This is added to the chat history when a run is started. |
| `user_id` | `Optional[str]` | `None` | ID of the user interacting with this agent |
| `user_data` | `Optional[Dict[str, Any]]` | `None` | Metadata associated with the user interacting with this agent |
| `session_id` | `Optional[str]` | `None` | Session UUID (autogenerated if not set) |
| `session_name` | `Optional[str]` | `None` | Session name |
| `session_state` | `Optional[Dict[str, Any]]` | `None` | Session state (stored in the database to persist across runs) |
| `context` | `Optional[Dict[str, Any]]` | `None` | Context available for tools and prompt functions |
| `add_context` | `bool` | `False` | If True, add the context to the user prompt |
| `resolve_context` | `bool` | `True` | If True, resolve the context (i.e. call any functions in the context) before running the agent |
| `memory` | `Optional[AgentMemory]` | `None` | Agent Memory |
| `add_history_to_messages` | `bool` | `False` | Add chat history to the messages sent to the Model |
| `num_history_responses` | `int` | `3` | Number of historical responses to add to the messages |
| `knowledge` | `Optional[AgentKnowledge]` | `None` | Agent Knowledge |
| `add_references` | `bool` | `False` | Enable RAG by adding references from AgentKnowledge to the user prompt |
| `retriever` | `Optional[Callable[..., Optional[List[Dict]]]]` | `None` | Function to get references to add to the user\_message |
| `references_format` | `Literal["json", "yaml"]` | `"json"` | Format of the references |
| `storage` | `Optional[AgentStorage]` | `None` | Agent Storage |
| `extra_data` | `Optional[Dict[str, Any]]` | `None` | Extra data stored with this agent |
| `tools` | `Optional[List[Union[Toolkit, Callable, Function]]]` | `None` | A list of tools provided to the Model |
| `show_tool_calls` | `bool` | `False` | Show tool calls in Agent response |
| `tool_call_limit` | `Optional[int]` | `None` | Maximum number of tool calls allowed |
| `tool_choice` | `Optional[Union[str, Dict[str, Any]]]` | `None` | Controls which (if any) tool is called by the model |
| `reasoning` | `bool` | `False` | Enable reasoning by working through the problem step by step |
| `reasoning_model` | `Optional[Model]` | `None` | Model to use for reasoning |
| `reasoning_agent` | `Optional[Agent]` | `None` | Agent to use for reasoning |
| `reasoning_min_steps` | `int` | `1` | Minimum number of reasoning steps |
| `reasoning_max_steps` | `int` | `10` | Maximum number of reasoning steps |
| `read_chat_history` | `bool` | `False` | Add a tool that allows the Model to read the chat history |
| `search_knowledge` | `bool` | `True` | Add a tool that allows the Model to search the knowledge base |
| `update_knowledge` | `bool` | `False` | Add a tool that allows the Model to update the knowledge base |
| `read_tool_call_history` | `bool` | `False` | Add a tool that allows the Model to get the tool call history |
| `system_message` | `Optional[Union[str, Callable, Message]]` | `None` | Provide the system message as a string or function |
| `system_message_role` | `str` | `"system"` | Role for the system message |
| `create_default_system_message` | `bool` | `True` | If True, create a default system message using agent settings |
| `description` | `Optional[str]` | `None` | A description of the Agent that is added to the start of the system message |
| `goal` | `Optional[str]` | `None` | The goal of this task |
| `instructions` | `Optional[Union[str, List[str], Callable]]` | `None` | List of instructions for the agent |
| `expected_output` | `Optional[str]` | `None` | Provide the expected output from the Agent |
| `additional_context` | `Optional[str]` | `None` | Additional context added to the end of the system message |
| `markdown` | `bool` | `False` | If markdown=true, add instructions to format the output using markdown |
| `add_name_to_instructions` | `bool` | `False` | If True, add the agent name to the instructions |
| `add_datetime_to_instructions` | `bool` | `False` | If True, add the current datetime to the instructions |
| `add_state_in_messages` | `bool` | `False` | If True, add the session state variables in messages |
| `add_messages` | `Optional[List[Union[Dict, Message]]]` | `None` | A list of extra messages added after the system message |
| `user_message` | `Optional[Union[List, Dict, str, Callable, Message]]` | `None` | Provide the user message |
| `user_message_role` | `str` | `"user"` | Role for the user message |
| `create_default_user_message` | `bool` | `True` | If True, create a default user message |
| `retries` | `int` | `0` | Number of retries to attempt |
| `delay_between_retries` | `int` | `1` | Delay between retries |
| `exponential_backoff` | `bool` | `False` | If True, the delay between retries is doubled each time |
| `response_model` | `Optional[Type[BaseModel]]` | `None` | Provide a response model to get the response as a Pydantic model |
| `parse_response` | `bool` | `True` | If True, the response is converted into the response\_model |
| `structured_outputs` | `bool` | `False` | Use model enforced structured\_outputs if supported |
| `save_response_to_file` | `Optional[str]` | `None` | Save the response to a file |
| `stream` | `Optional[bool]` | `None` | Stream the response from the Agent |
| `stream_intermediate_steps` | `bool` | `False` | Stream the intermediate steps from the Agent |
| `team` | `Optional[List[Agent]]` | `None` | The team of agents that this agent can transfer tasks to |
| `team_data` | `Optional[Dict[str, Any]]` | `None` | Data shared between team members |
| `role` | `Optional[str]` | `None` | If this Agent is part of a team, this is the role of the agent |
| `respond_directly` | `bool` | `False` | If True, member agent responds directly to user |
| `add_transfer_instructions` | `bool` | `True` | Add instructions for transferring tasks to team members |
| `team_response_separator` | `str` | `"\n"` | Separator between responses from the team |
| `debug_mode` | `bool` | `False` | Enable debug logs |
| `monitoring` | `bool` | `False` | Log Agent information to agno.com for monitoring |
| `telemetry` | `bool` | `True` | Log minimal telemetry for analytics |



================================================================================
Section 6: Content from https://docs.agno.com/changelog/overview
================================================================================

Title: Product updates - Agno

URL Source: https://docs.agno.com/changelog/overview

Markdown Content:
1.1.4
-----

Improvements:
-------------

*   **Gmail Tools**: Added `get_emails_by_thread` and `send_email_reply` methods to `GmailTools`.

Bug Fixes:
----------

*   **Gemini List Parameters**: Fixed issue with functions with list-type parameters in Gemini.
*   **Gemini Safety Parameters**: Fixed issue with passing safety parameters in Gemini.
*   **ChromaDB Multiple Docs:** Fixed issue with loading multiple documents into ChromaDB.
*   **Agentic Chunking:** Fixed an issue where `openai` would be required for chunking even if a model was passed.

1.1.3
-----

Bug Fixes:
----------

*   **Gemini Tool-Call History**: Fixed an issue where Gemini rejected tool-calls from historic messages.

1.1.2
-----

Improvements:
-------------

*   **Reasoning with o3 Models**: Reasoning support added for OpenAI’s o3 models.
    
*   **Gemini embedder update:** Updated the `GeminiEmbedder` to use the new [Google’s genai SDK](https://github.com/googleapis/python-genai). This update introduces a slight change in the interface:
    
    ```
    # Before
    embeddings = GeminiEmbedder("models/text-embedding-004").get_embedding(
        "The quick brown fox jumps over the lazy dog."
    )
    
    # After
    embeddings = GeminiEmbedder("text-embedding-004").get_embedding(
        "The quick brown fox jumps over the lazy dog."
    )
    ```
    

Bug Fixes:
----------

*   **Singlestore Fix:** Fixed issue where when querying singlestore the embeddings column was returning in binary format.
*   **MongoDB Vectorstore Fix:** MongoDB had multiple issues like creating and dropping the collections twice while initialising. All known issues were fixed.
*   **LanceDB Fix:** Fixed various errors on LanceDB and added `on_bad_vectors` as parameters.

1.1.1
-----

Improvements:
-------------

*   **File / Image Uploads on Agent UI:** Agent UI now supports file and image uploads with prompts.
    
    *   Supported file formats: `.pdf` `.csv` `.txt` `.docx` `.json`
    *   Supported image formats: `.png` `.jpeg` `.jpg` `.webp`
*   **Firecrawl Custom API URL**: Allowed users to set a custom API URL for Firecrawl.
    
*   **Updated `ModelsLabTools` Toolkit Constructor**: The constructor in `/libs/agno/tools/models_labs.py` has been updated to accommodate audio generation API calls. This is a breaking change, as the parameters for the `ModelsLabTools` class have changed. The `url` and `fetch_url` parameters have been removed, and API URLs are now decided based on the `file_type` provided by the user.
    
    ```
    MODELS_LAB_URLS = {
        "MP4": "https://modelslab.com/api/v6/video/text2video",
        "MP3": "https://modelslab.com/api/v6/voice/music_gen",
        "GIF": "https://modelslab.com/api/v6/video/text2video",
    }
    
    MODELS_LAB_FETCH_URLS = {
        "MP4": "https://modelslab.com/api/v6/video/fetch",
        "MP3": "https://modelslab.com/api/v6/voice/fetch",
        "GIF": "https://modelslab.com/api/v6/video/fetch",
    }
    ```
    
    The `FileType` enum now includes `MP3` type:
    
    ```
    class FileType(str, Enum):
        MP4 = "mp4"
        GIF = "gif"
        MP3 = "mp3"
    ```
    

Bug Fixes:
----------

*   **Gemini functions with no parameters:** Addressed an issue where Gemini would reject function declarations with empty properties.
*   **Fix exponential memory growth**: Fixed certain cases where the agent memory would grow exponentially.
*   **Chroma DB:** Fixed various issues related to metadata on insertion and search.
*   **Gemini Structured Output**: Fixed a bug where Gemini would not generate structured output correctly.
*   **MistralEmbedder:** Fixed issue with instantiation of `MistralEmbedder`.
*   **Reasoning**: Fixed an issue with setting reasoning models.
*   **Audio Response:** Fixed an issue with streaming audio artefacts to the playground.

1.1.0 - Models Refactor and Cloud Support
-----------------------------------------

Model Improvements:
-------------------

*   **Models Refactor**: A complete overhaul of our models implementation to improve on performance and to have better feature parity across models.
    *   This improves metrics and visibility on the Agent UI as well.
    *   All models now support async-await, with the exception of `AwsBedrock`.
*   **Azure AI Foundry**: We now support all models on Azure AI Foundry. Learn more [here](https://learn.microsoft.com/azure/ai-services/models)..
*   **AWS Bedrock Support**: Our redone AWS Bedrock implementation now supports all Bedrock models. It is important to note [which models support which features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).
*   **Gemini via Google SDK**: With the 1.0.0 release of [Google’s genai SDK](https://github.com/googleapis/python-genai) we could improve our previous implementation of `Gemini`. This will allow for easier integration of Gemini features in future.
*   **Model Failure Retries:** We added better error handling of third-party errors (e.g. Rate-Limit errors) and the agent will now optionally retry with exponential backoff if `exponential_backoff` is set to `True`.

Other Improvements
------------------

*   **Exa Answers Support**: Added support for the [Exa answers](https://docs.exa.ai/reference/answer) capability.
*   **GoogleSearchTools**: Updated the name of `GoogleSearch` to `GoogleSearchTools` for consistency.

Deprecation
-----------

*   Our `Gemini` implementation directly on the Vertex API has been replaced by the Google SDK implementation of `Gemini`.
*   Our `Gemini` implementation via the OpenAI client has been replaced by the Google SDK implementation of `Gemini`.
*   Our `OllamaHermes` has been removed as the implementation of `Ollama` was improved.

Bug Fixes
---------

*   **Team Members Names**: Fixed a bug where teams where team members have non-aphanumeric characters in their names would cause exceptions.

1.0.8
-----

New Features:
-------------

*   **Perplexity Model**: We now support [Perplexity](https://www.perplexity.ai/) as a model provider.
*   **Todoist Toolkit:** Added a toolkit for managing tasks on Todoist.
*   **JSON Reader**: Added a JSON file reader for use in knowledge bases.

Improvements:
-------------

*   **LanceDb**: Implemented `name_exists` function for LanceDb.

Bug Fixes:
----------

*   **Storage growth bug:** Fixed a bug with duplication of `run_messages.messages` for every run in storage.

1.0.7
-----

New Features:
-------------

*   **Google Sheets Toolkit**: Added a basic toolkit for reading, creating and updating Google sheets.
*   **Weviate Vector Store**: Added support for Weviate as a vector store.

Improvements:
-------------

*   **Mistral Async**: Mistral now supports async execution via `agent.arun()` and `agent.aprint_response()`.
*   **Cohere Async**: Cohere now supports async execution via `agent.arun()` and `agent.aprint_response()`.

Bug Fixes:
----------

*   **Retriever as knowledge source**: Added small fix and examples for using the custom `retriever` parameter with an agent.

1.0.6
-----

New Features:
-------------

*   **Google Maps Toolkit**: Added a rich toolkit for Google Maps that includes business discovery, directions, navigation, geocode locations, nearby places, etc.
*   **URL reader and knowledge base**: Added reader and knowledge base that can process any URL and store the text contents in the document store.

Bug Fixes:
----------

*   **Zoom tools fix:** Zoom tools updated to include the auth step and other misc fixes.
*   **Github search\_repositories pagination**: Pagination did not work correctly and this was fixed.

1.0.5
-----

New Features:
-------------

*   **Gmail Tools:** Add tools for Gmail, including mail search, sending mails, etc.

Improvements:
-------------

*   **Exa Toolkit Upgrade:** Added `find_similar` to `ExaTools`
*   **Claude Async:** Claude models can now be used with `await agent.aprint_response()` and `await agent.arun()`.
*   **Mistral Vision:** Mistral vision models are now supported. Various examples were added to illustrate [example](https://github.com/agno-agi/agno/blob/main/cookbook/models/mistral/image_file_input_agent.py).

1.0.4
-----

Bug Fixes:
----------

*   **Claude Tool Invocation:** Fixed issue where Claude was not working with tools that have no parameters.

1.0.3
-----

Improvements:
-------------

*   **OpenAI Reasoning Parameter:** Added a reasoning parameter to OpenAI models.

1.0.2
-----

Improvements:
-------------

*   **Model Client Caching:** Made all models cache the client instantiation, improving Agno agent instantiation time
*   **XTools:** Renamed `TwitterTools` to `XTools` and updated capabilities to be compatible with Twitter API v2.

Bug Fixes:
----------

*   **Agent Dataclass Compatibility:** Removed `slots=True` from the agent dataclass decorator, which was not compatible with Python < 3.10.
*   **AzureOpenAIEmbedder:** Made `AzureOpenAIEmbedder` a dataclass to match other embedders.

1.0.1
-----

Improvement:
------------

*   **Mistral Model Caching:** Enabled caching for Mistral models.

1.0.0 - Agno
------------

This is the major refactor from `phidata` to `agno`, released with the official launch of Agno AI.

See the [migration guide](https://docs.agno.com/how-to/phidata-to-agno) for additional guidance.

Interface Changes:
------------------

*   `phi.model.x` → `agno.models.x`
    
*   `phi.knowledge_base.x` → `agno.knowledge.x` (applies to all knowledge bases)
    
*   `phi.document.reader.xxx` → `agno.document.reader.xxx_reader` (applies to all document readers)
    
*   All Agno toolkits are now suffixed with `Tools`. E.g. `DuckDuckGo` → `DuckDuckGoTools`
    
*   Multi-modal interface updates:
    
    *   `agent.run(images=[])` and `agent.print_response(images=[])` is now of type `Image`
        
        ```
        class Image(BaseModel):
            url: Optional[str] = None  # Remote location for image
            filepath: Optional[Union[Path, str]] = None  # Absolute local location for image
            content: Optional[Any] = None  # Actual image bytes content
            detail: Optional[str] = None # low, medium, high or auto (per OpenAI spec https://platform.openai.com/docs/guides/vision?lang=node#low-or-high-fidelity-image-understanding)
            id: Optional[str] = None
        ```
        
    *   `agent.run(audio=[])` and `agent.print_response(audio=[])` is now of type `Audio`
        
        ```
        class Audio(BaseModel):
            filepath: Optional[Union[Path, str]] = None  # Absolute local location for audio
            content: Optional[Any] = None  # Actual audio bytes content
            format: Optional[str] = None
        ```
        
    *   `agent.run(video=[])` and `agent.print_response(video=[])` is now of type `Video`
        
        ```
        class Video(BaseModel):
            filepath: Optional[Union[Path, str]] = None  # Absolute local location for video
            content: Optional[Any] = None  # Actual video bytes content
        ```
        
    *   `RunResponse.images` is now a list of type `ImageArtifact`
        
        ```
        class ImageArtifact(Media):
            id: str
            url: str  # Remote location for file
            alt_text: Optional[str] = None
        ```
        
    *   `RunResponse.audio` is now a list of type `AudioArtifact`
        
        ```
        class AudioArtifact(Media):
            id: str
            url: Optional[str] = None  # Remote location for file
            base64_audio: Optional[str] = None  # Base64-encoded audio data
            length: Optional[str] = None
            mime_type: Optional[str] = None
        ```
        
    *   `RunResponse.videos` is now a list of type `VideoArtifact`
        
        ```
        class VideoArtifact(Media):
            id: str
            url: str  # Remote location for file
            eta: Optional[str] = None
            length: Optional[str] = None
        ```
        
    *   `RunResponse.response_audio` is now of type `AudioOutput`
        
        ```
        class AudioOutput(BaseModel):
            id: str
            content: str  # Base64 encoded
            expires_at: int
            transcript: str
        ```
        
*   Models:
    
    *   `Hermes` → `OllamaHermes`
    *   `AzureOpenAIChat` → `AzureOpenAI`
    *   `CohereChat` → `Cohere`
    *   `DeepSeekChat` → `DeepSeek`
    *   `GeminiOpenAIChat` → `GeminiOpenAI`
    *   `HuggingFaceChat` → `HuggingFace`
*   Embedders now all take `id` instead of `model` as a parameter. For example
    
    ```
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(
            table_name="recipes",
            db_url=db_url,
            embedder=OllamaEmbedder(id="llama3.2", dimensions=3072),
        ),
    )
    knowledge_base.load(recreate=True)
    ```
    
*   Agent Storage class
    
    *   `PgAgentStorage` → `PostgresDbAgentStorage`
    *   `SqlAgentStorage` → `SqliteDbAgentStorage`
    *   `MongoAgentStorage` → `MongoDbAgentStorage`
    *   `S2AgentStorage` → `SingleStoreDbAgentStorage`
*   Workflow Storage class
    
    *   `SqlWorkflowStorage` → `SqliteDbWorkflowStorage`
    *   `PgWorkflowStorage` → `PostgresDbWorkflowStorage`
    *   `MongoWorkflowStorage` → `MongoDbWorkflowStorage`
*   Knowledge Base
    
    *   `phi.knowledge.pdf.PDFUrlKnowledgeBase` → `agno.knowledge.pdf_url.PDFUrlKnowledgeBase`
    *   `phi.knowledge.csv.CSVUrlKnowledgeBase` → `agno.knowledge.csv_url.CSVUrlKnowledgeBase`
*   Readers
    
    *   `phi.document.reader.arxiv` → `agno.document.reader.arxiv_reader`
    *   `phi.document.reader.docx` → `agno.document.reader.docx_reader`
    *   `phi.document.reader.json` → `agno.document.reader.json_reader`
    *   `phi.document.reader.pdf` → `agno.document.reader.pdf_reader`
    *   `phi.document.reader.s3.pdf` → `agno.document.reader.s3.pdf_reader`
    *   `phi.document.reader.s3.text` → `agno.document.reader.s3.text_reader`
    *   `phi.document.reader.text` → `agno.document.reader.text_reader`
    *   `phi.document.reader.website` → `agno.document.reader.website_reader`

Improvements:
-------------

*   **Dataclasses:** Changed various instances of Pydantic models to dataclasses to improve the speed.
*   Moved `Embedder` class from pydantic to data class

Removals
--------

*   Removed all references to `Assistant`
*   Removed all references to `llm`
*   Removed the `PhiTools` tool
*   On the `Agent` class, `guidelines`, `prevent_hallucinations`, `prevent_prompt_leakage`, `limit_tool_access`, and `task` has been removed. They can be incorporated into the `instructions` parameter as you see fit.

Bug Fixes:
----------

*   **Semantic Chunking:** Fixed semantic chunking by replacing `similarity_threshold` param with `threshold` param.

New Features:
-------------

*   **Evals for Agents:** Introducing Evals to measure the performance, accuracy, and reliability of your Agents.



================================================================================
Section 7: Content from https://docs.agno.com/faq/environment_variables
================================================================================

Title: Setting Environment Variables - Agno

URL Source: https://docs.agno.com/faq/environment_variables

Markdown Content:
Setting Environment Variables - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

FAQs

Setting Environment Variables

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### FAQs

*   [Environment Variables Setup](https://docs.agno.com/faq/environment_variables)
*   [TPM rate limiting](https://docs.agno.com/faq/tpm-issues)
*   [Command line authentication](https://docs.agno.com/faq/cli-auth)
*   [Connecting to Tableplus](https://docs.agno.com/faq/connecting-to-tableplus)
*   [Docker Connection Error](https://docs.agno.com/faq/could-not-connect-to-docker)
*   [OpenAI Key Request While Using Other Models](https://docs.agno.com/faq/openai_key_request_for_other_models)

FAQs

Setting Environment Variables
=============================

To configure your environment for applications, you may need to set environment variables. This guide provides instructions for setting environment variables in both macOS (Shell) and Windows (PowerShell and Windows Command Prompt).

[​](https://docs.agno.com/faq/environment_variables#macos)

macOS
-------------------------------------------------------------------

### 

[​](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-shell)

Setting Environment Variables in Shell

#### 

[​](https://docs.agno.com/faq/environment_variables#temporary-environment-variables)

Temporary Environment Variables

These environment variables will only be available in the current shell session.

Copy

```shell
export VARIABLE_NAME="value"
```

To display the environment variable:

Copy

```shell
echo $VARIABLE_NAME
```

#### 

[​](https://docs.agno.com/faq/environment_variables#permanent-environment-variables)

Permanent Environment Variables

To make environment variables persist across sessions, add them to your shell configuration file (e.g., `.bashrc`, `.bash_profile`, `.zshrc`).

For Zsh:

Copy

```shell
echo 'export VARIABLE_NAME="value"' >> ~/.zshrc
source ~/.zshrc
```

To display the environment variable:

Copy

```shell
echo $VARIABLE_NAME
```

[​](https://docs.agno.com/faq/environment_variables#windows)

Windows
-----------------------------------------------------------------------

### 

[​](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-powershell)

Setting Environment Variables in PowerShell

#### 

[​](https://docs.agno.com/faq/environment_variables#temporary-environment-variables-2)

Temporary Environment Variables

These environment variables will only be available in the current PowerShell session.

Copy

```powershell
$env:VARIABLE_NAME = "value"
```

To display the environment variable:

Copy

```powershell
echo $env:VARIABLE_NAME
```

#### 

[​](https://docs.agno.com/faq/environment_variables#permanent-environment-variables-2)

Permanent Environment Variables

To make environment variables persist across sessions, add them to your PowerShell profile script (e.g., `Microsoft.PowerShell_profile.ps1`).

Copy

```powershell
notepad $PROFILE
```

Add the following line to the profile script:

Copy

```powershell
$env:VARIABLE_NAME = "value"
```

Save and close the file, then reload the profile:

Copy

```powershell
. $PROFILE
```

To display the environment variable:

Copy

```powershell
echo $env:VARIABLE_NAME
```

### 

[​](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-windows-command-prompt)

Setting Environment Variables in Windows Command Prompt

#### 

[​](https://docs.agno.com/faq/environment_variables#temporary-environment-variables-3)

Temporary Environment Variables

These environment variables will only be available in the current Command Prompt session.

Copy

```cmd
set VARIABLE_NAME=value
```

To display the environment variable:

Copy

```cmd
echo %VARIABLE_NAME%
```

#### 

[​](https://docs.agno.com/faq/environment_variables#permanent-environment-variables-3)

Permanent Environment Variables

To make environment variables persist across sessions, you can use the `setx` command:

Copy

```cmd
setx VARIABLE_NAME "value"
```

Note: After setting an environment variable using `setx`, you need to restart the Command Prompt or any applications that need to read the new environment variable.

To display the environment variable in a new Command Prompt session:

Copy

```cmd
echo %VARIABLE_NAME%
```

By following these steps, you can effectively set and display environment variables in macOS Shell, Windows Command Prompt, and PowerShell. This will ensure your environment is properly configured for your applications.

[TPM rate limiting](https://docs.agno.com/faq/tpm-issues)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [macOS](https://docs.agno.com/faq/environment_variables#macos)
*   [Setting Environment Variables in Shell](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-shell)
*   [Temporary Environment Variables](https://docs.agno.com/faq/environment_variables#temporary-environment-variables)
*   [Permanent Environment Variables](https://docs.agno.com/faq/environment_variables#permanent-environment-variables)
*   [Windows](https://docs.agno.com/faq/environment_variables#windows)
*   [Setting Environment Variables in PowerShell](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-powershell)
*   [Temporary Environment Variables](https://docs.agno.com/faq/environment_variables#temporary-environment-variables-2)
*   [Permanent Environment Variables](https://docs.agno.com/faq/environment_variables#permanent-environment-variables-2)
*   [Setting Environment Variables in Windows Command Prompt](https://docs.agno.com/faq/environment_variables#setting-environment-variables-in-windows-command-prompt)
*   [Temporary Environment Variables](https://docs.agno.com/faq/environment_variables#temporary-environment-variables-3)
*   [Permanent Environment Variables](https://docs.agno.com/faq/environment_variables#permanent-environment-variables-3)



================================================================================
Section 8: Content from https://docs.agno.com/hackathon/introduction
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/hackathon/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Hackathon Resources

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Hackathon Resources

*   [Introduction](https://docs.agno.com/hackathon/introduction)
*   [Setup](https://docs.agno.com/hackathon/setup)
*   Examples
    
*   Models
    
*   [Pre-built Replit Template](https://docs.agno.com/hackathon/replit)
*   [🏆 Prizes](https://docs.agno.com/hackathon/prizes)

Hackathon Resources

Introduction
============

Welcome to Agno’s Hackathon Documentation!

Here you’ll find setup guides, examples, and resources to bring your multimodal agents to life. For dedicated hackathon support, join our [discord](https://agno.link/hack-support) where our team is ready to help you.

[​](https://docs.agno.com/hackathon/introduction#quick-start-guide)

Quick Start Guide
----------------------------------------------------------------------------------------

[Setup ----- Get your environment ready for building Agents](https://docs.agno.com/hackathon/setup)[Ready-to-Use Code ----------------- Copy-paste solutions for common use cases](https://agno.link/hack-code)[Replit Template --------------- Fork our pre-built Replit template](https://agno.link/hack-repl)

[​](https://docs.agno.com/hackathon/introduction#text-examples)

Text Examples
--------------------------------------------------------------------------------

[Simple Text Agent ----------------- Agent with text input and output](https://docs.agno.com/hackathon/examples/simple-text-agent)[Agent with Tools ---------------- Agent with tools to search the web](https://docs.agno.com/hackathon/examples/agent-with-tools)[Agent with Knowledge -------------------- Agent with a knowledge base it can search](https://docs.agno.com/hackathon/examples/agent-with-knowledge)[Agent with Structured Outputs ----------------------------- Agent with a structured output (pydantic object)](https://docs.agno.com/hackathon/examples/structured-outputs)[Research Agent -------------- Agent that searches Exa and generates a report in a consistent format](https://docs.agno.com/hackathon/examples/research-agent)[YouTube Agent ------------- Analyze YouTube videos and provide detailed summaries, timestamps, and key points](https://docs.agno.com/hackathon/examples/youtube-agent)

[​](https://docs.agno.com/hackathon/introduction#image-processing-and-generation)

Image Processing & Generation
------------------------------------------------------------------------------------------------------------------

[Image Input + Tools ------------------- Agent that takes image input and makes tool calls to search the web](https://docs.agno.com/hackathon/examples/image-input-with-tools)[Generate Image -------------- Agent that generates images using DALL-E](https://docs.agno.com/hackathon/examples/image-generate)[Image to Structured Output -------------------------- Agent that extracts structured data from images](https://docs.agno.com/hackathon/examples/image-to-structured-output)[Generate Audio from Image ------------------------- Agent that generates audio from an image](https://docs.agno.com/hackathon/examples/image-generate-audio)[Image Input + Output -------------------- Agent that takes an image input and outputs an image](https://docs.agno.com/hackathon/examples/image-input-output)[Image Transcription ------------------- Agent that transcribes images using Mistral](https://docs.agno.com/hackathon/examples/image-transcribe)[Image Search using Giphy ------------------------ Agent that searches for gifs using Giphy](https://docs.agno.com/hackathon/examples/image-gif-seach)

[​](https://docs.agno.com/hackathon/introduction#audio-processing-and-generation)

Audio Processing & Generation
------------------------------------------------------------------------------------------------------------------

[Audio Input ----------- Agent that takes audio input](https://docs.agno.com/hackathon/examples/audio-input)[Audio Input + Output -------------------- Agent that takes audio input and outputs audio](https://docs.agno.com/hackathon/examples/audio-input-output)[Audio Sentiment --------------- Agent that takes audio input and outputs a sentiment analysis](https://docs.agno.com/hackathon/examples/audio-sentiment)[Audio Transcript ---------------- Agent that takes audio input and outputs a transcript of the audio](https://docs.agno.com/hackathon/examples/audio-transcript)[Audio Multi Turn ---------------- Agent that continues an audio input - output conversation](https://docs.agno.com/hackathon/examples/audio-multi-turn)[Audio Generate Podcast ---------------------- Agent that generates a podcast from an audio input](https://docs.agno.com/hackathon/examples/audio-generate-podcast)

[​](https://docs.agno.com/hackathon/introduction#video-processing-and-generation)

Video Processing & Generation
------------------------------------------------------------------------------------------------------------------

[Video Input ----------- Agent that takes video input](https://docs.agno.com/hackathon/examples/video-input)[Video Generation with Models Lab -------------------------------- Agent that generates videos using Models Lab](https://docs.agno.com/hackathon/examples/video-modelslab)[Video Generation with Replicate ------------------------------- Agent that generates videos using Replicate](https://docs.agno.com/hackathon/examples/video-replicate)[Video Captions -------------- Agent that generates captions for videos](https://docs.agno.com/hackathon/examples/video-captions)[Video to Shorts --------------- Agent that converts videos to shorts](https://docs.agno.com/hackathon/examples/video-to-shorts)

[​](https://docs.agno.com/hackathon/introduction#streamlit-applications)

Streamlit Applications
--------------------------------------------------------------------------------------------------

A list of streamlit applications built with Agno that you can use as a starting point for your hackathon project.

[Answer Engine ------------- A powerful answer engine that combines web search and exa search to answer questions](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/answer_engine)[Chess Game ---------- A simple chess game built with Agno](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/chess_team)[Geobuddy -------- Geeography agent that analyzes images to predict locations based on visible cues like landmarks, architecture, and cultural symbols.](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/geobuddy)[Medical Imaging --------------- Medical imaging analysis agent that analyzes medical images and provides detailed findings by utilizing models and external tools.](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/medical_imaging)[Game Generator -------------- Game generator agent that generates games based on user input](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/game_generator)[SQL Agent --------- SQL agent that can query a database and return the results](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/sql_agent)[Podcast Generator ----------------- Agent that generates a podcast from an audio input](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/podcast_generator)[Tic Tac Toe ----------- Tic Tac Toe game](https://github.com/agno-agi/agno/tree/main/cookbook/examples/apps/tic_tac_toe)

[​](https://docs.agno.com/hackathon/introduction#models)

Models
------------------------------------------------------------------

Choose the right model for your project. Each has unique capabilities and strengths.

[Gemini ------ Multimodal examples using Google Gemini](https://docs.agno.com/hackathon/models/gemini)[OpenAI ------ Multimodal examples using OpenAI](https://docs.agno.com/hackathon/models/openai)[Ollama ------ Multimodal examples using Ollama models locally](https://docs.agno.com/hackathon/models/ollama)[Anthropic --------- Multimodal examples using Anthropic models like Claude](https://docs.agno.com/hackathon/models/anthropic)[Groq ---- Multimodal examples using Groq’s fast inference](https://docs.agno.com/hackathon/models/groq)[Mistral ------- Multimodal examples using Mistral models](https://docs.agno.com/hackathon/models/mistral)

[​](https://docs.agno.com/hackathon/introduction#more-examples)

More Examples
--------------------------------------------------------------------------------

*   Browse 100s of other [examples](https://docs.agno.com/examples) and [cookbooks](https://agno.link/cookbooks) for inspiration.

[​](https://docs.agno.com/hackathon/introduction#model-capabilities-at-a-glance)

Model Capabilities at a Glance
------------------------------------------------------------------------------------------------------------------

Here’s a quick comparison of multimodal support across models:

| Model | Image | Audio | Video | Text |
| --- | --- | --- | --- | --- |
| Gemini | ✅ | ✅ | ✅ | ✅ |
| OpenAI | ✅ | ✅ | ❌ | ✅ |
| Anthropic | ✅ | ❌ | ❌ | ✅ |
| Groq | ✅ | ❌ | ❌ | ✅ |
| Mistral | ✅ | ❌ | ❌ | ✅ |

For more details, see our [compatibility matrix](https://docs.agno.com/models/compatibility#multimodal-support).

[Setup](https://docs.agno.com/hackathon/setup)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Quick Start Guide](https://docs.agno.com/hackathon/introduction#quick-start-guide)
*   [Text Examples](https://docs.agno.com/hackathon/introduction#text-examples)
*   [Image Processing & Generation](https://docs.agno.com/hackathon/introduction#image-processing-and-generation)
*   [Audio Processing & Generation](https://docs.agno.com/hackathon/introduction#audio-processing-and-generation)
*   [Video Processing & Generation](https://docs.agno.com/hackathon/introduction#video-processing-and-generation)
*   [Streamlit Applications](https://docs.agno.com/hackathon/introduction#streamlit-applications)
*   [Models](https://docs.agno.com/hackathon/introduction#models)
*   [More Examples](https://docs.agno.com/hackathon/introduction#more-examples)
*   [Model Capabilities at a Glance](https://docs.agno.com/hackathon/introduction#model-capabilities-at-a-glance)



================================================================================
Section 9: Content from https://docs.agno.com/get-started/agents
================================================================================

Title: Your first Agent - Agno

URL Source: https://docs.agno.com/get-started/agents

Markdown Content:
Your first Agent - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Your first Agent

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Your first Agent
================

[​](https://docs.agno.com/get-started/agents#what-are-agents)

What are Agents?
---------------------------------------------------------------------------------

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Instead of a rigid binary definition, let’s think of Agents in terms of agency and autonomy.

*   **Level 0**: Agents with no tools (basic inference tasks).
*   **Level 1**: Agents with tools for autonomous task execution.
*   **Level 2**: Agents with knowledge, combining memory and reasoning.
*   **Level 3**: Teams of agents collaborating on complex workflows.

[​](https://docs.agno.com/get-started/agents#basic-agent)

Basic Agent
------------------------------------------------------------------------

basic\_agent.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

To run the agent, install dependencies and export your `OPENAI_API_KEY`.

1

Setup your virtual environment

Mac

Windows

Copy

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2

Install dependencies

Mac

Windows

Copy

```bash
pip install -U openai agno
```

3

Export your OpenAI key

Mac

Windows

Copy

```bash
export OPENAI_API_KEY=sk-***
```

4

Run the agent

Copy

```shell
python basic_agent.py
```

[​](https://docs.agno.com/get-started/agents#agent-with-tools)

Agent with tools
----------------------------------------------------------------------------------

This basic agent will obviously make up a story, lets give it a tool to search the web.

agent\_with\_tools.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

Install dependencies and run the Agent

1

Install dependencies

Mac

Windows

Copy

```bash
pip install -U duckduckgo-search
```

2

Run the agent

Copy

```shell
python agent_with_tools.py
```

Now you should see a much more relevant result.

[​](https://docs.agno.com/get-started/agents#agent-with-knowledge)

Agent with knowledge
------------------------------------------------------------------------------------------

Agents can store knowledge in a vector database and use it for RAG or dynamic few-shot learning.

**Agno agents use Agentic RAG** by default, which means they will search their knowledge base for the specific information they need to achieve their task.

agent\_with\_knowledge.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What is the history of Thai curry?", stream=True)
```

Install dependencies and run the Agent

1

Install dependencies

Mac

Windows

Copy

```bash
pip install -U lancedb tantivy pypdf duckduckgo-search
```

2

Run the agent

Copy

```shell
python agent_with_knowledge.py
```

[​](https://docs.agno.com/get-started/agents#multi-agent-teams)

Multi Agent Teams
------------------------------------------------------------------------------------

Agents work best when they have a singular purpose, a narrow scope and a small number of tools. When the number of tools grows beyond what the language model can handle or the tools belong to different categories, use a team of agents to spread the load.

agent\_team.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
```

Install dependencies and run the Agent team

1

Install dependencies

Mac

Windows

Copy

```bash
pip install -U duckduckgo-search yfinance
```

2

Run the agent

Copy

```shell
python agent_team.py
```

[​](https://docs.agno.com/get-started/agents#debugging)

Debugging
--------------------------------------------------------------------

Want to see the system prompt, user messages and tool calls?

Agno includes a built-in debugger that will print debug logs in the terminal. Set `debug_mode=True` on any agent or set `AGNO_DEBUG=true` in your environment.

debugging.py

Copy

```python
from agno.agent import Agent

agent = Agent(markdown=True, debug_mode=True)
agent.print_response("Share a 2 sentence horror story")
```

Run the agent to view debug logs in the terminal:

Copy

```shell
python debugging.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/debugging.png)

[Welcome to Agno](https://docs.agno.com/introduction)[Agent Playground](https://docs.agno.com/get-started/playground)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [What are Agents?](https://docs.agno.com/get-started/agents#what-are-agents)
*   [Basic Agent](https://docs.agno.com/get-started/agents#basic-agent)
*   [Agent with tools](https://docs.agno.com/get-started/agents#agent-with-tools)
*   [Agent with knowledge](https://docs.agno.com/get-started/agents#agent-with-knowledge)
*   [Multi Agent Teams](https://docs.agno.com/get-started/agents#multi-agent-teams)
*   [Debugging](https://docs.agno.com/get-started/agents#debugging)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/debugging.png)



================================================================================
Section 10: Content from https://docs.agno.com/get-started/playground
================================================================================

Title: Agent Playground - Agno

URL Source: https://docs.agno.com/get-started/playground

Markdown Content:
Agent Playground - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Agent Playground

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Agent Playground
================

**Agno provides a beautiful Agent UI for interacting with your agents.**

![Image 3](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent_playground.png)

Agent Playground

No data is sent to [agno.com](https://app.agno.com/), all agent data is stored locally in your sqlite database.

[​](https://docs.agno.com/get-started/playground#running-playground-locally)

Running Playground Locally
----------------------------------------------------------------------------------------------------------

Let’s run the playground application locally so we can chat with our Agents using the Agent UI. Create a file `playground.py`

playground.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    # Store the agent sessions in a sqlite database
    storage=SqliteAgentStorage(table_name="web_agent", db_file=agent_storage),
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=5,
    # Adds markdown formatting to the messages
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

app = Playground(agents=[web_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
```

Remember to export your `OPENAI_API_KEY` before running the playground application.

Make sure the `serve_playground_app()` points to the file that contains your `Playground` app.

[​](https://docs.agno.com/get-started/playground#authenticate-with-agno)

Authenticate with Agno
--------------------------------------------------------------------------------------------------

Authenticate with agno.com so your local application can let agno know that you are running a playground application. Run:

No data is sent to agno.com, only that you’re running a playground application at port 7777.

Copy

```shell
ag setup
```

\[or\] export your `AGNO_API_KEY` from [app.agno.com](https://app.agno.com/)

Mac

Windows

Copy

```bash
export AGNO_API_KEY=ag-***
```

[​](https://docs.agno.com/get-started/playground#run-the-playground-app)

Run the playground app
--------------------------------------------------------------------------------------------------

Install dependencies and run your playground application:

Copy

```shell
pip install openai duckduckgo-search yfinance sqlalchemy 'fastapi[standard]' agno

python playground.py
```

[​](https://docs.agno.com/get-started/playground#view-the-playground)

View the playground
--------------------------------------------------------------------------------------------

*   Open the link provided or navigate to `http://app.agno.com/playground` (login required)
*   Select the `localhost:7777` endpoint and start chatting with your agents!

[Your first Agent](https://docs.agno.com/get-started/agents)[Agent Observability](https://docs.agno.com/get-started/monitoring)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Running Playground Locally](https://docs.agno.com/get-started/playground#running-playground-locally)
*   [Authenticate with Agno](https://docs.agno.com/get-started/playground#authenticate-with-agno)
*   [Run the playground app](https://docs.agno.com/get-started/playground#run-the-playground-app)
*   [View the playground](https://docs.agno.com/get-started/playground#view-the-playground)

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent_playground.png)



================================================================================
Section 11: Content from https://docs.agno.com/get-started/monitoring
================================================================================

Title: Agent Observability - Agno

URL Source: https://docs.agno.com/get-started/monitoring

Markdown Content:
Agent Observability - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Agent Observability

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Agent Observability
===================

[​](https://docs.agno.com/get-started/monitoring#monitoring)

Monitoring
--------------------------------------------------------------------------

Want to monitor and track your Agents?

Agno provides built-in monitoring capabilities that track session and performance metrics through [app.agno.com](https://app.agno.com/). To enable monitoring:

1.  **Authenticate** (one of these methods):
    
    *   Run `agno setup` in your terminal
    *   Export `AGNO_API_KEY=***` in your environment
2.  **Enable monitoring** (one of these methods):
    
    *   Set `monitoring=True` when creating an Agent
    *   Set `AGNO_MONITOR=true` in your environment

Create a file `monitoring.py` with the following code:

monitoring.py

Copy

```python
from agno.agent import Agent

agent = Agent(markdown=True, monitoring=True)
agent.print_response("Share a 2 sentence horror story")
```

Run the agent locally and view your sessions at [app.agno.com/sessions](https://app.agno.com/sessions)

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/monitoring.png)

Facing issues? Check out our [troubleshooting guide](https://docs.agno.com/faq/cli-auth)

[Agent Playground](https://docs.agno.com/get-started/playground)[Community](https://docs.agno.com/get-started/community)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Monitoring](https://docs.agno.com/get-started/monitoring#monitoring)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/monitoring.png)



================================================================================
Section 12: Content from https://docs.agno.com/get-started/community
================================================================================

Title: Community - Agno

URL Source: https://docs.agno.com/get-started/community

Markdown Content:
Community - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Get Started

Community

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Get Started

Community
=========

[​](https://docs.agno.com/get-started/community#building-something-amazing-with-agno)

Building something amazing with Agno?
------------------------------------------------------------------------------------------------------------------------------

Share what you’re building on [X](https://agno.link/x) or join our [Discord](https://agno.link/discord) to connect with other developers and explore new ideas together.

[​](https://docs.agno.com/get-started/community#got-questions)

Got questions?
--------------------------------------------------------------------------------

Head over to our [community forum](https://agno.link/community) for help and insights from the team.

[​](https://docs.agno.com/get-started/community#looking-for-dedicated-support)

Looking for dedicated support?
----------------------------------------------------------------------------------------------------------------

We’ve helped many companies turn ideas into production-grade AI products. Here’s how we can help you:

1.  **Build agents** tailored to your needs.
2.  **Integrate your agents** with your products.
3.  **Monitor, improve and scale** your AI systems.

[Book a call](https://cal.com/team/agno/intro) with us to get started. Our prices start at **$16k/month** and we specialize in taking companies from idea to production within 3 months.

[Agent Observability](https://docs.agno.com/get-started/monitoring)[Introduction](https://docs.agno.com/agents/introduction)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Building something amazing with Agno?](https://docs.agno.com/get-started/community#building-something-amazing-with-agno)
*   [Got questions?](https://docs.agno.com/get-started/community#got-questions)
*   [Looking for dedicated support?](https://docs.agno.com/get-started/community#looking-for-dedicated-support)



================================================================================
Section 13: Content from https://docs.agno.com/agents/run
================================================================================

Title: Agent.run() - Agno

URL Source: https://docs.agno.com/agents/run

Markdown Content:
Use the `Agent.run()` function to run the agent and return the response as a `RunResponse` object or a stream of `RunResponse` objects.

RunResponse
-----------

The `Agent.run()` function returns either a `RunResponse` object or an `Iterator[RunResponse]` when `stream=True`. It has the following attributes:

### RunResponse Attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `content` | `Any` | `None` | Content of the response. |
| `content_type` | `str` | `"str"` | Specifies the data type of the content. |
| `context` | `List[MessageContext]` | `None` | The context added to the response for RAG. |
| `event` | `str` | `RunEvent.run_response.value` | Event type of the response. |
| `event_data` | `Dict[str, Any]` | `None` | Data associated with the event. |
| `messages` | `List[Message]` | `None` | A list of messages included in the response. |
| `metrics` | `Dict[str, Any]` | `None` | Usage metrics of the run. |
| `model` | `str` | `None` | The model used in the run. |
| `run_id` | `str` | `None` | Run Id. |
| `agent_id` | `str` | `None` | Agent Id for the run. |
| `session_id` | `str` | `None` | Session Id for the run. |
| `tools` | `List[Dict[str, Any]]` | `None` | List of tools provided to the model. |
| `images` | `List[Image]` | `None` | List of images the model produced. |
| `videos` | `List[Video]` | `None` | List of videos the model produced. |
| `audio` | `List[Audio]` | `None` | List of audio snippets the model produced. |
| `response_audio` | `ModelResponseAudio` | `None` | The model’s raw response in audio. |
| `created_at` | `int` | \- | Unix timestamp of the response creation. |
| `extra_data` | `RunResponseExtraData` | `None` | Extra data containing optional fields like `references`, `add_messages`, `history`, `reasoning_steps`, and `reasoning_messages`. |

*   [RunResponse](https://docs.agno.com/agents/run#runresponse)
*   [RunResponse Attributes](https://docs.agno.com/agents/run#runresponse-attributes)



================================================================================
Section 14: Content from https://docs.agno.com/agents/structured-output
================================================================================

Title: Structured Output - Agno

URL Source: https://docs.agno.com/agents/structured-output

Markdown Content:
Structured Output - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Structured Output

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Structured Output
=================

One of our favorite features is using Agents to generate structured data (i.e. a pydantic model). Use this feature to extract features, classify data, produce fake data etc. The best part is that they work with function calls, knowledge bases and all other features.

[​](https://docs.agno.com/agents/structured-output#example)

Example
----------------------------------------------------------------------

Let’s create an Movie Agent to write a `MovieScript` for us.

movie\_agent.py

Copy

```python
from typing import List
from rich.pretty import pprint
from pydantic import BaseModel, Field
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat

class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(
        ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

# Agent that uses JSON mode
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You write movie scripts.",
    response_model=MovieScript,
)
# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You write movie scripts.",
    response_model=MovieScript,
    structured_outputs=True,
)

# Get the response in a variable
# json_mode_response: RunResponse = json_mode_agent.run("New York")
# pprint(json_mode_response.content)
# structured_output_response: RunResponse = structured_output_agent.run("New York")
# pprint(structured_output_response.content)

json_mode_agent.print_response("New York")
structured_output_agent.print_response("New York")
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

python movie_agent.py
```

The output is an object of the `MovieScript` class, here’s how it looks:

Copy

```python
# Using JSON mode
MovieScript(
│   setting='The bustling streets of New York City, filled with skyscrapers, secret alleyways, and hidden underground passages.',
│   ending='The protagonist manages to thwart an international conspiracy, clearing his name and winning the love of his life back.',
│   genre='Thriller',
│   name='Shadows in the City',
│   characters=['Alex Monroe', 'Eva Parker', 'Detective Rodriguez', 'Mysterious Mr. Black'],
│   storyline="When Alex Monroe, an ex-CIA operative, is framed for a crime he didn't commit, he must navigate the dangerous streets of New York to clear his name. As he uncovers a labyrinth of deceit involving the city's most notorious crime syndicate, he enlists the help of an old flame, Eva Parker. Together, they race against time to expose the true villain before it's too late."
)

# Use the structured output
MovieScript(
│   setting='In the bustling streets and iconic skyline of New York City.',
│   ending='Isabella and Alex, having narrowly escaped the clutches of the Syndicate, find themselves standing at the top of the Empire State Building. As the glow of the setting sun bathes the city, they share a victorious kiss. Newly emboldened and as an unstoppable duo, they vow to keep NYC safe from any future threats.',
│   genre='Action Thriller',
│   name='The NYC Chronicles',
│   characters=['Isabella Grant', 'Alex Chen', 'Marcus Kane', 'Detective Ellie Monroe', 'Victor Sinclair'],
│   storyline='Isabella Grant, a fearless investigative journalist, uncovers a massive conspiracy involving a powerful syndicate plotting to control New York City. Teaming up with renegade cop Alex Chen, they must race against time to expose the culprits before the city descends into chaos. Dodging danger at every turn, they fight to protect the city they love from imminent destruction.'
)
```

[​](https://docs.agno.com/agents/structured-output#developer-resources)

Developer Resources
----------------------------------------------------------------------------------------------

*   View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/async/structured_output.py)

[Agent.run()](https://docs.agno.com/agents/run)[Multimodal Agents](https://docs.agno.com/agents/multimodal)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Example](https://docs.agno.com/agents/structured-output#example)
*   [Developer Resources](https://docs.agno.com/agents/structured-output#developer-resources)



================================================================================
Section 15: Content from https://docs.agno.com/agents/multimodal
================================================================================

Title: Multimodal Agents - Agno

URL Source: https://docs.agno.com/agents/multimodal

Markdown Content:
Multimodal Agents - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Multimodal Agents

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Multimodal Agents
=================

Agno agents support text, image, audio and video inputs and can generate text, image, audio and video outputs. For a complete overview, please checkout the [compatibility matrix](https://docs.agno.com/models/compatibility).

[​](https://docs.agno.com/agents/multimodal#multimodal-inputs-to-an-agent)

Multimodal inputs to an agent
-----------------------------------------------------------------------------------------------------------

Let’s create an agent that can understand images and make tool calls as needed

### 

[​](https://docs.agno.com/agents/multimodal#image-agent)

Image Agent

image\_agent.py

Copy

```python
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)
```

Run the agent:

Copy

```shell
python image_agent.py
```

Similar to images, you can also use audio and video as an input.

### 

[​](https://docs.agno.com/agents/multimodal#audio-agent)

Audio Agent

audio\_agent.py

Copy

```python
import base64

import requests
from agno.agent import Agent, RunResponse  # noqa
from agno.media import Audio
from agno.models.openai import OpenAIChat

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content

agent = Agent(
    model=OpenAIChat(id="gpt-4o-audio-preview", modalities=["text"]),
    markdown=True,
)
agent.print_response(
    "What is in this audio?", audio=[Audio(content=wav_data, format="wav")]
)
```

### 

[​](https://docs.agno.com/agents/multimodal#video-agent)

Video Agent

Currently Agno only supports video as an input for Gemini models.

video\_agent.py

Copy

```python
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

# Please download "GreatRedSpot.mp4" using
# wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4
video_path = Path(__file__).parent.joinpath("GreatRedSpot.mp4")

agent.print_response("Tell me about this video", videos=[Video(filepath=video_path)])
```

[​](https://docs.agno.com/agents/multimodal#multimodal-outputs-from-an-agent)

Multimodal outputs from an agent
-----------------------------------------------------------------------------------------------------------------

Similar to providing multimodal inputs, you can also get multimodal outputs from an agent.

### 

[​](https://docs.agno.com/agents/multimodal#image-generation)

Image Generation

The following example demonstrates how to generate an image using DALL-E with an agent.

image\_agent.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DalleTools()],
    description="You are an AI agent that can generate images using DALL-E.",
    instructions="When the user asks you to create an image, use the `create_image` tool to create the image.",
    markdown=True,
    show_tool_calls=True,
)

image_agent.print_response("Generate an image of a white siamese cat")

images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(image_url)
```

### 

[​](https://docs.agno.com/agents/multimodal#audio-response)

Audio Response

The following example demonstrates how to obtain both text and audio responses from an agent. The agent will respond with text and audio bytes that can be saved to a file.

audio\_agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)
response: RunResponse = agent.run("Tell me a 5 second scary story")

# Save the response audio to a file
if response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/scary_story.wav"
    )
```

[​](https://docs.agno.com/agents/multimodal#multimodal-inputs-and-outputs-together)

Multimodal inputs and outputs together
-----------------------------------------------------------------------------------------------------------------------------

You can create Agents that can take multimodal inputs and return multimodal outputs. The following example demonstrates how to provide a combination of audio and text inputs to an agent and obtain both text and audio outputs.

### 

[​](https://docs.agno.com/agents/multimodal#audio-input-and-audio-output)

Audio input and Audio output

audio\_agent.py

Copy

```python
import base64

import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)

agent.run("What's in these recording?", audio=[Audio(content=wav_data, format="wav")])

if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/result.wav"
    )
```

[Structured Output](https://docs.agno.com/agents/structured-output)[Prompts](https://docs.agno.com/agents/prompts)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Multimodal inputs to an agent](https://docs.agno.com/agents/multimodal#multimodal-inputs-to-an-agent)
*   [Image Agent](https://docs.agno.com/agents/multimodal#image-agent)
*   [Audio Agent](https://docs.agno.com/agents/multimodal#audio-agent)
*   [Video Agent](https://docs.agno.com/agents/multimodal#video-agent)
*   [Multimodal outputs from an agent](https://docs.agno.com/agents/multimodal#multimodal-outputs-from-an-agent)
*   [Image Generation](https://docs.agno.com/agents/multimodal#image-generation)
*   [Audio Response](https://docs.agno.com/agents/multimodal#audio-response)
*   [Multimodal inputs and outputs together](https://docs.agno.com/agents/multimodal#multimodal-inputs-and-outputs-together)
*   [Audio input and Audio output](https://docs.agno.com/agents/multimodal#audio-input-and-audio-output)



================================================================================
Section 16: Content from https://docs.agno.com/agents/prompts
================================================================================

Title: Prompts - Agno

URL Source: https://docs.agno.com/agents/prompts

Markdown Content:
We prompt Agents using `description` and `instructions` and a number of other settings. These settings are used to build the **system** message that is sent to the language model.

Understanding how these prompts are created will help you build better Agents.

The 2 key parameters are:

1.  **Description**: A description that guides the overall behaviour of the agent.
2.  **Instructions**: A list of precise, task-specific instructions on how to achieve its goal.

System message
--------------

The system message is created using `description`, `instructions` and a number of other settings. The `description` is added to the start of the system message and `instructions` are added as a list after `Instructions`. For example:

Will translate to (set `debug_mode=True` to view the logs):

Set the system message directly
-------------------------------

You can manually set the system message using the `system_message` parameter.

User message
------------

The input `message` sent to the `Agent.run()` or `Agent.print_response()` functions is used as the user message.

Default system message
----------------------

The Agent creates a default system message that can be customized using the following parameters:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `description` | `str` | `None` | A description of the Agent that is added to the start of the system message. |
| `task` | `str` | `None` | Describe the task the agent should achieve. |
| `instructions` | `List[str]` | `None` | List of instructions added to the system prompt in `<instructions>` tags. Default instructions are also created depending on values for `markdown`, `output_model` etc. |
| `additional_context` | `str` | `None` | Additional context added to the end of the system message. |
| `expected_output` | `str` | `None` | Provide the expected output from the Agent. This is added to the end of the system message. |
| `extra_instructions` | `List[str]` | `None` | List of extra instructions added to the default system prompt. Use these when you want to add some extra instructions at the end of the default instructions. |
| `prevent_hallucinations` | `bool` | `False` | If True, add instructions to return “I don’t know” when the agent does not know the answer. |
| `prevent_prompt_injection` | `bool` | `False` | If True, add instructions to prevent prompt injection attacks. |
| `limit_tool_access` | `bool` | `False` | If True, add instructions for limiting tool access to the default system prompt if tools are provided |
| `markdown` | `bool` | `False` | Add an instruction to format the output using markdown. |
| `add_datetime_to_instructions` | `bool` | `False` | If True, add the current datetime to the prompt to give the agent a sense of time. This allows for relative times like “tomorrow” to be used in the prompt |
| `system_prompt` | `str` | `None` | System prompt: provide the system prompt as a string |
| `system_prompt_template` | `PromptTemplate` | `None` | Provide the system prompt as a PromptTemplate. |
| `use_default_system_message` | `bool` | `True` | If True, build a default system message using agent settings and use that. |
| `system_message_role` | `str` | `system` | Role for the system message. |

Default user message
--------------------

The Agent creates a default user message, which is either the input message or a message with the `context` if `enable_rag=True`. The default user message can be customized using:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `enable_rag` | `bool` | `False` | Enable RAG by adding references from the knowledge base to the prompt. |
| `add_rag_instructions` | `bool` | `False` | If True, adds instructions for using the RAG to the system prompt (if knowledge is also provided). For example: add an instruction to prefer information from the knowledge base over its training data. |
| `add_history_to_messages` | `bool` | `False` | If true, adds the chat history to the messages sent to the Model. |
| `num_history_responses` | `int` | `3` | Number of historical responses to add to the messages. |
| `user_prompt` | `Union[List, Dict, str]` | `None` | Provide the user prompt as a string. Note: this will ignore the message sent to the run function. |
| `user_prompt_template` | `PromptTemplate` | `None` | Provide the user prompt as a PromptTemplate. |
| `use_default_user_message` | `bool` | `True` | If True, build a default user prompt using references and chat history. |
| `user_message_role` | `str` | `user` | Role for the user message. |



================================================================================
Section 17: Content from https://docs.agno.com/agents/tools
================================================================================

Title: Tools - Agno

URL Source: https://docs.agno.com/agents/tools

Markdown Content:
**Agents use tools to take actions and interact with external systems**.

Tools are functions that an Agent can run to achieve tasks. For example: searching the web, running SQL, sending an email or calling APIs. You can use any python function as a tool or use a pre-built **toolkit**. The general syntax is:

Agno provides many pre-built **toolkits** that you can add to your Agents. For example, let’s use the DuckDuckGo toolkit to search the web.

For more control, write your own python functions and add them as tools to an Agent. For example, here’s how to add a `get_top_hackernews_stories` tool to an Agent.

Read more about:

*   [Available toolkits](https://docs.agno.com/tools/toolkits)
*   [Using functions as tools](https://docs.agno.com/tools/functions)

Attributes
----------

The following attributes allow an `Agent` to use tools

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `tools` | `List[Union[Tool, Toolkit, Callable, Dict, Function]]` | \- | A list of tools provided to the Model. Tools are functions the model may generate JSON inputs for. |
| `show_tool_calls` | `bool` | `False` | Print the signature of the tool calls in the Model response. |
| `tool_call_limit` | `int` | \- | Maximum number of tool calls allowed. |
| `tool_choice` | `Union[str, Dict[str, Any]]` | \- | Controls which (if any) tool is called by the model. “none” means the model will not call a tool and instead generates a message. “auto” means the model can pick between generating a message or calling a tool. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. “none” is the default when no tools are present. “auto” is the default if tools are present. |
| `read_chat_history` | `bool` | `False` | Add a tool that allows the Model to read the chat history. |
| `search_knowledge` | `bool` | `False` | Add a tool that allows the Model to search the knowledge base (aka Agentic RAG). |
| `update_knowledge` | `bool` | `False` | Add a tool that allows the Model to update the knowledge base. |
| `read_tool_call_history` | `bool` | `False` | Add a tool that allows the Model to get the tool call history. |

Developer Resources
-------------------

*   View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/tools)

*   [Using a Toolkit](https://docs.agno.com/agents/tools#using-a-toolkit)
*   [Writing your own Tools](https://docs.agno.com/agents/tools#writing-your-own-tools)
*   [Attributes](https://docs.agno.com/agents/tools#attributes)
*   [Developer Resources](https://docs.agno.com/agents/tools#developer-resources)



================================================================================
Section 18: Content from https://docs.agno.com/agents/knowledge
================================================================================

Title: Knowledge - Agno

URL Source: https://docs.agno.com/agents/knowledge

Markdown Content:
Knowledge - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Knowledge

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Knowledge
=========

**Agents use knowledge to supplement their training data with domain expertise**.

Knowledge is stored in a vector database and provides agents with business context at query time, helping them respond in a context-aware manner. The general syntax is:

Copy

```python
from agno.agent import Agent, AgentKnowledge

# Create a knowledge base for the Agent
knowledge_base = AgentKnowledge(vector_db=...)

# Add information to the knowledge base
knowledge_base.load_text("The sky is blue")

# Add the knowledge base to the Agent and
# give it a tool to search the knowledge base as needed
agent = Agent(knowledge=knowledge_base, search_knowledge=True)
```

You can give your agent access to your knowledge base in the following ways:

*   You can set `search_knowledge=True` to provide a `search_knowledge_base()` tool to your agent. This is automatically added if you provide a knowledgebase.
*   You can set `add_references=True` to automatically add references from the knowledge base. Optionally pass your own `retriever` callable with the following signature:

Copy

```
def retriever(agent: Agent, query: str, num_documents: Optional[int], **kwargs) -> Optional[list[dict]]:
  ...
```

*   You can set `update_knowledge=True` to provide a `add_to_knowledge()` tool to your agent allowing it to update the knowledgebase.

[​](https://docs.agno.com/agents/knowledge#vector-databases)

Vector Databases
--------------------------------------------------------------------------------

While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly. Here’s how vector databases are used with Agents:

1

Chunk the information

Break down the knowledge into smaller chunks to ensure our search query returns only relevant results.

2

Load the knowledge base

Convert the chunks into embedding vectors and store them in a vector database.

3

Search the knowledge base

When the user sends a message, we convert the input message into an embedding and “search” for nearest neighbors in the vector database.

[​](https://docs.agno.com/agents/knowledge#example-rag-agent-with-a-pdf-knowledge-base)

Example: RAG Agent with a PDF Knowledge Base
---------------------------------------------------------------------------------------------------------------------------------------

Let’s build a **RAG Agent** that answers questions from a PDF.

### 

[​](https://docs.agno.com/agents/knowledge#step-1-run-pgvector)

Step 1: Run PgVector

Let’s use `PgVector` as our vector db as it can also provide storage for our Agents.

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

Copy

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agno/pgvector:16
```

### 

[​](https://docs.agno.com/agents/knowledge#step-2-traditional-rag)

Step 2: Traditional RAG

Retrieval Augmented Generation (RAG) means **“stuffing the prompt with relevant information”** to improve the model’s response. This is a 2 step process:

1.  Retrieve relevant information from the knowledge base.
2.  Augment the prompt to provide context to the model.

Let’s build a **traditional RAG** Agent that answers questions from a PDF of recipes.

1

Install libraries

Install the required libraries using pip

Mac

Windows

Copy

```bash
pip install -U pgvector pypdf "psycopg[binary]" sqlalchemy
```

2

Create a Traditional RAG Agent

Create a file `traditional_rag.py` with the following contents

traditional\_rag.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    # Read PDF from this URL
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Store embeddings in the `ai.recipes` table
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
# Load the knowledge base: Comment after first run
knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Enable RAG by adding references from AgentKnowledge to the user prompt.
    add_references=True,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=False,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup")
```

3

Run the agent

Run the agent (it takes a few seconds to load the knowledge base).

Mac

Windows

Copy

```bash
python traditional_rag.py
```

  

How to use local PDFs

If you want to use local PDFs, use a `PDFKnowledgeBase` instead

agent.py

Copy

```python
from agno.knowledge.pdf import PDFKnowledgeBase

...
knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)
...
```

### 

[​](https://docs.agno.com/agents/knowledge#step-3-agentic-rag)

Step 3: Agentic RAG

With traditional RAG above, `add_references=True` always adds information from the knowledge base to the prompt, regardless of whether it is relevant to the question or helpful.

With Agentic RAG, we let the Agent decide **if** it needs to access the knowledge base and what search parameters it needs to query the knowledge base.

Set `search_knowledge=True` and `read_chat_history=True`, giving the Agent tools to search its knowledge and chat history on demand.

1

Create an Agentic RAG Agent

Create a file `agentic_rag.py` with the following contents

agentic\_rag.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
# Load the knowledge base: Comment out after first run
knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Add a tool to search the knowledge base which enables agentic RAG.
    search_knowledge=True,
    # Add a tool to read chat history.
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What was my last question?", markdown=True)
```

2

Run the agent

Run the agent

Mac

Windows

Copy

```bash
python agentic_rag.py
```

Notice how it searches the knowledge base and chat history when needed

[​](https://docs.agno.com/agents/knowledge#attributes)

Attributes
--------------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `knowledge` | `AgentKnowledge` | `None` | Provides the knowledge base used by the agent. |
| `search_knowledge` | `bool` | `True` | Adds a tool that allows the Model to search the knowledge base (aka Agentic RAG). Enabled by default when `knowledge` is provided. |
| `add_references` | `bool` | `False` | Enable RAG by adding references from AgentKnowledge to the user prompt. |
| `retriever` | `Callable[..., Optional[list[dict]]]` | `None` | Function to get context to add to the user message. This function is called when add\_references is True. |
| `context_format` | `Literal['json', 'yaml']` | `json` | Specifies the format for RAG, either “json” or “yaml”. |
| `add_context_instructions` | `bool` | `False` | If True, add instructions for using the context to the system prompt (if knowledge is also provided). For example: add an instruction to prefer information from the knowledge base over its training data. |

[​](https://docs.agno.com/agents/knowledge#developer-resources)

Developer Resources
--------------------------------------------------------------------------------------

*   View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/knowledge)

[Tools](https://docs.agno.com/agents/tools)[Memory](https://docs.agno.com/agents/memory)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Vector Databases](https://docs.agno.com/agents/knowledge#vector-databases)
*   [Example: RAG Agent with a PDF Knowledge Base](https://docs.agno.com/agents/knowledge#example-rag-agent-with-a-pdf-knowledge-base)
*   [Step 1: Run PgVector](https://docs.agno.com/agents/knowledge#step-1-run-pgvector)
*   [Step 2: Traditional RAG](https://docs.agno.com/agents/knowledge#step-2-traditional-rag)
*   [Step 3: Agentic RAG](https://docs.agno.com/agents/knowledge#step-3-agentic-rag)
*   [Attributes](https://docs.agno.com/agents/knowledge#attributes)
*   [Developer Resources](https://docs.agno.com/agents/knowledge#developer-resources)



================================================================================
Section 19: Content from https://docs.agno.com/agents/memory
================================================================================

Title: Memory - Agno

URL Source: https://docs.agno.com/agents/memory

Markdown Content:
Agno provides 3 types of memory for Agents:

1.  **Chat History:** The message history of the session. Agno will store the sessions in a database for you, and retrieve them when you resume a session.
2.  **User Memories:** Notes and insights about the user, this helps the model personalize the response to the user.
3.  **Summaries:** A summary of the conversation, which is added to the prompt when chat history gets too long.

Before we dive in, let’s understand the terminology:

*   **Session:** Each conversation with an Agent is called a **session**. Sessions are identified by a `session_id`.
*   **Run:** Every interaction (i.e. chat) within a session is called a **run**. Runs are identified by a `run_id`.
*   **Messages:** are the individual messages sent to and received from the model. They have a `role` (`system`, `user` or `assistant`) and `content`.

Built-in Memory
---------------

Every Agent comes with built-in memory that can be used to access the historical **runs** and **messages**. Access it using `agent.memory`

The list of runs between the user and agent. Each run contains the input message and output response.

The full list of messages sent to the model, including system prompt, tool calls etc.

You can give your agent access to memory in the following ways:

*   You can set `add_history_to_messages=True` and `num_history_responses=5` to add the previous 5 messages automatically to every message sent to the agent.
*   You can set `read_chat_history=True` to provide a `get_chat_history()` tool to your agent allowing it to read any message in the entire chat history.
*   You can set `read_tool_call_history=True` to provide a `get_tool_call_history()` tool to your agent allowing it to read tool calls in reverse chronological order.

### Example

Persistent Memory
-----------------

The built-in memory only lasts while the session is active. To persist memory across sessions, we can store Agent sessions in a database using `AgentStorage`.

Storage is a necessary component when building user facing AI products as any production application will require users to be able to “continue” their conversation with the Agent.

Let’s test this out, create a file `persistent_memory.py` with the following code:

### Run the agent

Install dependencies and run the agent:

You can view the agent sessions in the sqlite database and continue any conversation by providing the same `session_id`.

Read more in the [storage](https://docs.agno.com/agents/storage) section.

User preferences and conversation summaries
-------------------------------------------

Along with storing chat history and run messages, `AgentMemory` can be extended to automatically classify and store user preferences and conversation summaries.

To do this, add a `db` to `AgentMemory` and set `create_user_memories=True` and `create_session_summary=True`

User memories are stored in the `AgentMemory` whereas session summaries are stored in the `AgentStorage` table with the rest of the session information.

Example
-------

personalized\_memories\_and\_summaries.py

Attributes
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `memory` | `AgentMemory` | `AgentMemory()` | Agent’s memory object used for storing and retrieving information. |
| `add_history_to_messages` | `bool` | `False` | If true, adds the chat history to the messages sent to the Model. Also known as `add_chat_history_to_messages`. |
| `num_history_responses` | `int` | `3` | Number of historical responses to add to the messages. |
| `create_user_memories` | `bool` | `False` | If true, create and store personalized memories for the user. |
| `update_user_memories_after_run` | `bool` | `True` | If true, update memories for the user after each run. |
| `create_session_summary` | `bool` | `False` | If true, create and store session summaries. |
| `update_session_summary_after_run` | `bool` | `True` | If true, update session summaries after each run. |

Developer Resources
-------------------

*   View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/memory)



================================================================================
Section 20: Content from https://docs.agno.com/agents/storage
================================================================================

Title: Storage - Agno

URL Source: https://docs.agno.com/agents/storage

Markdown Content:
Storage - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Storage

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Storage
=======

**Agents use storage to persist sessions by storing them in a database.**

Agents come with built-in memory, but it only lasts while the session is active. To continue conversations across sessions, we store agent sessions in a database like Sqllite or PostgreSQL.

The general syntax for adding storage to an Agent looks like:

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.storage.agent.postgres import PostgresAgentStorage

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    storage=PostgresAgentStorage(table_name="agent_sessions", db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
agent.print_response("Which country are we speaking about?")
```

[​](https://docs.agno.com/agents/storage#example)

Example
------------------------------------------------------------

1

Run Postgres

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **Postgres** on port **5532** using:

Copy

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agno/pgvector:16
```

2

Create an Agent with Storage

Create a file `agent_with_storage.py` with the following contents

Copy

```python
import typer
from typing import Optional, List
from agno.agent import Agent
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
storage = PostgresAgentStorage(table_name="pdf_agent", db_url=db_url)

def pdf_agent(new: bool = False, user: str = "user"):
    session_id: Optional[str] = None

    if not new:
        existing_sessions: List[str] = storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        session_id=session_id,
        user_id=user,
        knowledge=knowledge_base,
        storage=storage,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
        # We can also automatically add the chat history to the messages sent to the model
        # But giving the model the chat history is not always useful, so we give it a tool instead
        # to only use when needed.
        # add_history_to_messages=True,
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
    )
    if session_id is None:
        session_id = agent.session_id
        print(f"Started Session: {session_id}\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    # Runs the agent as a cli app
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    # Load the knowledge base: Comment after first run
    knowledge_base.load(upsert=True)

    typer.run(pdf_agent)
```

3

Run the agent

Install libraries

Mac

Windows

Copy

```bash
pip install -U agno openai pgvector pypdf "psycopg[binary]" sqlalchemy
```

Run the agent

Copy

```bash
python agent_with_storage.py
```

Now the agent continues across sessions. Ask a question:

Copy

```
How do I make pad thai?
```

Then message `bye` to exit, start the app again and ask:

Copy

```
What was my last message?
```

4

Start a new run

Run the `agent_with_storage.py` file with the `--new` flag to start a new run.

Copy

```bash
python agent_with_storage.py --new
```

[​](https://docs.agno.com/agents/storage#params)

Params
----------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `storage` | `Optional[AgentStorage]` | `None` | Storage mechanism for the agent, if applicable. |

[​](https://docs.agno.com/agents/storage#developer-resources)

Developer Resources
------------------------------------------------------------------------------------

*   View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/storage)

[Memory](https://docs.agno.com/agents/memory)[Reasoning](https://docs.agno.com/agents/reasoning)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Example](https://docs.agno.com/agents/storage#example)
*   [Params](https://docs.agno.com/agents/storage#params)
*   [Developer Resources](https://docs.agno.com/agents/storage#developer-resources)



================================================================================
Section 21: Content from https://docs.agno.com/agents/reasoning
================================================================================

Title: Reasoning - Agno

URL Source: https://docs.agno.com/agents/reasoning

Markdown Content:
Reasoning - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Reasoning

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Reasoning
=========

Reasoning is an **experimental feature** that enables an `Agent` to think through a problem step-by-step before jumping into a response. The Agent works through different ideas, validating and correcting as needed. Once it reaches a final answer, it will validate and provide a response. Let’s give it a try. Create a file `reasoning_agent.py`

reasoning\_agent.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Three missionaries and three cannibals need to cross a river. "
    "They have a boat that can carry up to two people at a time. "
    "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
)

reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the Reasoning Agent:

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python reasoning_agent.py
```

Agno Agents can leverage **specialized reasoning models** alongside the primary Agent model. These models are dedicated to reasoning rather than handling the main Agent tasks. Their responses are appended as messages to the Agent, integrating into the message history sent to the primary Agent model.

Currently, Groq and DeepSeek models are supported for external reasoning. Below is an example `Agent` that uses a `Groq` model for reasoning but uses the `OpenAI` model for the main `Agent`.

groq\_reasoning.py

Copy

```python
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat

reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning_model=Groq(id="deepseek-r1-distill-llama-70b"))
reasoning_agent.print_response(task, stream=True)
```

Run the Reasoning Agent:

Copy

```bash
pip install -U agno openai groq

export OPENAI_API_KEY=***
export GROQ_API_KEY=***

python groq_reasoning.py
```

[​](https://docs.agno.com/agents/reasoning#how-to-use-reasoning)

How to use reasoning
----------------------------------------------------------------------------------------

To add reasoning, set `reasoning=True` or set `reasoning_model` to a supported reasoning model. If you do not set `reasoning_model`, the primary `Agent` model will be used for reasoning.

deepseek\_reasoning.py

Copy

```python
from agno.models.openai import OpenAIChat
from agno.models.deepseek import DeepSeek

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
)
reasoning_agent.print_response("How many 'r' are in the word 'supercalifragilisticexpialidocious'?", stream=True)
```

Copy

```bash
pip install -U agno openai deepseek

export OPENAI_API_KEY=***
export DEEPSEEK_API_KEY=***

python deepseek_reasoning.py
```

[​](https://docs.agno.com/agents/reasoning#reasoning-with-tools)

Reasoning with tools
----------------------------------------------------------------------------------------

You can also use tools with a reasoning agent. Lets create a finance agent that can reason.

finance\_reasoning.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to show data"],
    show_tool_calls=True,
    markdown=True,
    reasoning=True,
)
reasoning_agent.print_response("Write a report comparing NVDA to TSLA", stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai yfinance

export OPENAI_API_KEY=***

python finance_reasoning.py
```

[​](https://docs.agno.com/agents/reasoning#more-reasoning-examples)

More reasoning examples
----------------------------------------------------------------------------------------------

### 

[​](https://docs.agno.com/agents/reasoning#logical-puzzles)

Logical puzzles

logical\_puzzle.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Three missionaries and three cannibals need to cross a river. "
    "They have a boat that can carry up to two people at a time. "
    "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python logical_puzzle.py
```

### 

[​](https://docs.agno.com/agents/reasoning#mathematical-proofs)

Mathematical proofs

mathematical\_proof.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Prove that for any positive integer n, the sum of the first n odd numbers is equal to n squared. Provide a detailed proof."
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python mathematical_proof.py
```

### 

[​](https://docs.agno.com/agents/reasoning#scientific-research)

Scientific research

scientific\_research.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Read the following abstract of a scientific paper and provide a critical evaluation of its methodology,"
    "results, conclusions, and any potential biases or flaws:\n\n"
    "Abstract: This study examines the effect of a new teaching method on student performance in mathematics. "
    "A sample of 30 students was selected from a single school and taught using the new method over one semester. "
    "The results showed a 15% increase in test scores compared to the previous semester. "
    "The study concludes that the new teaching method is effective in improving mathematical performance among high school students."
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python scientific_research.py
```

### 

[​](https://docs.agno.com/agents/reasoning#ethical-dilemma)

Ethical dilemma

ethical\_dilemma.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "You are a train conductor faced with an emergency: the brakes have failed, and the train is heading towards "
    "five people tied on the track. You can divert the train onto another track, but there is one person tied there. "
    "Do you divert the train, sacrificing one to save five? Provide a well-reasoned answer considering utilitarian "
    "and deontological ethical frameworks. "
    "Provide your answer also as an ascii art diagram."
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python ethical_dilemma.py
```

### 

[​](https://docs.agno.com/agents/reasoning#planning-an-itinerary)

Planning an itinerary

planning\_itinerary.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Plan an itinerary from Los Angeles to Las Vegas"
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python planning_itinerary.py
```

### 

[​](https://docs.agno.com/agents/reasoning#creative-writing)

Creative writing

creative\_writing.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Write a short story about life in 5000000 years"
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True, structured_outputs=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

Run the script to see the output.

Copy

```bash
pip install -U agno openai

export OPENAI_API_KEY=***

python creative_writing.py
```

[​](https://docs.agno.com/agents/reasoning#developer-resources)

Developer Resources
--------------------------------------------------------------------------------------

*   View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/reasoning)

[Storage](https://docs.agno.com/agents/storage)[Teams](https://docs.agno.com/agents/teams)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to use reasoning](https://docs.agno.com/agents/reasoning#how-to-use-reasoning)
*   [Reasoning with tools](https://docs.agno.com/agents/reasoning#reasoning-with-tools)
*   [More reasoning examples](https://docs.agno.com/agents/reasoning#more-reasoning-examples)
*   [Logical puzzles](https://docs.agno.com/agents/reasoning#logical-puzzles)
*   [Mathematical proofs](https://docs.agno.com/agents/reasoning#mathematical-proofs)
*   [Scientific research](https://docs.agno.com/agents/reasoning#scientific-research)
*   [Ethical dilemma](https://docs.agno.com/agents/reasoning#ethical-dilemma)
*   [Planning an itinerary](https://docs.agno.com/agents/reasoning#planning-an-itinerary)
*   [Creative writing](https://docs.agno.com/agents/reasoning#creative-writing)
*   [Developer Resources](https://docs.agno.com/agents/reasoning#developer-resources)



================================================================================
Section 22: Content from https://docs.agno.com/agents/teams
================================================================================

Title: Teams - Agno

URL Source: https://docs.agno.com/agents/teams

Markdown Content:
Teams - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Teams

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Teams
=====

We can combine multiple Agents to form a team and tackle tasks as a cohesive unit. Here’s a simple example that uses a team of agents to write an article about the top stories on hackernews.

hackernews\_team.py

Copy

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

hn_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

article_reader = Agent(
    name="Article Reader",
    model=OpenAIChat("gpt-4o"),
    role="Reads articles from URLs.",
    tools=[Newspaper4kTools()],
)

hn_team = Agent(
    name="Hackernews Team",
    model=OpenAIChat("gpt-4o"),
    team=[hn_researcher, web_searcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the article reader to read the links for the stories to get more information.",
        "Important: you must provide the article reader with the links to read.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    show_tool_calls=True,
    markdown=True,
)
hn_team.print_response("Write an article about the top 2 stories on hackernews", stream=True)
```

Run the script to see the output.

Copy

```bash
pip install -U openai duckduckgo-search newspaper4k lxml_html_clean agno

python hackernews_team.py
```

[​](https://docs.agno.com/agents/teams#how-to-build-agent-teams)

How to build Agent Teams
--------------------------------------------------------------------------------------------

1.  Add a `name` and `role` parameter to the member Agents.
2.  Create a Team Leader that can delegate tasks to team-members.
3.  Use your Agent team just like you would use a regular Agent.

[​](https://docs.agno.com/agents/teams#developer-resources)

Developer Resources
----------------------------------------------------------------------------------

*   View [Examples](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/teams/)

[Reasoning](https://docs.agno.com/agents/reasoning)[Introduction](https://docs.agno.com/models/introduction)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build Agent Teams](https://docs.agno.com/agents/teams#how-to-build-agent-teams)
*   [Developer Resources](https://docs.agno.com/agents/teams#developer-resources)



================================================================================
Section 23: Content from https://docs.agno.com/how-to/install
================================================================================

Title: Install & Setup - Agno

URL Source: https://docs.agno.com/how-to/install

Markdown Content:
Install & Setup - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

How to

Install & Setup

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

How to

Install & Setup
===============

[​](https://docs.agno.com/how-to/install#install-agno)

Install agno
----------------------------------------------------------------------

We highly recommend:

*   Installing `agno` using `pip` in a python virtual environment.

1

Create a virtual environment

Mac

Windows

Copy

```bash
python3 -m venv ~/.venvs/agno
source ~/.venvs/agno/bin/activate
```

2

Install agno

Install `agno` using pip

Mac

Windows

Copy

```bash
pip install -U agno
```

  

If you encounter errors, try updating pip using `python -m pip install --upgrade pip`

* * *

[​](https://docs.agno.com/how-to/install#upgrade-agno)

Upgrade agno
----------------------------------------------------------------------

To upgrade `agno`, run this in your virtual environment

Copy

```bash
pip install -U agno --no-cache-dir
```

* * *

[​](https://docs.agno.com/how-to/install#setup-agno)

Setup Agno
------------------------------------------------------------------

Log-in and connect to agno.com using `ag setup`

Copy

```bash
ag setup
```

[Advanced](https://docs.agno.com/workflows/advanced)[Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Install agno](https://docs.agno.com/how-to/install#install-agno)
*   [Upgrade agno](https://docs.agno.com/how-to/install#upgrade-agno)
*   [Setup Agno](https://docs.agno.com/how-to/install#setup-agno)



================================================================================
Section 24: Content from https://docs.agno.com/how-to/local-docker-guide
================================================================================

Title: Run Local Agent API - Agno

URL Source: https://docs.agno.com/how-to/local-docker-guide

Markdown Content:
Run Local Agent API - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

How to

Run Local Agent API

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

How to

Run Local Agent API
===================

This guide will walk you through:

*   Creating a minimal FastAPI app with an Agno agent
*   Containerizing it with Docker
*   Running it locally along with a PostgreSQL database for knowledge and memory

[​](https://docs.agno.com/how-to/local-docker-guide#setup)

Setup
-------------------------------------------------------------------

1

Create a new directory for your project

Create a new directory for your project and navigate to it. After following this guide, your project structure will should look like this:

Copy

```shell
mkdir my-project
cd my-project
```

After following this guide, your project structure will should look like this:

Copy

```shell
my-project/
├── main.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
```

2

Create a \`requirements.txt\` file and add the required dependencies:

requirements.txt

Copy

```txt
fastapi
agno
openai
pgvector
pypdf
psycopg[binary]
sqlalchemy
uvicorn
```

[​](https://docs.agno.com/how-to/local-docker-guide#step-1-create-a-fastapi-app-with-an-agno-agent)

Step 1: Create a FastAPI App with an Agno Agent
------------------------------------------------------------------------------------------------------------------------------------------------------

1

Create a new Python file, e.g., \`main.py\`, and add the following code to create a minimal FastAPI app with an Agno agent:

main.py

Copy

```python
from fastapi import FastAPI
from agno.agent import Agent
from agno.models.openai import OpenAIChat

app = FastAPI()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant.",
    markdown=True,
)

@app.get("/ask")
async def ask(query: str):
    response = agent.run(query)
    return {"response": response.content}
```

2

Create and activate a virtual environment:

Copy

```bash
python -m venv .venv
source .venv/bin/activate
```

3

Install the required dependencies by running:

Copy

```bash
pip install -r requirements.txt
```

4

Set your OPENAI\_API\_KEY environment variable:

Copy

```bash
export OPENAI_API_KEY=your_api_key
```

5

Run the FastAPI app with \`uvicorn main:app --reload\`.

Copy

```bash
uvicorn main:app --reload
```

[​](https://docs.agno.com/how-to/local-docker-guide#step-2-create-a-dockerfile)

Step 2: Create a Dockerfile
--------------------------------------------------------------------------------------------------------------

1

In the same directory, create a new file named \`Dockerfile\` with the following content:

Dockerfile

Copy

```dockerfile
FROM agnohq/python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2

Build the Docker image by running:

Copy

```bash
docker build -t my-agent-app .
```

3

Run the Docker container with:

Copy

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=your_api_key my-agent-app
```

4

Access your app

You can now access the FastAPI app at `http://localhost:8000`.

[​](https://docs.agno.com/how-to/local-docker-guide#step-3-add-knowledge-and-memory-with-postgresql)

Step 3: Add Knowledge and Memory with PostgreSQL
--------------------------------------------------------------------------------------------------------------------------------------------------------

1

Update your \`main.py\` file to include knowledge and memory storage using PostgreSQL:

main.py

Copy

```python
from fastapi import FastAPI
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.storage.agent.postgres import PostgresAgentStorage

app = FastAPI()

db_url = "postgresql+psycopg://agno:agno@db/agno"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    knowledge=knowledge_base,
    storage=PostgresAgentStorage(table_name="agent_sessions", db_url=db_url),
    markdown=True,
)

@app.get("/ask")
async def ask(query: str):
    response = agent.run(query)
    return {"response": response.content}
```

2

Create a \`docker-compose.yml\` file in the same directory with the following content:

docker-compose.yml

Copy

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      db:
        condition: service_healthy

  db:
    image: agnohq/pgvector:16
    environment:
      POSTGRES_DB: agno
      POSTGRES_USER: agno
      POSTGRES_PASSWORD: agno
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U agno"]
      interval: 2s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

3

Run the Docker Compose setup with:

Copy

```bash
docker-compose up --build
```

This will start the FastAPI app and the PostgreSQL database, allowing your agent to use knowledge and memory storage.

You can now access the FastAPI app at `http://localhost:8000` and interact with your agent that has knowledge and memory capabilities.

You can test the agent by running `curl http://localhost:8000/ask?query="What is the recipe for pad thai?"`.

[Install & Setup](https://docs.agno.com/how-to/install)[Contributing to Agno](https://docs.agno.com/how-to/contribute)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Setup](https://docs.agno.com/how-to/local-docker-guide#setup)
*   [Step 1: Create a FastAPI App with an Agno Agent](https://docs.agno.com/how-to/local-docker-guide#step-1-create-a-fastapi-app-with-an-agno-agent)
*   [Step 2: Create a Dockerfile](https://docs.agno.com/how-to/local-docker-guide#step-2-create-a-dockerfile)
*   [Step 3: Add Knowledge and Memory with PostgreSQL](https://docs.agno.com/how-to/local-docker-guide#step-3-add-knowledge-and-memory-with-postgresql)



================================================================================
Section 25: Content from https://docs.agno.com/how-to/contribute
================================================================================

Title: Contributing to Agno - Agno

URL Source: https://docs.agno.com/how-to/contribute

Markdown Content:
Agno is an open-source project and we welcome contributions.

👩‍💻 How to contribute
-----------------------

Please follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow:

*   Fork the repository.
*   Create a new branch for your feature.
*   Add your feature or improvement.
*   Send a pull request.
*   We appreciate your support & input!

Development setup
-----------------

1.  Clone the repository.
2.  Create a virtual environment:
    *   For Unix, use `./scripts/dev_setup.sh`.
    *   This setup will:
        *   Create a `.venv` virtual environment in the current directory.
        *   Install the required packages.
        *   Install the `agno` package in editable mode.
3.  Activate the virtual environment:
    *   On Unix: `source .venv/bin/activate`

> From here on you have to use `uv pip install` to install missing packages

Formatting and validation
-------------------------

Ensure your code meets our quality standards by running the appropriate formatting and validation script before submitting a pull request:

*   For Unix:
    *   `./scripts/format.sh`
    *   `./scripts/validate.sh`

These scripts will perform code formatting with `ruff` and static type checks with `mypy`.

Read more about the guidelines [here](https://github.com/agno-agi/agno/tree/main/cookbook/CONTRIBUTING.md)

Message us on [Discord](https://discord.gg/4MtYHHrgA8) or post on [Discourse](https://community.agno.com/) if you have any questions or need help with credits.



================================================================================
Section 26: Content from https://docs.agno.com/how-to/phidata-to-agno
================================================================================

Title: Migrate from Phidata to Agno - Agno

URL Source: https://docs.agno.com/how-to/phidata-to-agno

Markdown Content:
This guide helps you migrate your codebase to adapt to the major refactor accompanying the launch of Agno.

General Namespace Updates
-------------------------

This refactor includes comprehensive updates to namespaces to improve clarity and consistency. Pay close attention to the following changes:

*   All `phi` namespaces are now replaced with `agno` to reflect the updated structure.
*   Submodules and classes have been renamed to better represent their functionality and context.

Interface Changes
-----------------

### Module and Namespace Updates

*   **Models**:
    *   `phi.model.x` ➔ `agno.models.x`
        *   All model classes now reside under the `agno.models` namespace, consolidating related functionality in a single location.
*   **Knowledge Bases**:
    *   `phi.knowledge_base.x` ➔ `agno.knowledge.x`
        *   Knowledge bases have been restructured for better organization under `agno.knowledge`.
*   **Document Readers**:
    *   `phi.document.reader.xxx` ➔ `agno.document.reader.xxx_reader`
        *   Document readers now include a `_reader` suffix for clarity and consistency.
*   **Toolkits**:
    *   All Agno toolkits now have a `Tools` suffix. For example, `DuckDuckGo` ➔ `DuckDuckGoTools`.
        *   This change standardizes the naming of tools, making their purpose more explicit.

### Multi-Modal Interface Updates

The multi-modal interface now uses specific types for different media inputs and outputs:

#### Inputs

*   **Images**:
    
    *   Images are now represented by a dedicated `Image` class, providing additional metadata and control over image handling.
*   **Audio**:
    
    *   Audio files are handled through the `Audio` class, allowing specification of content and format.
*   **Video**:
    
    *   Videos have their own `Video` class, enabling better handling of video data.

#### Outputs

*   `RunResponse` now includes updated artifact types:
    *   `RunResponse.images` is a list of type `ImageArtifact`:
        
    *   `RunResponse.audio` is a list of type `AudioArtifact`:
        
    *   `RunResponse.videos` is a list of type `VideoArtifact`:
        
    *   `RunResponse.response_audio` is of type `AudioOutput`:
        
        *   This response audio corresponds to the model’s response in audio format.

### Model Name Changes

*   `Hermes` ➔ `OllamaHermes`
*   `AzureOpenAIChat` ➔ `AzureOpenAI`
*   `CohereChat` ➔ `Cohere`
*   `DeepSeekChat` ➔ `DeepSeek`
*   `GeminiOpenAIChat` ➔ `GeminiOpenAI`
*   `HuggingFaceChat` ➔ `HuggingFace`

For example:

### Storage Class Updates

*   **Agent Storage**:
    *   `PgAgentStorage` ➔ `PostgresAgentStorage`
    *   `SqlAgentStorage` ➔ `SqliteAgentStorage`
    *   `MongoAgentStorage` ➔ `MongoDbAgentStorage`
    *   `S2AgentStorage` ➔ `SingleStoreAgentStorage`
*   **Workflow Storage**:
    *   `SqlWorkflowStorage` ➔ `SqliteWorkflowStorage`
    *   `PgWorkflowStorage` ➔ `PostgresWorkflowStorage`
    *   `MongoWorkflowStorage` ➔ `MongoDbWorkflowStorage`

### Knowledge Base Updates

*   `phi.knowledge.pdf.PDFUrlKnowledgeBase` ➔ `agno.knowledge.pdf_url.PDFUrlKnowledgeBase`
*   `phi.knowledge.csv.CSVUrlKnowledgeBase` ➔ `agno.knowledge.csv_url.CSVUrlKnowledgeBase`

### Embedders updates

Embedders now all take id instead of model as a parameter. For example:

*   `OllamaEmbedder(model="llama3.2")` -\> `OllamaEmbedder(id="llama3.2")`

### Reader Updates

*   `phi.document.reader.arxiv` ➔ `agno.document.reader.arxiv_reader`
*   `phi.document.reader.docx` ➔ `agno.document.reader.docx_reader`
*   `phi.document.reader.json` ➔ `agno.document.reader.json_reader`
*   `phi.document.reader.pdf` ➔ `agno.document.reader.pdf_reader`
*   `phi.document.reader.s3.pdf` ➔ `agno.document.reader.s3.pdf_reader`
*   `phi.document.reader.s3.text` ➔ `agno.document.reader.s3.text_reader`
*   `phi.document.reader.text` ➔ `agno.document.reader.text_reader`
*   `phi.document.reader.website` ➔ `agno.document.reader.website_reader`

Agent Updates
-------------

*   `guidelines`, `prevent_hallucinations`, `prevent_prompt_leakage`, `limit_tool_access`, and `task` have been removed from the `Agent` class. They can be incorporated into the `instructions` parameter as you see fit.

For example:

CLI and Infrastructure Updates
------------------------------

### Command Line Interface Changes

The Agno CLI has been refactored from `phi` to `ag`. Here are the key changes:

### New Commands

*   `ag ping` -\> Check if you are authenticated

### Removed Commands

*   `phi ws setup` -\> Replaced by `ag setup`

### Infrastructure Path Changes

The infrastructure-related code has been reorganized for better clarity:

*   **Docker Infrastructure**: This has been moved to a separate package in `/libs/infra/agno_docker` and has a separate PyPi package [`agno-docker`](https://pypi.org/project/agno-docker/).
*   **AWS Infrastructure**: This has been moved to a separate package in `/libs/infra/agno_aws` and has a separate PyPi package [`agno-aws`](https://pypi.org/project/agno-aws/).

We recommend installing these packages in applications that you intend to deploy to AWS using Agno, or if you are migrating from a Phidata application.

The specific path changes are:

*   `import phi.aws.resource.xxx` ➔ `import agno.aws.resource.xxx`
*   `import phi.docker.xxx` ➔ `import agno.docker.xxx`

* * *

Follow the steps above to ensure your codebase is compatible with the latest version of Agno AI. If you encounter any issues, don’t hesitate to contact us on [Discourse](https://community.phidata.com/) or [Discord](https://discord.gg/4MtYHHrgA8).



================================================================================
Section 27: Content from https://docs.agno.com/agents/introduction#what-are-agents
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/agents/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Introduction
============

[​](https://docs.agno.com/agents/introduction#what-are-agents)

What are Agents?
----------------------------------------------------------------------------------

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Instead of a rigid binary definition, let’s think of Agents in terms of agency and autonomy.

*   **Level 0**: Agents with no tools (basic inference tasks).
*   **Level 1**: Agents with tools for autonomous task execution.
*   **Level 2**: Agents with knowledge, combining memory and reasoning.
*   **Level 3**: Teams of agents collaborating on complex workflows.

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)If you haven’t built your first agent yet, [follow this guide](https://docs.agno.com/agents) and then dive into more advanced concepts.

[​](https://docs.agno.com/agents/introduction#example-research-agent)

Example: Research Agent
------------------------------------------------------------------------------------------------

Let’s create a research agent that can search the web using DuckDuckGo, scrape the top links using Newspaper4k and write a research report for us. Ideally we’ll use specialized tools (like Exa) but let’s start with the free tools first.

The description and instructions are converted to the system message and the input is passed as the user message. Set `debug_mode=True` to view logs behind the scenes.

1

Create Research Agent

Create a file `research_agent.py`

research\_agent.py

Copy

```python
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""
```

2

Run the agent

Install libraries

Copy

```shell
pip install openai exa-py agno
```

Run the agent

Copy

```shell
python research_agent.py
```

[Community](https://docs.agno.com/get-started/community)[Agent.run()](https://docs.agno.com/agents/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [What are Agents?](https://docs.agno.com/agents/introduction#what-are-agents)
*   [Example: Research Agent](https://docs.agno.com/agents/introduction#example-research-agent)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)



================================================================================
Section 28: Content from https://docs.agno.com/agents
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/agents

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Introduction
============

[​](https://docs.agno.com/agents#what-are-agents)

What are Agents?
---------------------------------------------------------------------

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Instead of a rigid binary definition, let’s think of Agents in terms of agency and autonomy.

*   **Level 0**: Agents with no tools (basic inference tasks).
*   **Level 1**: Agents with tools for autonomous task execution.
*   **Level 2**: Agents with knowledge, combining memory and reasoning.
*   **Level 3**: Teams of agents collaborating on complex workflows.

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)If you haven’t built your first agent yet, [follow this guide](https://docs.agno.com/agents) and then dive into more advanced concepts.

[​](https://docs.agno.com/agents#example-research-agent)

Example: Research Agent
-----------------------------------------------------------------------------------

Let’s create a research agent that can search the web using DuckDuckGo, scrape the top links using Newspaper4k and write a research report for us. Ideally we’ll use specialized tools (like Exa) but let’s start with the free tools first.

The description and instructions are converted to the system message and the input is passed as the user message. Set `debug_mode=True` to view logs behind the scenes.

1

Create Research Agent

Create a file `research_agent.py`

research\_agent.py

Copy

```python
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""
```

2

Run the agent

Install libraries

Copy

```shell
pip install openai exa-py agno
```

Run the agent

Copy

```shell
python research_agent.py
```

[Community](https://docs.agno.com/get-started/community)[Agent.run()](https://docs.agno.com/agents/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [What are Agents?](https://docs.agno.com/agents#what-are-agents)
*   [Example: Research Agent](https://docs.agno.com/agents#example-research-agent)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)



================================================================================
Section 29: Content from https://docs.agno.com/agents/introduction#example-research-agent
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/agents/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,020](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Introduction

[User Guide](https://docs.agno.com/introduction)[Examples](https://docs.agno.com/examples/introduction)[Reference](https://docs.agno.com/reference/agents/agent)[Changelog](https://docs.agno.com/changelog/overview)[FAQs](https://docs.agno.com/faq/environment_variables)[Hackathon Resources](https://docs.agno.com/hackathon/introduction)

##### Get Started

*   [Welcome to Agno](https://docs.agno.com/introduction)
*   [Your first Agent](https://docs.agno.com/get-started/agents)
*   [Agent Playground](https://docs.agno.com/get-started/playground)
*   [Agent Observability](https://docs.agno.com/get-started/monitoring)
*   [Community](https://docs.agno.com/get-started/community)

##### Concepts

*   Agents
    
    *   [Introduction](https://docs.agno.com/agents/introduction)
    *   [Agent.run()](https://docs.agno.com/agents/run)
    *   [Structured Output](https://docs.agno.com/agents/structured-output)
    *   [Multimodal Agents](https://docs.agno.com/agents/multimodal)
    *   [Prompts](https://docs.agno.com/agents/prompts)
    *   [Tools](https://docs.agno.com/agents/tools)
    *   [Knowledge](https://docs.agno.com/agents/knowledge)
    *   [Memory](https://docs.agno.com/agents/memory)
    *   [Storage](https://docs.agno.com/agents/storage)
    *   [Reasoning](https://docs.agno.com/agents/reasoning)
    *   [Teams](https://docs.agno.com/agents/teams)
*   Models
    
*   Tools
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Agents

Introduction
============

[​](https://docs.agno.com/agents/introduction#what-are-agents)

What are Agents?
----------------------------------------------------------------------------------

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Instead of a rigid binary definition, let’s think of Agents in terms of agency and autonomy.

*   **Level 0**: Agents with no tools (basic inference tasks).
*   **Level 1**: Agents with tools for autonomous task execution.
*   **Level 2**: Agents with knowledge, combining memory and reasoning.
*   **Level 3**: Teams of agents collaborating on complex workflows.

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)If you haven’t built your first agent yet, [follow this guide](https://docs.agno.com/agents) and then dive into more advanced concepts.

[​](https://docs.agno.com/agents/introduction#example-research-agent)

Example: Research Agent
------------------------------------------------------------------------------------------------

Let’s create a research agent that can search the web using DuckDuckGo, scrape the top links using Newspaper4k and write a research report for us. Ideally we’ll use specialized tools (like Exa) but let’s start with the free tools first.

The description and instructions are converted to the system message and the input is passed as the user message. Set `debug_mode=True` to view logs behind the scenes.

1

Create Research Agent

Create a file `research_agent.py`

research\_agent.py

Copy

```python
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""
```

2

Run the agent

Install libraries

Copy

```shell
pip install openai exa-py agno
```

Run the agent

Copy

```shell
python research_agent.py
```

[Community](https://docs.agno.com/get-started/community)[Agent.run()](https://docs.agno.com/agents/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [What are Agents?](https://docs.agno.com/agents/introduction#what-are-agents)
*   [Example: Research Agent](https://docs.agno.com/agents/introduction#example-research-agent)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent.png)


