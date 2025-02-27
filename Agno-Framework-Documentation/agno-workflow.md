
================================================================================
Section 1: Content from https://docs.agno.com/workflows/introduction
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/workflows/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Workflows

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
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Introduction
============

Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

### 

[​](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

[​](https://docs.agno.com/workflows/introduction#example-blog-post-generator)

Example: Blog Post Generator
-------------------------------------------------------------------------------------------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### 

[​](https://docs.agno.com/workflows/introduction#create-the-workflow)

Create the Workflow

1.  Define your workflow as a class by inheriting from the `Workflow` class.

blog\_post\_generator.py

Copy

```python
from agno.workflow import Workflow

class BlogPostGenerator(Workflow):
    pass
```

2.  Add one or more agents to the workflow.

blog\_post\_generator.py

Copy

```python

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )
```

3.  Implement your logic in the `run()` method.

blog\_post\_generator.py

Copy

```python

import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 2: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
```

4.  Add [caching](https://docs.agno.com/workflows/session_state) to the workflow where needed.

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)
```

5.  Run the workflow

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold]\n✨",
        default="Why Cats Secretly Run the Internet",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_blog_post_workflows",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(topic=topic, use_cache=True)

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

### 

[​](https://docs.agno.com/workflows/introduction#run-the-workflow)

Run the workflow

Install libraries

Copy

```shell
pip install agno openai duckduckgo-search sqlalchemy
```

Run the workflow

Copy

```shell
python blog_post_generator.py
```

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.

Copy

```shell
python blog_post_generator.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)Checkout more examples in the [examples](https://docs.agno.com/examples/use-cases/advanced) section.

[Voyage AI](https://docs.agno.com/embedder/voyageai)[Caching](https://docs.agno.com/workflows/session_state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build a workflow:](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)
*   [Example: Blog Post Generator](https://docs.agno.com/workflows/introduction#example-blog-post-generator)
*   [Create the Workflow](https://docs.agno.com/workflows/introduction#create-the-workflow)
*   [Run the workflow](https://docs.agno.com/workflows/introduction#run-the-workflow)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)


================================================================================
Section 13: Content from https://docs.agno.com/workflows/session_state
================================================================================

Title: Caching - Agno

URL Source: https://docs.agno.com/workflows/session_state

Markdown Content:
Caching - Agno
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

Workflows

Caching

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
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Caching
=======

**Use the `session_state` to cache intermediate results in a database.**

All Workflows come with a `session_state` dictionary that you can use to cache intermediate results. Provide your workflows with `storage` and a `session_id` to enable caching.

For example, you can use the `SqliteWorkflowStorage` to cache results in a Sqlite database.

Copy

```python
# Create the workflow
generate_blog_post = BlogPostGenerator(
    session_id="my-session-id",
    storage=SqliteWorkflowStorage(
        table_name="generate_blog_post_workflows",
        db_file="tmp/workflows.db",
    ),
)
```

Then in the `run()` method, you can read from and add to the `session_state` as needed.

Copy

```python

class BlogPostGenerator(Workflow):
    # ... agents
    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        # Read from the session state cache
        if use_cache and "blog_posts" in self.session_state:
            logger.info("Checking if cached blog post exists")
            for cached_blog_post in self.session_state["blog_posts"]:
                if cached_blog_post["topic"] == topic:
                    logger.info("Found cached blog post")
                    yield RunResponse(
                        run_id=self.run_id,
                        event=RunEvent.workflow_completed,
                        content=cached_blog_post["blog_post"],
                    )
                    return

        # ... generate the blog post

        # Save to session state for future runs
        if "blog_posts" not in self.session_state:
            self.session_state["blog_posts"] = []
        self.session_state["blog_posts"].append({"topic": topic, "blog_post": self.writer.run_response.content})
```

When the workflow starts, the `session_state` for that particular `session_id` is read from the database and when the workflow ends, the `session_state` is stored in the database.

You can always call `self.write_to_storage()` to save the `session_state` to the database at any time. Incase you need to abort the workflow but want to store the intermediate results.

View the [Blog Post Generator](https://docs.agno.com/workflows/introduction#full-example-blog-post-generator) for an example of how to use session state for caching.

[Introduction](https://docs.agno.com/workflows/introduction)[Postgres](https://docs.agno.com/workflows/storage/postgres)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)



================================================================================
Section 14: Content from https://docs.agno.com/workflows/advanced
================================================================================

Title: Advanced - Agno

URL Source: https://docs.agno.com/workflows/advanced

Markdown Content:
Workflows are all about control and flexibility. You have full control over the multi-agent process, how the input is processed, which agents are used and in what order.

You also have full control over how the output is streamed.

Streaming
---------

To stream the output, yield an `Iterator[RunResponse]` from the `run()` method of your workflow.

```
# Define the workflow
class GenerateNewsReport(Workflow):
    agent_1: Agent = ...

    agent_2: Agent = ...

    agent_3: Agent = ...

    def run(self, ...) -> Iterator[RunResponse]:
        # Run agents and gather the response
        # These can be batch responses, you can also stream intermediate results if you want
        final_agent_input = ...

        # Generate the final response from the writer agent
        agent_3_response_stream: Iterator[RunResponse] = self.agent_3.run(final_agent_input, stream=True)

        # Yield the response
        yield agent_3_response_stream

# Instantiate the workflow
generate_news_report = GenerateNewsReport()

# Run workflow and get the response as an iterator of RunResponse objects
report_stream: Iterator[RunResponse] = generate_news_report.run(...)

# Print the response
pprint_run_response(report_stream, markdown=True)
```

Batch
-----

Simply return a `RunResponse` object from the `run()` method of your workflow to return a single output.

```
# Define the workflow
class GenerateNewsReport(Workflow):
    agent_1: Agent = ...

    agent_2: Agent = ...

    agent_3: Agent = ...

    def run(self, ...) -> RunResponse:
        # Run agents and gather the response
        final_agent_input = ...

        # Generate the final response from the writer agent
        agent_3_response: RunResponse = self.agent_3.run(final_agent_input)

        # Return the response
        return agent_3_response

# Instantiate the workflow
generate_news_report = GenerateNewsReport()

# Run workflow and get the response as a RunResponse object
report: RunResponse = generate_news_report.run(...)

# Print the response
pprint_run_response(report, markdown=True)
```
================================================================================
Section 19: Content from https://docs.agno.com/workflows/introduction#how-to-build-a-workflow
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/workflows/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Workflows

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
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Introduction
============

Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

### 

[​](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

[​](https://docs.agno.com/workflows/introduction#example-blog-post-generator)

Example: Blog Post Generator
-------------------------------------------------------------------------------------------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### 

[​](https://docs.agno.com/workflows/introduction#create-the-workflow)

Create the Workflow

1.  Define your workflow as a class by inheriting from the `Workflow` class.

blog\_post\_generator.py

Copy

```python
from agno.workflow import Workflow

class BlogPostGenerator(Workflow):
    pass
```

2.  Add one or more agents to the workflow.

blog\_post\_generator.py

Copy

```python

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )
```

3.  Implement your logic in the `run()` method.

blog\_post\_generator.py

Copy

```python

import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 2: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
```

4.  Add [caching](https://docs.agno.com/workflows/session_state) to the workflow where needed.

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)
```

5.  Run the workflow

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold]\n✨",
        default="Why Cats Secretly Run the Internet",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_blog_post_workflows",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(topic=topic, use_cache=True)

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

### 

[​](https://docs.agno.com/workflows/introduction#run-the-workflow)

Run the workflow

Install libraries

Copy

```shell
pip install agno openai duckduckgo-search sqlalchemy
```

Run the workflow

Copy

```shell
python blog_post_generator.py
```

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.

Copy

```shell
python blog_post_generator.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)Checkout more examples in the [examples](https://docs.agno.com/examples/use-cases/advanced) section.

[Voyage AI](https://docs.agno.com/embedder/voyageai)[Caching](https://docs.agno.com/workflows/session_state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build a workflow:](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)
*   [Example: Blog Post Generator](https://docs.agno.com/workflows/introduction#example-blog-post-generator)
*   [Create the Workflow](https://docs.agno.com/workflows/introduction#create-the-workflow)
*   [Run the workflow](https://docs.agno.com/workflows/introduction#run-the-workflow)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)



================================================================================
Section 20: Content from https://docs.agno.com/workflows/introduction#example-blog-post-generator
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/workflows/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Workflows

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
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Introduction
============

Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

### 

[​](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

[​](https://docs.agno.com/workflows/introduction#example-blog-post-generator)

Example: Blog Post Generator
-------------------------------------------------------------------------------------------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### 

[​](https://docs.agno.com/workflows/introduction#create-the-workflow)

Create the Workflow

1.  Define your workflow as a class by inheriting from the `Workflow` class.

blog\_post\_generator.py

Copy

```python
from agno.workflow import Workflow

class BlogPostGenerator(Workflow):
    pass
```

2.  Add one or more agents to the workflow.

blog\_post\_generator.py

Copy

```python

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )
```

3.  Implement your logic in the `run()` method.

blog\_post\_generator.py

Copy

```python

import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 2: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
```

4.  Add [caching](https://docs.agno.com/workflows/session_state) to the workflow where needed.

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)
```

5.  Run the workflow

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold]\n✨",
        default="Why Cats Secretly Run the Internet",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_blog_post_workflows",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(topic=topic, use_cache=True)

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

### 

[​](https://docs.agno.com/workflows/introduction#run-the-workflow)

Run the workflow

Install libraries

Copy

```shell
pip install agno openai duckduckgo-search sqlalchemy
```

Run the workflow

Copy

```shell
python blog_post_generator.py
```

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.

Copy

```shell
python blog_post_generator.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)Checkout more examples in the [examples](https://docs.agno.com/examples/use-cases/advanced) section.

[Voyage AI](https://docs.agno.com/embedder/voyageai)[Caching](https://docs.agno.com/workflows/session_state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build a workflow:](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)
*   [Example: Blog Post Generator](https://docs.agno.com/workflows/introduction#example-blog-post-generator)
*   [Create the Workflow](https://docs.agno.com/workflows/introduction#create-the-workflow)
*   [Run the workflow](https://docs.agno.com/workflows/introduction#run-the-workflow)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)



================================================================================
Section 21: Content from https://docs.agno.com/workflows/introduction#create-the-workflow
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/workflows/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Workflows

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
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Introduction
============

Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

### 

[​](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

[​](https://docs.agno.com/workflows/introduction#example-blog-post-generator)

Example: Blog Post Generator
-------------------------------------------------------------------------------------------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### 

[​](https://docs.agno.com/workflows/introduction#create-the-workflow)

Create the Workflow

1.  Define your workflow as a class by inheriting from the `Workflow` class.

blog\_post\_generator.py

Copy

```python
from agno.workflow import Workflow

class BlogPostGenerator(Workflow):
    pass
```

2.  Add one or more agents to the workflow.

blog\_post\_generator.py

Copy

```python

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )
```

3.  Implement your logic in the `run()` method.

blog\_post\_generator.py

Copy

```python

import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 2: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
```

4.  Add [caching](https://docs.agno.com/workflows/session_state) to the workflow where needed.

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)
```

5.  Run the workflow

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold]\n✨",
        default="Why Cats Secretly Run the Internet",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_blog_post_workflows",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(topic=topic, use_cache=True)

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

### 

[​](https://docs.agno.com/workflows/introduction#run-the-workflow)

Run the workflow

Install libraries

Copy

```shell
pip install agno openai duckduckgo-search sqlalchemy
```

Run the workflow

Copy

```shell
python blog_post_generator.py
```

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.

Copy

```shell
python blog_post_generator.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)Checkout more examples in the [examples](https://docs.agno.com/examples/use-cases/advanced) section.

[Voyage AI](https://docs.agno.com/embedder/voyageai)[Caching](https://docs.agno.com/workflows/session_state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build a workflow:](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)
*   [Example: Blog Post Generator](https://docs.agno.com/workflows/introduction#example-blog-post-generator)
*   [Create the Workflow](https://docs.agno.com/workflows/introduction#create-the-workflow)
*   [Run the workflow](https://docs.agno.com/workflows/introduction#run-the-workflow)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)



================================================================================
Section 22: Content from https://docs.agno.com/workflows/introduction#run-the-workflow
================================================================================

Title: Introduction - Agno

URL Source: https://docs.agno.com/workflows/introduction

Markdown Content:
Introduction - Agno
===============
  

[Agno home page![Image 2: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 3: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,023](https://github.com/agno-agi/agno)

Search...

Navigation

Workflows

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
    
*   Knowledge
    
*   Chunking
    
*   VectorDbs
    
*   Storage
    
*   Embeddings
    
*   Workflows
    
    *   [Introduction](https://docs.agno.com/workflows/introduction)
    *   [Caching](https://docs.agno.com/workflows/session_state)
    *   Storage
        
    *   [Advanced](https://docs.agno.com/workflows/advanced)

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Workflows

Introduction
============

Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

### 

[​](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

[​](https://docs.agno.com/workflows/introduction#example-blog-post-generator)

Example: Blog Post Generator
-------------------------------------------------------------------------------------------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### 

[​](https://docs.agno.com/workflows/introduction#create-the-workflow)

Create the Workflow

1.  Define your workflow as a class by inheriting from the `Workflow` class.

blog\_post\_generator.py

Copy

```python
from agno.workflow import Workflow

class BlogPostGenerator(Workflow):
    pass
```

2.  Add one or more agents to the workflow.

blog\_post\_generator.py

Copy

```python

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )
```

3.  Implement your logic in the `run()` method.

blog\_post\_generator.py

Copy

```python

import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 2: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
```

4.  Add [caching](https://docs.agno.com/workflows/session_state) to the workflow where needed.

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)
```

5.  Run the workflow

blog\_post\_generator.py

Copy

```python
import json
from typing import Optional, Iterator

from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger

class NewsArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(..., description="Summary of the article if available.")

class SearchResults(BaseModel):
    articles: list[NewsArticle]

class BlogPostGenerator(Workflow):
    # Define an Agent that will search the web for a topic
    searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 articles."],
        response_model=SearchResults,
        structured_outputs=True,
    )

    # Define an Agent that will write the blog post
    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You will be provided with a topic and a list of top articles on that topic.",
            "Carefully read each article and generate a New York Times worthy blog post on that topic.",
            "Break the blog post into sections and provide key takeaways at the end.",
            "Make sure the title is catchy and engaging.",
            "Always provide sources, do not make up information or sources.",
        ],
        markdown=True,
    )

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        """This is where the main logic of the workflow is implemented."""

        logger.info(f"Generating a blog post on: {topic}")

        # Step 1: Use the cached blog post if use_cache is True
        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                yield RunResponse(content=cached_blog_post, event=RunEvent.workflow_completed)
                return

        # Step 2: Search the web for articles on the topic
        search_results: Optional[SearchResults] = self._get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Step 3: Write a blog post
        yield from self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        """Get the cached blog post for a topic."""

        logger.info("Checking if cached blog post exists")
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]):
        """Add a blog post to the cache."""

        logger.info(f"Saving blog post for topic: {topic}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        """Get the search results for a topic."""

        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)

                # Check if we got a valid response
                if not searcher_response or not searcher_response.content:
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Empty searcher response")
                    continue
                # Check if the response is of the expected SearchResults type
                if not isinstance(searcher_response.content, SearchResults):
                    logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS}: Invalid response type")
                    continue

                article_count = len(searcher_response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                return searcher_response.content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_ATTEMPTS} failed: {str(e)}")

        logger.error(f"Failed to get search results after {MAX_ATTEMPTS} attempts")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        """Write a blog post on a topic."""

        logger.info("Writing blog post")
        # Prepare the input for the writer
        writer_input = {"topic": topic, "articles": [v.model_dump() for v in search_results.articles]}
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the blog post in the cache
        self._add_blog_post_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold]\n✨",
        default="Why Cats Secretly Run the Internet",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_blog_post_workflows",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(topic=topic, use_cache=True)

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

### 

[​](https://docs.agno.com/workflows/introduction#run-the-workflow)

Run the workflow

Install libraries

Copy

```shell
pip install agno openai duckduckgo-search sqlalchemy
```

Run the workflow

Copy

```shell
python blog_post_generator.py
```

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.

Copy

```shell
python blog_post_generator.py
```

![Image 4](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)Checkout more examples in the [examples](https://docs.agno.com/examples/use-cases/advanced) section.

[Voyage AI](https://docs.agno.com/embedder/voyageai)[Caching](https://docs.agno.com/workflows/session_state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [How to build a workflow:](https://docs.agno.com/workflows/introduction#how-to-build-a-workflow)
*   [Example: Blog Post Generator](https://docs.agno.com/workflows/introduction#example-blog-post-generator)
*   [Create the Workflow](https://docs.agno.com/workflows/introduction#create-the-workflow)
*   [Run the workflow](https://docs.agno.com/workflows/introduction#run-the-workflow)

![Image 5](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/BlogPostGenerator.gif)



================================================================================
Section 23: Content from https://docs.agno.com/examples/use-cases/advanced
================================================================================

Title: Welcome to Agno - Agno

URL Source: https://docs.agno.com/examples/use-cases/advanced

Markdown Content:
Welcome to Agno - Agno
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

[​](https://docs.agno.com/examples/use-cases/advanced#simple-fast-and-agnostic)

Simple, Fast, and Agnostic
-------------------------------------------------------------------------------------------------------------

Agno is designed with three core principles:

*   **Simplicity**: No graphs, chains, or convoluted patterns — just pure python.
*   **Uncompromising Performance**: Blazing fast agents with a minimal memory footprint.
*   **Truly Agnostic**: Any model, any provider, any modality. Agno is designed to be the container for AGI.

[​](https://docs.agno.com/examples/use-cases/advanced#key-features)

Key features
-----------------------------------------------------------------------------------

Here’s why you should build Agents with Agno:

*   **Lightning Fast**: Agent creation is 5000x faster than LangGraph (see [performance](https://github.com/agno-agi/agno#performance)).
*   **Model Agnostic**: Use any model, any provider, no lock-in.
*   **Multi Modal**: Native support for text, image, audio and video.
*   **Multi Agent**: Delegate tasks across a team of specialized agents.
*   **Memory Management**: Store user sessions and agent state in a database.
*   **Knowledge Stores**: Use vector databases for Agentic RAG or dynamic few-shot.
*   **Structured Outputs**: Make Agents respond with structured data.
*   **Monitoring**: Track agent sessions and performance in real-time on [agno.com](https://app.agno.com/).

[​](https://docs.agno.com/examples/use-cases/advanced#get-started)

Get Started
---------------------------------------------------------------------------------

If you’re new to Agno, start here to build your first Agent.

[Build your first Agent ---------------------- Learn how to build Agents with Agno](https://docs.agno.com/get-started/agents)[Agent Playground ---------------- Chat with your Agents using a beautiful Agent UI](https://docs.agno.com/get-started/playground)[Agent Observability ------------------- Monitor your Agents on [agno.com](https://app.agno.com/)](https://docs.agno.com/get-started/monitoring)

After that, checkout the [Examples Gallery](https://docs.agno.com/examples) to discover real-world applications built with Agno.

[​](https://docs.agno.com/examples/use-cases/advanced#build-with-agno)

Build with Agno
-----------------------------------------------------------------------------------------

Agno is a battle-tested framework with best-in-class performance, checkout the following guides to dive-in:

[Agents ------ Learn core Agent concepts](https://docs.agno.com/agents)[Models ------ Use any model, any provider, no lock-in](https://docs.agno.com/models)[Tools ----- Use 100s of tools to extend your Agents](https://docs.agno.com/tools)[Knowledge --------- Add domain-specific knowledge to your Agents](https://docs.agno.com/knowledge)[Vector Databases ---------------- Add semantic search and retrieval to your Agents](https://docs.agno.com/vectordb)[Storage ------- Persist agent states and conversations in a database](https://docs.agno.com/storage)[Memory ------ Remember user details and session summaries](https://docs.agno.com/agents/memory)[Embeddings ---------- Generate embeddings for your knowledge base](https://docs.agno.com/embedder)[Workflows --------- Build complex workflows with Agents](https://docs.agno.com/workflows)

[Your first Agent](https://docs.agno.com/get-started/agents)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Simple, Fast, and Agnostic](https://docs.agno.com/examples/use-cases/advanced#simple-fast-and-agnostic)
*   [Key features](https://docs.agno.com/examples/use-cases/advanced#key-features)
*   [Get Started](https://docs.agno.com/examples/use-cases/advanced#get-started)
*   [Build with Agno](https://docs.agno.com/examples/use-cases/advanced#build-with-agno)



================================================================================
Section 24: Content from https://docs.agno.com/embedder/voyageai
================================================================================

Title: Voyage AI Embedder - Agno

URL Source: https://docs.agno.com/embedder/voyageai

Markdown Content:
Voyage AI Embedder - Agno
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

Embeddings

Voyage AI Embedder

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
    
    *   [Introduction](https://docs.agno.com/embedder/introduction)
    *   [OpenAI](https://docs.agno.com/embedder/openai)
    *   [Gemini](https://docs.agno.com/embedder/gemini)
    *   [Ollama](https://docs.agno.com/embedder/ollama)
    *   [Azure OpenAI](https://docs.agno.com/embedder/azure_openai)
    *   [Cohere](https://docs.agno.com/embedder/cohere)
    *   [Fireworks](https://docs.agno.com/embedder/fireworks)
    *   [HuggingFace](https://docs.agno.com/embedder/huggingface)
    *   [Mistral](https://docs.agno.com/embedder/mistral)
    *   [FastEmbed](https://docs.agno.com/embedder/qdrant_fastembed)
    *   [SentenceTransformers](https://docs.agno.com/embedder/sentencetransformers)
    *   [Together](https://docs.agno.com/embedder/together)
    *   [Voyage AI](https://docs.agno.com/embedder/voyageai)
*   Workflows
    

##### How to

*   [Install & Setup](https://docs.agno.com/how-to/install)
*   [Run Local Agent API](https://docs.agno.com/how-to/local-docker-guide)
*   [Contributing to Agno](https://docs.agno.com/how-to/contribute)
*   [Migrate from Phidata to Agno](https://docs.agno.com/how-to/phidata-to-agno)

Embeddings

Voyage AI Embedder
==================

The `VoyageAIEmbedder` class is used to embed text data into vectors using the Voyage AI API. Get your key from [here](https://dash.voyageai.com/api-keys).

[​](https://docs.agno.com/embedder/voyageai#usage)

Usage
-----------------------------------------------------------

cookbook/embedders/voyageai\_embedder.py

Copy

```python
from agno.agent import AgentKnowledge
from agno.vectordb.pgvector import PgVector
from agno.embedder.voyageai import VoyageAIEmbedder

# Embed sentence in database
embeddings = VoyageAIEmbedder().get_embedding("The quick brown fox jumps over the lazy dog.")

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Use an embedder in a knowledge base
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="voyageai_embeddings",
        embedder=VoyageAIEmbedder(),
    ),
    num_documents=2,
)
```

[​](https://docs.agno.com/embedder/voyageai#params)

Params
-------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"voyage-2"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `1024` | The dimensionality of the embeddings generated by the model. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the API request. Optional. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `base_url` | `str` | `"https://api.voyageai.com/v1/embeddings"` | The base URL for the API endpoint. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retries for API requests. Optional. |
| `timeout` | `Optional[float]` | \- | The timeout duration for API requests. Optional. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for configuring the API client. Optional. |
| `voyage_client` | `Optional[Client]` | \- | An instance of the Client to use for making API requests. Optional. |

[​](https://docs.agno.com/embedder/voyageai#developer-resources)

Developer Resources
---------------------------------------------------------------------------------------

*   View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/embedders/voyageai_embedder.py)

[Together](https://docs.agno.com/embedder/together)[Introduction](https://docs.agno.com/workflows/introduction)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Usage](https://docs.agno.com/embedder/voyageai#usage)
*   [Params](https://docs.agno.com/embedder/voyageai#params)
*   [Developer Resources](https://docs.agno.com/embedder/voyageai#developer-resources)


