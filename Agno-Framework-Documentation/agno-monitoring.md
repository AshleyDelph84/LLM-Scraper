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