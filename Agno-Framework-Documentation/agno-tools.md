
================================================================================
Section 1: Content from https://docs.agno.com/tools/introduction
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/tools/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Tools

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
    
*   Models
    
*   Tools
    
    *   [Introduction](https://docs.agno.com/tools/introduction)
    *   Toolkits
        
    *   [Writing your own Toolkit](https://docs.agno.com/tools/custom-toolkits)
    *   [Python Functions](https://docs.agno.com/tools/functions)
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

Tools

Introduction
============

Tools are **functions** that an Agent can run like searching the web, running SQL, sending an email or calling APIs. Use tools integrate Agents with external systems. You can use any python function as a tool or use a pre-built **toolkit**. The general syntax is:

Copy

```python
from agno.agent import Agent

agent = Agent(
    # Add functions or Toolkits
    tools=[...],
    # Show tool calls in the Agent response
    show_tool_calls=True
)
```

Read more about:

*   [Available Toolkits](https://docs.agno.com/tools/toolkits)
*   [Using functions as tools](https://docs.agno.com/tools/functions)

[xAI](https://docs.agno.com/models/xai)[Introduction](https://docs.agno.com/tools/toolkits/toolkits)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)



================================================================================
Section 13: Content from https://docs.agno.com/tools/custom-toolkits
================================================================================

Title: Writing your own Toolkit - Agno

URL Source: https://docs.agno.com/tools/custom-toolkits

Markdown Content:
Many advanced use-cases will require writing custom Toolkits. Here’s the general flow:

1.  Create a class inheriting the `agno.tools.Toolkit` class.
2.  Add your functions to the class.
3.  **Important:** Register the functions using `self.register(function_name)`

Now your Toolkit is ready to use with an Agent. For example:

```
from typing import List

from agno.agent import Agent
from agno.tools import Toolkit
from agno.utils.log import logger

class ShellTools(Toolkit):
    def __init__(self):
        super().__init__(name="shell_tools")
        self.register(self.run_shell_command)

    def run_shell_command(self, args: List[str], tail: int = 100) -> str:
        """
        Runs a shell command and returns the output or error.

        Args:
            args (List[str]): The command to run as a list of strings.
            tail (int): The number of lines to return from the output.
        Returns:
            str: The output of the command.
        """
        import subprocess

        logger.info(f"Running shell command: {args}")
        try:
            logger.info(f"Running shell command: {args}")
            result = subprocess.run(args, capture_output=True, text=True)
            logger.debug(f"Result: {result}")
            logger.debug(f"Return code: {result.returncode}")
            if result.returncode != 0:
                return f"Error: {result.stderr}"
            # return only the last n lines of the output
            return "\n".join(result.stdout.split("\n")[-tail:])
        except Exception as e:
            logger.warning(f"Failed to run shell command: {e}")
            return f"Error: {e}"

agent = Agent(tools=[ShellTools()], show_tool_calls=True, markdown=True)
agent.print_response("List all the files in my home directory.")
```



================================================================================
Section 14: Content from https://docs.agno.com/tools/functions
================================================================================

Title: Python Functions - Agno

URL Source: https://docs.agno.com/tools/functions

Markdown Content:
Any python function can be used as a tool by an Agent. **We highly recommend** creating functions specific to your workflow and adding them to your Agents.

For example, here’s how to use a `get_top_hackernews_stories` function as a tool:

```
import json
import httpx

from agno.agent import Agent

def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """
    Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True)
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
```

================================================================================
Section 19: Content from https://docs.agno.com/tools/toolkits
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/tools/toolkits

Markdown Content:
A **Toolkit** is a collection of functions that can be added to an Agent. The functions in a Toolkit are designed to work together, share internal state and provide a better development experience.

The following **Toolkits** are available to use

[Airflow ------- Tools to manage Airflow DAGs.](https://docs.agno.com/tools/toolkits/airflow)[Apify ----- Tools to use Apify Actors.](https://docs.agno.com/tools/toolkits/apify)[Arxiv ----- Tools to read arXiv papers.](https://docs.agno.com/tools/toolkits/arxiv)[Calculator ---------- Tools to perform calculations.](https://docs.agno.com/tools/toolkits/calculator)[CalCom ------ Tools to interact with the Cal.com API.](https://docs.agno.com/tools/toolkits/calcom)[Composio -------- Tools to compose complex workflows.](https://docs.agno.com/tools/toolkits/composio)[Confluence ---------- Tools to manage Confluence pages.](https://docs.agno.com/tools/toolkits/confluence)[Crawl4AI -------- Tools to crawl web data.](https://docs.agno.com/tools/toolkits/crawl4ai)[CSV --- Tools to work with CSV files.](https://docs.agno.com/tools/toolkits/csv)[Dalle ----- Tools to interact with Dalle.](https://docs.agno.com/tools/toolkits/dalle)[Discord ------- Tools to interact with Discord.](https://docs.agno.com/tools/toolkits/discord)[DuckDb ------ Tools to run SQL using DuckDb.](https://docs.agno.com/tools/toolkits/duckdb)[DuckDuckGo ---------- Tools to search the web using DuckDuckGo.](https://docs.agno.com/tools/toolkits/duckduckgo)[Eleven Labs ----------- Tools to generate audio using Eleven Labs.](https://docs.agno.com/tools/toolkits/eleven_labs)[Email ----- Tools to send emails.](https://docs.agno.com/tools/toolkits/email)[Exa --- Tools to search the web using Exa.](https://docs.agno.com/tools/toolkits/exa)[Fal --- Tools to generate media using Fal.](https://docs.agno.com/tools/toolkits/fal)[File ---- Tools to read and write files.](https://docs.agno.com/tools/toolkits/file)[Firecrawl --------- Tools to crawl the web using Firecrawl.](https://docs.agno.com/tools/toolkits/firecrawl)[GitHub ------ Tools to interact with GitHub.](https://docs.agno.com/tools/toolkits/github)[Giphy ----- Tools to search for GIFs on Giphy.](https://docs.agno.com/tools/toolkits/giphy)[Gmail ----- Tools to interact with Gmail.](https://docs.agno.com/tools/toolkits/gmail)[Google Maps ----------- Tools to search for places on Google Maps.](https://docs.agno.com/tools/toolkits/google_maps)[Google Calendar --------------- Tools to manage Google Calendar events.](https://docs.agno.com/tools/toolkits/googlecalendar)[Google Search ------------- Tools to search Google.](https://docs.agno.com/tools/toolkits/googlesearch)[HackerNews ---------- Tools to read Hacker News articles.](https://docs.agno.com/tools/toolkits/hackernews)[Jina Reader ----------- Tools for neural search and AI services using Jina.](https://docs.agno.com/tools/toolkits/jina_reader)[Jira ---- Tools to interact with Jira.](https://docs.agno.com/tools/toolkits/jira)[MLX Transcribe -------------- Tools to transcribe audio using MLX.](https://docs.agno.com/tools/toolkits/mlx_transcribe)[ModelsLabs ---------- Tools to generate videos using ModelsLabs.](https://docs.agno.com/tools/toolkits/models_labs)[Newspaper --------- Tools to read news articles.](https://docs.agno.com/tools/toolkits/newspaper)[Newspaper4k ----------- Tools to read articles using Newspaper4k.](https://docs.agno.com/tools/toolkits/newspaper4k)[OpenBB ------ Tools to search for stock data using OpenBB.](https://docs.agno.com/tools/toolkits/openbb)[Pandas ------ Tools to manipulate data using Pandas.](https://docs.agno.com/tools/toolkits/pandas)[Postgres -------- Tools to interact with PostgreSQL databases.](https://docs.agno.com/tools/toolkits/postgres)[Pubmed ------ Tools to search Pubmed.](https://docs.agno.com/tools/toolkits/pubmed)[Python ------ Tools to write and run Python code.](https://docs.agno.com/tools/toolkits/python)[Resend ------ Tools to send emails using Resend.](https://docs.agno.com/tools/toolkits/resend)[SearxNG ------- Tools to search the web using SearxNG.](https://docs.agno.com/tools/toolkits/searxng)[Serpapi ------- Tools to search Google, YouTube, and more using Serpapi.](https://docs.agno.com/tools/toolkits/serpapi)[Shell ----- Tools to run shell commands.](https://docs.agno.com/tools/toolkits/shell)[Slack ----- Tools to interact with Slack.](https://docs.agno.com/tools/toolkits/slack)[Sleep ----- Tools to pause execution for a given number of seconds.](https://docs.agno.com/tools/toolkits/sleep)[Spider ------ Tools to crawl websites.](https://docs.agno.com/tools/toolkits/spider)[SQL --- Tools to run SQL queries.](https://docs.agno.com/tools/toolkits/sql)[Tavily ------ Tools to search the web using Tavily.](https://docs.agno.com/tools/toolkits/tavily)[Todoist ------- Tools to interact with Todoist.](https://docs.agno.com/tools/toolkits/todoist)[Twilio ------ Tools to interact with Twilio services.](https://docs.agno.com/tools/toolkits/twilio)[X (Twitter) ----------- Tools to interact with X.](https://docs.agno.com/tools/toolkits/x)[Website ------- Tools to scrape websites.](https://docs.agno.com/tools/toolkits/website)[Wikipedia --------- Tools to search Wikipedia.](https://docs.agno.com/tools/toolkits/wikipedia)[YFinance -------- Tools to search Yahoo Finance.](https://docs.agno.com/tools/toolkits/yfinance)[YouTube ------- Tools to search YouTube.](https://docs.agno.com/tools/toolkits/youtube)[Zendesk ------- Tools to search Zendesk.](https://docs.agno.com/tools/toolkits/zendesk)[Zoom ---- Tools to interact with Zoom.](https://docs.agno.com/tools/toolkits/zoom)







================================================================================
Section 21: Content from https://docs.agno.com/tools/toolkits/toolkits
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/tools/toolkits/toolkits

Markdown Content:
A **Toolkit** is a collection of functions that can be added to an Agent. The functions in a Toolkit are designed to work together, share internal state and provide a better development experience.

The following **Toolkits** are available to use

[Airflow ------- Tools to manage Airflow DAGs.](https://docs.agno.com/tools/toolkits/airflow)[Apify ----- Tools to use Apify Actors.](https://docs.agno.com/tools/toolkits/apify)[Arxiv ----- Tools to read arXiv papers.](https://docs.agno.com/tools/toolkits/arxiv)[Calculator ---------- Tools to perform calculations.](https://docs.agno.com/tools/toolkits/calculator)[CalCom ------ Tools to interact with the Cal.com API.](https://docs.agno.com/tools/toolkits/calcom)[Composio -------- Tools to compose complex workflows.](https://docs.agno.com/tools/toolkits/composio)[Confluence ---------- Tools to manage Confluence pages.](https://docs.agno.com/tools/toolkits/confluence)[Crawl4AI -------- Tools to crawl web data.](https://docs.agno.com/tools/toolkits/crawl4ai)[CSV --- Tools to work with CSV files.](https://docs.agno.com/tools/toolkits/csv)[Dalle ----- Tools to interact with Dalle.](https://docs.agno.com/tools/toolkits/dalle)[Discord ------- Tools to interact with Discord.](https://docs.agno.com/tools/toolkits/discord)[DuckDb ------ Tools to run SQL using DuckDb.](https://docs.agno.com/tools/toolkits/duckdb)[DuckDuckGo ---------- Tools to search the web using DuckDuckGo.](https://docs.agno.com/tools/toolkits/duckduckgo)[Eleven Labs ----------- Tools to generate audio using Eleven Labs.](https://docs.agno.com/tools/toolkits/eleven_labs)[Email ----- Tools to send emails.](https://docs.agno.com/tools/toolkits/email)[Exa --- Tools to search the web using Exa.](https://docs.agno.com/tools/toolkits/exa)[Fal --- Tools to generate media using Fal.](https://docs.agno.com/tools/toolkits/fal)[File ---- Tools to read and write files.](https://docs.agno.com/tools/toolkits/file)[Firecrawl --------- Tools to crawl the web using Firecrawl.](https://docs.agno.com/tools/toolkits/firecrawl)[GitHub ------ Tools to interact with GitHub.](https://docs.agno.com/tools/toolkits/github)[Giphy ----- Tools to search for GIFs on Giphy.](https://docs.agno.com/tools/toolkits/giphy)[Gmail ----- Tools to interact with Gmail.](https://docs.agno.com/tools/toolkits/gmail)[Google Maps ----------- Tools to search for places on Google Maps.](https://docs.agno.com/tools/toolkits/google_maps)[Google Calendar --------------- Tools to manage Google Calendar events.](https://docs.agno.com/tools/toolkits/googlecalendar)[Google Search ------------- Tools to search Google.](https://docs.agno.com/tools/toolkits/googlesearch)[HackerNews ---------- Tools to read Hacker News articles.](https://docs.agno.com/tools/toolkits/hackernews)[Jina Reader ----------- Tools for neural search and AI services using Jina.](https://docs.agno.com/tools/toolkits/jina_reader)[Jira ---- Tools to interact with Jira.](https://docs.agno.com/tools/toolkits/jira)[MLX Transcribe -------------- Tools to transcribe audio using MLX.](https://docs.agno.com/tools/toolkits/mlx_transcribe)[ModelsLabs ---------- Tools to generate videos using ModelsLabs.](https://docs.agno.com/tools/toolkits/models_labs)[Newspaper --------- Tools to read news articles.](https://docs.agno.com/tools/toolkits/newspaper)[Newspaper4k ----------- Tools to read articles using Newspaper4k.](https://docs.agno.com/tools/toolkits/newspaper4k)[OpenBB ------ Tools to search for stock data using OpenBB.](https://docs.agno.com/tools/toolkits/openbb)[Pandas ------ Tools to manipulate data using Pandas.](https://docs.agno.com/tools/toolkits/pandas)[Postgres -------- Tools to interact with PostgreSQL databases.](https://docs.agno.com/tools/toolkits/postgres)[Pubmed ------ Tools to search Pubmed.](https://docs.agno.com/tools/toolkits/pubmed)[Python ------ Tools to write and run Python code.](https://docs.agno.com/tools/toolkits/python)[Resend ------ Tools to send emails using Resend.](https://docs.agno.com/tools/toolkits/resend)[SearxNG ------- Tools to search the web using SearxNG.](https://docs.agno.com/tools/toolkits/searxng)[Serpapi ------- Tools to search Google, YouTube, and more using Serpapi.](https://docs.agno.com/tools/toolkits/serpapi)[Shell ----- Tools to run shell commands.](https://docs.agno.com/tools/toolkits/shell)[Slack ----- Tools to interact with Slack.](https://docs.agno.com/tools/toolkits/slack)[Sleep ----- Tools to pause execution for a given number of seconds.](https://docs.agno.com/tools/toolkits/sleep)[Spider ------ Tools to crawl websites.](https://docs.agno.com/tools/toolkits/spider)[SQL --- Tools to run SQL queries.](https://docs.agno.com/tools/toolkits/sql)[Tavily ------ Tools to search the web using Tavily.](https://docs.agno.com/tools/toolkits/tavily)[Todoist ------- Tools to interact with Todoist.](https://docs.agno.com/tools/toolkits/todoist)[Twilio ------ Tools to interact with Twilio services.](https://docs.agno.com/tools/toolkits/twilio)[X (Twitter) ----------- Tools to interact with X.](https://docs.agno.com/tools/toolkits/x)[Website ------- Tools to scrape websites.](https://docs.agno.com/tools/toolkits/website)[Wikipedia --------- Tools to search Wikipedia.](https://docs.agno.com/tools/toolkits/wikipedia)[YFinance -------- Tools to search Yahoo Finance.](https://docs.agno.com/tools/toolkits/yfinance)[YouTube ------- Tools to search YouTube.](https://docs.agno.com/tools/toolkits/youtube)[Zendesk ------- Tools to search Zendesk.](https://docs.agno.com/tools/toolkits/zendesk)[Zoom ---- Tools to interact with Zoom.](https://docs.agno.com/tools/toolkits/zoom)


