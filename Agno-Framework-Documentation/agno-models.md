================================================================================
Section 4: Content from https://docs.agno.com/models/openai
================================================================================

Title: OpenAI - Agno

URL Source: https://docs.agno.com/models/openai

Markdown Content:
The GPT models are the best in class LLMs and used as the default LLM by **Agents**.

OpenAI supports a variety of world-class models. See their models [here](https://platform.openai.com/docs/models).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `gpt-4o` is good for most general use-cases.
*   `gpt-4o-mini` model is good for smaller tasks and faster inference.
*   `o1` models are good for complex reasoning and multi-step tasks.
*   `o3-mini` is a strong reasoning model with support for tool-calling and structured outputs, but at a much lower cost.

OpenAI have tier based rate limits. See the [docs](https://platform.openai.com/docs/guides/rate-limits/usage-tiers) for more information.

Authentication
--------------

Set your `OPENAI_API_KEY` environment variable. You can get one [from OpenAI here](https://platform.openai.com/account/api-keys).

Example
-------

Use `OpenAIChat` with your `Agent`:

Params
------

For more information, please refer to the [OpenAI docs](https://platform.openai.com/docs/api-reference/chat/create) as well.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The id of the OpenAI model to use. |
| `name` | `str` | `"OpenAIChat"` | The name of this chat model instance. |
| `provider` | `str` | `"OpenAI " + id` | The provider of the model. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `metadata` | `Optional[Dict[str, Any]]` | `None` | Additional metadata to include with the request. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | `None` | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | `None` | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `max_completion_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in completions. |
| `modalities` | `Optional[List[str]]` | `None` | List of modalities supported by the model. |
| `audio` | `Optional[Dict[str, Any]]` | `None` | Audio-specific parameters for the model. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | `None` | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | `None` | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | `None` | How many log probability results to return per token. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user. |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling. |
| `extra_headers` | `Optional[Any]` | `None` | Additional headers to send with the request. |
| `extra_query` | `Optional[Any]` | `None` | Additional query parameters to send with the request. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with OpenAI. |
| `organization` | `Optional[str]` | `None` | The organization to use for API requests. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for API requests. |
| `timeout` | `Optional[float]` | `None` | The timeout for API requests. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[OpenAIClient]` | `None` | The OpenAI client instance. |
| `async_client` | `Optional[AsyncOpenAIClient]` | `None` | The asynchronous OpenAI client instance. |
| `structured_outputs` | `bool` | `False` | Whether to use the structured outputs from the Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content. |
| `override_system_role` | `bool` | `True` | Whether to override the system role. |
| `system_message_role` | `str` | `"developer"` | The role to map the system message to. |

`OpenAIChat` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 5: Content from https://docs.agno.com/models/openai-like
================================================================================

Title: OpenAI Like - Agno

URL Source: https://docs.agno.com/models/openai-like

Markdown Content:
OpenAI Like - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

OpenAI Like

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

OpenAI Like
===========

Many providers like Together, Groq, Sambanova, etc support the OpenAI API format. Use the `OpenAILike` model to access them by replacing the `base_url`.

[​](https://docs.agno.com/models/openai-like#example)

Example
----------------------------------------------------------------

agent.py

Copy

```python
from os import getenv
from agno.agent import Agent, RunResponse
from agno.models.openai.like import OpenAILike

agent = Agent(
    model=OpenAILike(
        id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        api_key=getenv("TOGETHER_API_KEY"),
        base_url="https://api.together.xyz/v1",
    )
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
```

[​](https://docs.agno.com/models/openai-like#params)

Params
--------------------------------------------------------------

`OpenAILike` also support all the params of [OpenAIChat](https://docs.agno.com/reference/models/openai)

[OpenAI](https://docs.agno.com/models/openai)[Anthropic Claude](https://docs.agno.com/models/anthropic)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Example](https://docs.agno.com/models/openai-like#example)
*   [Params](https://docs.agno.com/models/openai-like#params)



================================================================================
Section 6: Content from https://docs.agno.com/models/anthropic
================================================================================

Title: Anthropic Claude - Agno

URL Source: https://docs.agno.com/models/anthropic

Markdown Content:
Claude is a family of foundational AI models by Anthropic that can be used in a variety of applications. See their model comparisons [here](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `claude-3-5-sonnet-20241022` model is good for most use-cases and supports image input.
*   `claude-3-5-haiku-20241022` model is their fastest model.

Anthropic has rate limits on their APIs. See the [docs](https://docs.anthropic.com/en/api/rate-limits#response-headers) for more information.

Authentication
--------------

Set your `ANTHROPIC_API_KEY` environment. You can get one [from Anthropic here](https://console.anthropic.com/settings/keys).

Example
-------

Use `Claude` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"claude-3-5-sonnet-20241022"` | The id of the Anthropic Claude model to use |
| `name` | `str` | `"Claude"` | The name of the model |
| `provider` | `str` | `"Anthropic"` | The provider of the model |
| `max_tokens` | `Optional[int]` | `1024` | Maximum number of tokens to generate in the chat completion |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output |
| `stop_sequences` | `Optional[List[str]]` | `None` | A list of strings that the model should stop generating text at |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling |
| `top_k` | `Optional[int]` | `None` | Controls diversity via top-k sampling |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Anthropic |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration |
| `client` | `Optional[AnthropicClient]` | `None` | A pre-configured instance of the Anthropic client |
| `structured_outputs` | `bool` | `False` | Whether to use structured outputs with this Model |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content |
| `override_system_role` | `bool` | `True` | Whether to override the system role |
| `system_message_role` | `str` | `"assistant"` | The role to map the system message to |

`Claude` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 7: Content from https://docs.agno.com/models/aws-bedrock
================================================================================

Title: AWS Bedrock - Agno

URL Source: https://docs.agno.com/models/aws-bedrock

Markdown Content:
Use AWS Bedrock to access various foundation models on AWS. Manage your access to models [on the portal](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/model-catalog).

See all the [AWS Bedrock foundational models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). Not all Bedrock models support all features. See the [supported features for each model](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   For a Mistral model with generally good performance, look at `mistral.mistral-large-2402-v1:0`.
*   You can play with Amazon Nova models. Use `amazon.nova-pro-v1:0` for general purpose tasks.
*   For Claude models, see our [Claude integration](https://docs.agno.com/models/aws-claude).

Authentication
--------------

Set your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variables.

Get your keys from [here](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home).

Example
-------

Use `AwsBedrock` with your `Agent`:

Parameters
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistral.mistral-large-2402-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrock"` | The name identifier for the AWS Bedrock agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | `"None"` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `"None"` | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `stop_sequences` | `Optional[List[str]]` | `"None"` | A list of sequences where the API will stop generating further tokens. |
| `request_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |

`AwsBedrock` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 8: Content from https://docs.agno.com/models/aws-claude
================================================================================

Title: AWS Claude - Agno

URL Source: https://docs.agno.com/models/aws-claude

Markdown Content:
Use Claude models through AWS Bedrock. This provides a native Claude integration optimized for AWS infrastructure.

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `anthropic.claude-3-5-sonnet-20241022-v2:0` model is good for most use-cases and supports image input.
*   `anthropic.claude-3-5-haiku-20241022-v2:0` model is their fastest model.

Authentication
--------------

Set your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variables.

Get your keys from [here](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home).

Example
-------

Use `Claude` with your `Agent`:

Parameters
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"anthropic.claude-3-5-sonnet-20240620-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrockAnthropicClaude"` | The name identifier for the Claude agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `client` | `Optional[AnthropicBedrock]` | `None` | The client for making requests to the Anthropic Bedrock service. |
| `async_client` | `Optional[AsyncAnthropicBedrock]` | `None` | The asynchronous client for making requests to the Anthropic Bedrock service. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | `"None"` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `"None"` | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `top_k` | `Optional[int]` | `"None"` | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `stop_sequences` | `Optional[List[str]]` | `"None"` | A list of sequences where the API will stop generating further tokens. |
| `request_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |

`Claude` is a subclass of [`AnthropicClaude`](https://docs.agno.com/models/anthropic) and has access to the same params.



================================================================================
Section 9: Content from https://docs.agno.com/models/azure-ai-foundry
================================================================================

Title: Azure AI Foundry - Agno

URL Source: https://docs.agno.com/models/azure-ai-foundry

Markdown Content:
Use various open source models hosted on Azure’s infrastructure. Learn more [here](https://learn.microsoft.com/azure/ai-services/models).

Azure AI Foundry provides access to models like `Phi`, `Llama`, `Mistral`, `Cohere` and more.

Authentication
--------------

Navigate to Azure AI Foundry on the [Azure Portal](https://portal.azure.com/) and create a service. Then set your environment variables:

Example
-------

Use `AzureAIFoundry` with your `Agent`:

Advanced Examples
-----------------

View more examples [here](https://docs.agno.com/examples/models/azure/ai_foundry).

Parameters
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | The specific model ID used for generating responses. This field is required. |
| `name` | `str` | `"AzureOpenAI"` | The name identifier for the agent. |
| `provider` | `str` | `"Azure"` | The provider of the model. |
| `api_key` | `Optional[str]` | `"None"` | The API key for authenticating requests to the Azure OpenAI service. |
| `api_version` | `str` | `"2024-10-21"` | The version of the Azure OpenAI API to use. |
| `azure_endpoint` | `Optional[str]` | `"None"` | The endpoint URL for the Azure OpenAI service. |
| `client` | `Optional[ChatCompletionsClient]` | `None` | The client for making requests to the Azure OpenAI service. |
| `async_client` | `Optional[AsyncChatCompletionsClient]` | `None` | The asynchronous client for making requests to the Azure OpenAI service. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. Higher values make output more random. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `frequency_penalty` | `Optional[float]` | `None` | Reduces repetition by penalizing tokens based on their frequency. |
| `presence_penalty` | `Optional[float]` | `None` | Reduces repetition by penalizing tokens that have appeared at all. |
| `top_p` | `Optional[float]` | `None` | Controls diversity by limiting cumulative probability of tokens considered. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Sequences where the model will stop generating further tokens. |
| `seed` | `Optional[int]` | `None` | Random seed for deterministic outputs. |
| `model_extras` | `Optional[Dict[str, Any]]` | `None` | Additional model-specific parameters. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass with the request. |
| `timeout` | `Optional[float]` | `None` | Timeout in seconds for API requests. |
| `max_retries` | `Optional[int]` | `None` | Maximum number of retries for failed requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | Custom HTTP client for making requests. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |

`AzureAIFoundry` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 10: Content from https://docs.agno.com/models/azure-openai
================================================================================

Title: Azure OpenAI - Agno

URL Source: https://docs.agno.com/models/azure-openai

Markdown Content:
Azure OpenAI - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Azure

Azure OpenAI

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
        *   [Azure AI Foundry](https://docs.agno.com/models/azure-ai-foundry)
        *   [Azure OpenAI](https://docs.agno.com/models/azure-openai)
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Azure

Azure OpenAI
============

Use OpenAI models through Azure’s infrastructure. Learn more [here](https://learn.microsoft.com/azure/ai-services/openai/overview).

Azure OpenAI provides access to OpenAI’s models like `GPT-4o`, `o3-mini`, and more.

[​](https://docs.agno.com/models/azure-openai#authentication)

Authentication
-------------------------------------------------------------------------------

Navigate to Azure OpenAI on the [Azure Portal](https://portal.azure.com/) and create a service. Then, using the Azure AI Studio portal, create a deployment and set your environment variables:

Mac

Windows

Copy

```bash
export AZURE_OPENAI_API_KEY=***
export AZURE_OPENAI_ENDPOINT=***  # Of the form https://<your-resource-name>.openai.azure.com/openai/deployments/<your-deployment-name>
# Optional:
# export AZURE_OPENAI_DEPLOYMENT=***
```

[​](https://docs.agno.com/models/azure-openai#example)

Example
-----------------------------------------------------------------

Use `AzureOpenAI` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from os import getenv

agent = Agent(
    model=AzureOpenAI(id="gpt-4o"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")
```

[​](https://docs.agno.com/models/azure-openai#advanced-examples)

Advanced Examples
-------------------------------------------------------------------------------------

View more examples [here](https://docs.agno.com/examples/models/azure/openai).

[​](https://docs.agno.com/models/azure-openai#parameters)

Parameters
-----------------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | The specific model ID used for generating responses. This field is required. |
| `name` | `str` | `"AzureOpenAI"` | The name identifier for the agent. |
| `provider` | `str` | `"Azure"` | The provider of the model. |
| `api_key` | `Optional[str]` | `"None"` | The API key for authenticating requests to the Azure OpenAI service. |
| `api_version` | `str` | `"2024-10-21"` | The version of the Azure OpenAI API to use. |
| `azure_endpoint` | `Optional[str]` | `"None"` | The endpoint URL for the Azure OpenAI service. |
| `azure_deployment` | `Optional[str]` | `"None"` | The deployment name or ID in Azure. |
| `azure_ad_token` | `Optional[str]` | `"None"` | The Azure Active Directory token for authenticating requests. |
| `azure_ad_token_provider` | `Optional[Any]` | `"None"` | The provider for obtaining Azure Active Directory tokens. |
| `openai_client` | `Optional[AzureOpenAIClient]` | `"None"` | An instance of AzureOpenAIClient provided for making API requests. |

`AzureOpenAI` also supports the parameters of [OpenAI](https://docs.agno.com/reference/models/openai).

[Azure AI Foundry](https://docs.agno.com/models/azure-ai-foundry)[Cohere](https://docs.agno.com/models/cohere)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/azure-openai#authentication)
*   [Example](https://docs.agno.com/models/azure-openai#example)
*   [Advanced Examples](https://docs.agno.com/models/azure-openai#advanced-examples)
*   [Parameters](https://docs.agno.com/models/azure-openai#parameters)



================================================================================
Section 11: Content from https://docs.agno.com/models/cohere
================================================================================

Title: Cohere - Agno

URL Source: https://docs.agno.com/models/cohere

Markdown Content:
Leverage Cohere’s powerful command models and more.

[Cohere](https://cohere.com/) has a wide range of models and is really good for fine-tuning. See their library of models [here](https://docs.cohere.com/v2/docs/models).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `command` model is good for most basic use-cases.
*   `command-light` model is good for smaller tasks and faster inference.
*   `command-r7b-12-2024` model is good with RAG tasks, complex reasoning and multi-step tasks.

Cohere also supports fine-tuning models. Here is a [guide](https://docs.cohere.com/v2/docs/fine-tuning) on how to do it.

Cohere has tier-based rate limits. See the [docs](https://docs.cohere.com/v2/docs/rate-limits) for more information.

Authentication
--------------

Set your `CO_API_KEY` environment variable. Get your key from [here](https://dashboard.cohere.com/api-keys).

Example
-------

Use `Cohere` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"command-r-plus"` | The specific model ID used for generating responses. |
| `name` | `str` | `"cohere"` | The name identifier for the agent. |
| `provider` | `str` | `"Cohere"` | The provider of the model. |
| `temperature` | `Optional[float]` | `None` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `top_k` | `Optional[int]` | `None` | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `frequency_penalty` | `Optional[float]` | `None` | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `presence_penalty` | `Optional[float]` | `None` | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `add_chat_history` | `bool` | `False` | Whether to add chat history to the Cohere messages instead of using the conversation\_id. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating requests to the Cohere service. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `cohere_client` | `Optional[CohereClient]` | `None` | A pre-configured instance of the Cohere client. |
| `structured_outputs` | `bool` | `False` | Whether to use structured outputs with this Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content. |
| `override_system_role` | `bool` | `True` | Whether to override the system role. |
| `system_message_role` | `str` | `"system"` | The role to map the system message to. |

`Cohere` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 12: Content from https://docs.agno.com/models/deepseek
================================================================================

Title: DeepSeek - Agno

URL Source: https://docs.agno.com/models/deepseek

Markdown Content:
DeepSeek - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

DeepSeek

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

DeepSeek
========

DeepSeek is a platform for providing endpoints for Large Language models. See their library of models [here](https://api-docs.deepseek.com/quick_start/pricing).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `deepseek-chat` model is good for most basic use-cases.
*   `deepseek-reasoner` model is good for complex reasoning and multi-step tasks.

DeepSeek does not have rate limits. See their [docs](https://api-docs.deepseek.com/quick_start/rate_limit) for information about how to deal with slower responses during high traffic.

[​](https://docs.agno.com/models/deepseek#authentication)

Authentication
---------------------------------------------------------------------------

Set your `DEEPSEEK_API_KEY` environment variable. Get your key from [here](https://platform.deepseek.com/api_keys).

Mac

Windows

Copy

```bash
export DEEPSEEK_API_KEY=***
```

[​](https://docs.agno.com/models/deepseek#example)

Example
-------------------------------------------------------------

Use `DeepSeek` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.deepseek import DeepSeek

agent = Agent(model=DeepSeek(), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](https://docs.agno.com/examples/models/deepseek).

[​](https://docs.agno.com/models/deepseek#params)

Params
-----------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"deepseek-chat"` | The specific model ID used for generating responses. |
| `name` | `str` | `"DeepSeek"` | The name identifier for the DeepSeek model. |
| `provider` | `str` | `"DeepSeek"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key used for authenticating requests to the DeepSeek service. Retrieved from the environment variable `DEEPSEEK_API_KEY`. |
| `base_url` | `str` | `"https://api.deepseek.com"` | The base URL for making API requests to the DeepSeek service. |

`DeepSeek` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[Cohere](https://docs.agno.com/models/cohere)[Fireworks](https://docs.agno.com/models/fireworks)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/deepseek#authentication)
*   [Example](https://docs.agno.com/models/deepseek#example)
*   [Params](https://docs.agno.com/models/deepseek#params)



================================================================================
Section 13: Content from https://docs.agno.com/models/fireworks
================================================================================

Title: Fireworks - Agno

URL Source: https://docs.agno.com/models/fireworks

Markdown Content:
Fireworks - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

Fireworks

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

Fireworks
=========

Fireworks is a platform for providing endpoints for Large Language models.

[​](https://docs.agno.com/models/fireworks#authentication)

Authentication
----------------------------------------------------------------------------

Set your `FIREWORKS_API_KEY` environment variable. Get your key from [here](https://fireworks.ai/account/api-keys).

Mac

Windows

Copy

```bash
export FIREWORKS_API_KEY=***
```

[​](https://docs.agno.com/models/fireworks#example)

Example
--------------------------------------------------------------

Use `Fireworks` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.fireworks import Fireworks

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/firefunction-v2"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](https://docs.agno.com/examples/models/fireworks).

[​](https://docs.agno.com/models/fireworks#params)

Params
------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"accounts/fireworks/models/llama-v3p1-405b-instruct"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Fireworks: {id}"` | The name identifier for the agent. Defaults to "Fireworks: " followed by the model ID. |
| `provider` | `str` | `"Fireworks"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. Retrieved from the environment variable FIREWORKS\_API\_KEY. |
| `base_url` | `str` | `"https://api.fireworks.ai/inference/v1"` | The base URL for making API requests to the Fireworks service. |

`Fireworks` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[DeepSeek](https://docs.agno.com/models/deepseek)[Gemini](https://docs.agno.com/models/google)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/fireworks#authentication)
*   [Example](https://docs.agno.com/models/fireworks#example)
*   [Params](https://docs.agno.com/models/fireworks#params)



================================================================================
Section 14: Content from https://docs.agno.com/models/google
================================================================================

Title: Gemini - Agno

URL Source: https://docs.agno.com/models/google

Markdown Content:
Use Google’s Gemini models through Google AI Studio - a platform providing access to large language models. Learn more [here](https://ai.google.dev/aistudio).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `gemini-1.5-flash` is good for most use-cases.
*   `gemini-1.5-flash-8b` is their most cost-effective model.
*   `gemini-2.0-flash-exp` is their strongest multi-modal model.

Authentication
--------------

You can use Gemini models through either Google AI Studio or Google Cloud’s Vertex AI:

### Google AI Studio

Set your `GOOGLE_API_KEY` environment variable. You can get one [from Google here](https://ai.google.dev/aistudio).

### Vertex AI

To use Vertex AI:

1.  Install Google Cloud CLI and authenticate:

2.  Set your project ID (optional if `GOOGLE_CLOUD_PROJECT` is set):

Example
-------

Use `Gemini` with your `Agent`:

Parameters
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gemini-2.0-flash-exp"` | The specific Gemini model ID to use. |
| `name` | `str` | `"Gemini"` | The name of this Gemini model instance. |
| `provider` | `str` | `"Google"` | The provider of the model. |
| `function_declarations` | `Optional[List[FunctionDeclaration]]` | `None` | List of function declarations for the model. |
| `generation_config` | `Optional[Any]` | `None` | Configuration for text generation. |
| `safety_settings` | `Optional[Any]` | `None` | Safety settings for the model. |
| `generative_model_kwargs` | `Optional[Dict[str, Any]]` | `None` | Additional keyword arguments for the generative model. |
| `api_key` | `Optional[str]` | `None` | API key for authentication. |
| `vertexai` | `bool` | `False` | Whether to use Vertex AI instead of Google AI Studio. |
| `project_id` | `Optional[str]` | `None` | Google Cloud project ID for Vertex AI. |
| `location` | `Optional[str]` | `None` | Google Cloud region for Vertex AI. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the client. |
| `client` | `Optional[GeminiClient]` | `None` | The underlying generative model client. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the output. Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. Only consider tokens whose cumulative probability exceeds this value. |
| `top_k` | `Optional[int]` | `None` | Only consider the top k tokens for text generation. |
| `max_output_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `stop_sequences` | `Optional[list[str]]` | `None` | List of sequences where the model should stop generating further tokens. |
| `logprobs` | `Optional[bool]` | `None` | Whether to return log probabilities of the output tokens. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `seed` | `Optional[int]` | `None` | Random seed for deterministic text generation. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the request. |

`Gemini` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 15: Content from https://docs.agno.com/models/groq
================================================================================

Title: Groq - Agno

URL Source: https://docs.agno.com/models/groq

Markdown Content:
Groq offers blazing-fast API endpoints for large language models.

See all the Groq supported models [here](https://console.groq.com/docs/models).

*   We recommend using `llama-3.3-70b-versatile` for general use
*   We recommend `llama-3.1-8b-instant` for a faster result.
*   We recommend using `llama-3.2-90b-vision-preview` for image understanding.

#### Multimodal Support

With Groq we support `Image` as input

Authentication
--------------

Set your `GROQ_API_KEY` environment variable. Get your key from [here](https://console.groq.com/keys).

Example
-------

Use `Groq` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama-3.3-70b-versatile"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Groq"` | The name identifier for the agent. |
| `provider` | `str` | `"Groq"` | The provider of the model. |
| `frequency_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `logit_bias` | `Optional[Any]` | `None` | A JSON object that modifies the likelihood of specified tokens appearing in the completion by mapping token IDs to bias values between -100 and 100. |
| `logprobs` | `Optional[bool]` | `None` | Whether to return log probabilities of the output tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `response_format` | `Optional[Dict[str, Any]]` | `None` | Specifies the format that the model must output. Setting to `{ "type": "json_object" }` enables JSON mode, ensuring the message generated is valid JSON. |
| `seed` | `Optional[int]` | `None` | A seed value for deterministic sampling, ensuring repeated requests with the same seed and parameters return the same result. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_logprobs` | `Optional[int]` | `None` | The number of top log probabilities to return for each generated token. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user, helping to monitor and detect abuse. |
| `extra_headers` | `Optional[Any]` | `None` | Additional headers to include in API requests. |
| `extra_query` | `Optional[Any]` | `None` | Additional query parameters to include in API requests. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating requests to the service. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for making API requests to the service. |
| `timeout` | `Optional[int]` | `None` | The timeout duration for requests, specified in seconds. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retry attempts for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all API requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all API requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | A custom HTTP client for making API requests. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[GroqClient]` | `None` | An instance of GroqClient provided for making API requests. |
| `async_client` | `Optional[AsyncGroqClient]` | `None` | An instance of AsyncGroqClient provided for making asynchronous API requests. |

`Groq` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 16: Content from https://docs.agno.com/models/huggingface
================================================================================

Title: HuggingFace - Agno

URL Source: https://docs.agno.com/models/huggingface

Markdown Content:
Hugging Face provides a wide range of state-of-the-art language models tailored to diverse NLP tasks, including text generation, summarization, translation, and question answering. These models are available through the Hugging Face Transformers library and are widely adopted due to their ease of use, flexibility, and comprehensive documentation.

Explore HuggingFace’s language models [here](https://huggingface.co/docs/text-generation-inference/en/supported_models).

Authentication
--------------

Set your `HF_TOKEN` environment. You can get one [from HuggingFace here](https://huggingface.co/settings/tokens).

Example
-------

Use `HuggingFace` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"meta-llama/Meta-Llama-3-8B-Instruct"` | The id of the HuggingFace model to use. |
| `name` | `str` | `"HuggingFace"` | The name of this chat model instance. |
| `provider` | `str` | `"HuggingFace"` | The provider of the model. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | `None` | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | `None` | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | `None` | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | `None` | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | `None` | How many log probability results to return per token. |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The Access Token for authenticating with HuggingFace. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for API requests. |
| `timeout` | `Optional[float]` | `None` | The timeout for API requests. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[InferenceClient]` | `None` | The HuggingFace Hub Inference client instance. |
| `async_client` | `Optional[AsyncInferenceClient]` | `None` | The asynchronous HuggingFace Hub client instance. |

`HuggingFace` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 17: Content from https://docs.agno.com/models/mistral
================================================================================

Title: Mistral - Agno

URL Source: https://docs.agno.com/models/mistral

Markdown Content:
Mistral is a platform for providing endpoints for Large Language models. See their library of models [here](https://docs.mistral.ai/getting-started/models/models_overview/).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `codestral` model is good for code generation and editing.
*   `mistral-large-latest` model is good for most use-cases.
*   `open-mistral-nemo` is a free model that is good for most use-cases.
*   `pixtral-12b-2409` is a vision model that is good for OCR, transcribing documents, and image comparison. It is not always capable at tool calling.

Mistral has tier-based rate limits. See the [docs](https://docs.mistral.ai/deployment/laplateforme/tier/) for more information.

Authentication
--------------

Set your `MISTRAL_API_KEY` environment variable. Get your key from [here](https://console.mistral.ai/api-keys/).

Example
-------

Use `Mistral` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistral-large-latest"` | The ID of the model. |
| `name` | `str` | `"MistralChat"` | The name of the model. |
| `provider` | `str` | `"Mistral"` | The provider of the model. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in output generation. |
| `max_tokens` | `Optional[int]` | `None` | Maximum number of tokens to generate. |
| `top_p` | `Optional[float]` | `None` | Controls diversity of output generation. |
| `random_seed` | `Optional[int]` | `None` | Seed for random number generation. |
| `safe_mode` | `bool` | `False` | Enables content filtering. |
| `safe_prompt` | `bool` | `False` | Applies content filtering to prompts. |
| `response_format` | `Optional[Union[Dict[str, Any], ChatCompletionResponse]]` | `None` | Specifies the desired response format. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional request parameters. |
| `api_key` | `Optional[str]` | `None` | Your Mistral API key. |
| `endpoint` | `Optional[str]` | `None` | Custom API endpoint URL. |
| `max_retries` | `Optional[int]` | `None` | Maximum number of API call retries. |
| `timeout` | `Optional[int]` | `None` | Timeout for API calls in seconds. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional client parameters. |
| `mistral_client` | `Optional[MistralClient]` | `None` | Custom Mistral client instance. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `frequency_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `logit_bias` | `Optional[Any]` | `None` | A JSON object that modifies the likelihood of specified tokens appearing in the completion by mapping token IDs to bias values between -100 and 100. |
| `logprobs` | `Optional[bool]` | `None` | Whether to return log probabilities of the output tokens. |
| `presence_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `top_logprobs` | `Optional[int]` | `None` | The number of top log probabilities to return for each generated token. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user, helping to monitor and detect abuse. |

`MistralChat` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 18: Content from https://docs.agno.com/models/nvidia
================================================================================

Title: Nvidia - Agno

URL Source: https://docs.agno.com/models/nvidia

Markdown Content:
Nvidia - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

Nvidia

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

Nvidia
======

NVIDIA offers a suite of high-performance language models optimized for advanced NLP tasks. These models are part of the NeMo framework, which provides tools for training, fine-tuning and deploying state-of-the-art models efficiently. NVIDIA’s language models are designed to handle large-scale workloads with GPU acceleration for faster inference and training. We recommend experimenting with NVIDIA’s models to find the best fit for your application.

Explore NVIDIA’s models [here](https://build.nvidia.com/models).

[​](https://docs.agno.com/models/nvidia#authentication)

Authentication
-------------------------------------------------------------------------

Set your `NVIDIA_API_KEY` environment variable. Get your key [from Nvidia here](https://build.nvidia.com/explore/discover).

Mac

Windows

Copy

```bash
export NVIDIA_API_KEY=***
```

[​](https://docs.agno.com/models/nvidia#example)

Example
-----------------------------------------------------------

Use `Nvidia` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.nvidia import Nvidia

agent = Agent(model=Nvidia(), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")

```

View more examples [here](https://docs.agno.com/examples/models/nvidia).

[​](https://docs.agno.com/models/nvidia#params)

Params
---------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"nvidia/llama-3.1-nemotron-70b-instruct"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Nvidia"` | The name identifier for the Nvidia agent. |
| `provider` | `str` | \- | The provider of the model, combining "Nvidia" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Nvidia service. Retrieved from the environment variable `NVIDIA_API_KEY`. |
| `base_url` | `str` | `"https://integrate.api.nvidia.com/v1"` | The base URL for making API requests to the Nvidia service. |

`Nvidia` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[Mistral](https://docs.agno.com/models/mistral)[Ollama](https://docs.agno.com/models/ollama)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/nvidia#authentication)
*   [Example](https://docs.agno.com/models/nvidia#example)
*   [Params](https://docs.agno.com/models/nvidia#params)



================================================================================
Section 19: Content from https://docs.agno.com/models/ollama
================================================================================

Title: Ollama - Agno

URL Source: https://docs.agno.com/models/ollama

Markdown Content:
Run Large Language Models locally with Ollama

[Ollama](https://ollama.com/) is a fantastic tool for running models locally.

Ollama supports multiple open-source models. See the library [here](https://ollama.com/library).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

*   `llama3.3` models are good for most basic use-cases.
*   `qwen` models perform specifically well with tool use.
*   `deepseek-r1` models have strong reasoning capabilities.
*   `phi4` models are powerful, while being really small in size.

Set up a model
--------------

Install [ollama](https://ollama.com/) and run a model using

This gives you an interactive session with the model.

Alternatively, to download the model to be used in an Agno agent

Example
-------

After you have the model locally, use the `Ollama` model class to access it

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama3.1"` | The ID of the model to use. |
| `name` | `str` | `"Ollama"` | The name of the model. |
| `provider` | `str` | `"Ollama"` | The provider of the model. |
| `format` | `Optional[Any]` | `None` | The format of the response. |
| `options` | `Optional[Any]` | `None` | Additional options to pass to the model. |
| `keep_alive` | `Optional[Union[float, str]]` | `None` | The keep alive time for the model. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the request. |
| `host` | `Optional[str]` | `None` | The host to connect to. |
| `timeout` | `Optional[Any]` | `None` | The timeout for the connection. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the client. |
| `client` | `Optional[OllamaClient]` | `None` | A pre-configured instance of the Ollama client. |
| `async_client` | `Optional[AsyncOllamaClient]` | `None` | A pre-configured instance of the asynchronous Ollama client. |
| `structured_outputs` | `bool` | `False` | Whether to use the structured outputs with this Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |

`Ollama` is a subclass of the [Model](https://docs.agno.com/reference/models/model) class and has access to the same params.



================================================================================
Section 20: Content from https://docs.agno.com/models/openrouter
================================================================================

Title: OpenRouter - Agno

URL Source: https://docs.agno.com/models/openrouter

Markdown Content:
OpenRouter - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

OpenRouter

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

OpenRouter
==========

OpenRouter is a platform for providing endpoints for Large Language models.

[​](https://docs.agno.com/models/openrouter#authentication)

Authentication
-----------------------------------------------------------------------------

Set your `OPENROUTER_API_KEY` environment variable. Get your key from [here](https://openrouter.ai/settings/keys).

Mac

Windows

Copy

```bash
export OPENROUTER_API_KEY=***
```

[​](https://docs.agno.com/models/openrouter#example)

Example
---------------------------------------------------------------

Use `OpenRouter` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.openrouter import OpenRouter

agent = Agent(
    model=OpenRouter(id="gpt-4o"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

```

[​](https://docs.agno.com/models/openrouter#params)

Params
-------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The specific model ID used for generating responses. |
| `name` | `str` | `"OpenRouter"` | The name identifier for the OpenRouter agent. |
| `provider` | `str` | `"OpenRouter:"+id` | The provider of the model, combining "OpenRouter" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the OpenRouter service. Retrieved from the environment variable `OPENROUTER_API_KEY`. |
| `base_url` | `str` | `"https://openrouter.ai/api/v1"` | The base URL for making API requests to the OpenRouter service. |
| `max_tokens` | `int` | `1024` | The maximum number of tokens to generate in the response. |

`OpenRouter` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[Ollama](https://docs.agno.com/models/ollama)[Perplexity](https://docs.agno.com/models/perplexity)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/openrouter#authentication)
*   [Example](https://docs.agno.com/models/openrouter#example)
*   [Params](https://docs.agno.com/models/openrouter#params)



================================================================================
Section 21: Content from https://docs.agno.com/models/perplexity
================================================================================

Title: Perplexity - Agno

URL Source: https://docs.agno.com/models/perplexity

Markdown Content:
Perplexity - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

Perplexity

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

Perplexity
==========

Perplexity offers powerful language models with built-in web search capabilities, enabling advanced research and Q&A functionality.

Explore Perplexity’s models [here](https://docs.perplexity.ai/guides/model-cards).

[​](https://docs.agno.com/models/perplexity#authentication)

Authentication
-----------------------------------------------------------------------------

Set your `PERPLEXITY_API_KEY` environment variable. Get your key [from Perplexity here](https://www.perplexity.ai/settings/api).

Mac

Windows

Copy

```bash
export PERPLEXITY_API_KEY=***
```

[​](https://docs.agno.com/models/perplexity#example)

Example
---------------------------------------------------------------

Use `Perplexity` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.perplexity import Perplexity

agent = Agent(model=Perplexity(id="sonar-pro"), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")

```

View more examples [here](https://docs.agno.com/examples/models/perplexity).

[​](https://docs.agno.com/models/perplexity#params)

Params
-------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"sonar-pro"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Perplexity"` | The name identifier for the Perplexity agent. |
| `provider` | `str` | `"Perplexity" + id` | The provider of the model, combining "Perplexity" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Perplexity service. Retrieved from the environment variable `PERPLEXITY_API_KEY`. |
| `base_url` | `str` | `"https://api.perplexity.ai/"` | The base URL for making API requests to the Perplexity service. |
| `max_tokens` | `int` | `1024` | The maximum number of tokens to generate in the response. |

`Perplexity` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[OpenRouter](https://docs.agno.com/models/openrouter)[Sambanova](https://docs.agno.com/models/sambanova)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/perplexity#authentication)
*   [Example](https://docs.agno.com/models/perplexity#example)
*   [Params](https://docs.agno.com/models/perplexity#params)



================================================================================
Section 22: Content from https://docs.agno.com/models/sambanova
================================================================================

Title: Sambanova - Agno

URL Source: https://docs.agno.com/models/sambanova

Markdown Content:
Sambanova - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

Sambanova

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

Sambanova
=========

Sambanova is a platform for providing endpoints for Large Language models. Note that Sambanova currently does not support function calling.

[​](https://docs.agno.com/models/sambanova#authentication)

Authentication
----------------------------------------------------------------------------

Set your `SAMBANOVA_API_KEY` environment variable. Get your key from [here](https://cloud.sambanova.ai/apis).

Mac

Windows

Copy

```bash
export SAMBANOVA_API_KEY=***
```

[​](https://docs.agno.com/models/sambanova#example)

Example
--------------------------------------------------------------

Use `Sambanova` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.sambanova import Sambanova

agent = Agent(model=Sambanova(), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

```

[​](https://docs.agno.com/models/sambanova#params)

Params
------------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"Meta-Llama-3.1-8B-Instruct"` | The id of the Sambanova model to use |
| `name` | `str` | `"Sambanova"` | The name of this chat model instance |
| `provider` | `str` | `"Sambanova"` | The provider of the model |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Sambanova (defaults to environment variable SAMBANOVA\_API\_KEY) |
| `base_url` | `str` | `"https://api.sambanova.ai/v1"` | The base URL for API requests |

`Sambanova` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[Perplexity](https://docs.agno.com/models/perplexity)[Together](https://docs.agno.com/models/together)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/sambanova#authentication)
*   [Example](https://docs.agno.com/models/sambanova#example)
*   [Params](https://docs.agno.com/models/sambanova#params)



================================================================================
Section 23: Content from https://docs.agno.com/models/together
================================================================================

Title: Together - Agno

URL Source: https://docs.agno.com/models/together

Markdown Content:
Together - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

Search...

Navigation

Models

Together

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
    
    *   [Introduction](https://docs.agno.com/models/introduction)
    *   [Compatibility](https://docs.agno.com/models/compatibility)
    *   [OpenAI](https://docs.agno.com/models/openai)
    *   [OpenAI Like](https://docs.agno.com/models/openai-like)
    *   [Anthropic Claude](https://docs.agno.com/models/anthropic)
    *   AWS
        
    *   Azure
        
    *   [Cohere](https://docs.agno.com/models/cohere)
    *   [DeepSeek](https://docs.agno.com/models/deepseek)
    *   [Fireworks](https://docs.agno.com/models/fireworks)
    *   [Gemini](https://docs.agno.com/models/google)
    *   [Groq](https://docs.agno.com/models/groq)
    *   [HuggingFace](https://docs.agno.com/models/huggingface)
    *   [Mistral](https://docs.agno.com/models/mistral)
    *   [Nvidia](https://docs.agno.com/models/nvidia)
    *   [Ollama](https://docs.agno.com/models/ollama)
    *   [OpenRouter](https://docs.agno.com/models/openrouter)
    *   [Perplexity](https://docs.agno.com/models/perplexity)
    *   [Sambanova](https://docs.agno.com/models/sambanova)
    *   [Together](https://docs.agno.com/models/together)
    *   [xAI](https://docs.agno.com/models/xai)
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

Models

Together
========

Together is a platform for providing endpoints for Large Language models. See their library of models [here](https://www.together.ai/models).

We recommend experimenting to find the best-suited model for your use-case.

[​](https://docs.agno.com/models/together#authentication)

Authentication
---------------------------------------------------------------------------

Set your `TOGETHER_API_KEY` environment variable. Get your key [from Together here](https://api.together.xyz/settings/api-keys).

Mac

Windows

Copy

```bash
export TOGETHER_API_KEY=***
```

[​](https://docs.agno.com/models/together#example)

Example
-------------------------------------------------------------

Use `Together` with your `Agent`:

agent.py

Copy

```python
from agno.agent import Agent, RunResponse
from agno.models.together import Together

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
```

View more examples [here](https://docs.agno.com/examples/models/together).

[​](https://docs.agno.com/models/together#params)

Params
-----------------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistralai/Mixtral-8x7B-Instruct-v0.1"` | The id of the Together model to use. |
| `name` | `str` | `"Together"` | The name of this chat model instance. |
| `provider` | `str` | `"Together " + id` | The provider of the model. |
| `api_key` | `Optional[str]` | `None` | The API key to authorize requests to Together. Defaults to environment variable TOGETHER\_API\_KEY. |
| `base_url` | `str` | `"https://api.together.xyz/v1"` | The base URL for API requests. |
| `monkey_patch` | `bool` | `False` | Whether to apply monkey patching. |

`Together` also supports the params of [OpenAI](https://docs.agno.com/reference/models/openai).

[Sambanova](https://docs.agno.com/models/sambanova)[xAI](https://docs.agno.com/models/xai)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Authentication](https://docs.agno.com/models/together#authentication)
*   [Example](https://docs.agno.com/models/together#example)
*   [Params](https://docs.agno.com/models/together#params)



================================================================================
Section 24: Content from https://docs.agno.com/models/vertexai
================================================================================

Title: Welcome to Agno - Agno

URL Source: https://docs.agno.com/models/vertexai

Markdown Content:
Welcome to Agno - Agno
===============
  

[Agno home page![Image 1: light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![Image 2: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](https://docs.agno.com/)

Search or ask...

Ctrl K

*   [Discord](https://agno.link/discord)
*   [Community](https://community.agno.com/)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)
*   [agno-agi/agno 19,022](https://github.com/agno-agi/agno)

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

[​](https://docs.agno.com/models/vertexai#simple-fast-and-agnostic)

Simple, Fast, and Agnostic
-------------------------------------------------------------------------------------------------

Agno is designed with three core principles:

*   **Simplicity**: No graphs, chains, or convoluted patterns — just pure python.
*   **Uncompromising Performance**: Blazing fast agents with a minimal memory footprint.
*   **Truly Agnostic**: Any model, any provider, any modality. Agno is designed to be the container for AGI.

[​](https://docs.agno.com/models/vertexai#key-features)

Key features
-----------------------------------------------------------------------

Here’s why you should build Agents with Agno:

*   **Lightning Fast**: Agent creation is 5000x faster than LangGraph (see [performance](https://github.com/agno-agi/agno#performance)).
*   **Model Agnostic**: Use any model, any provider, no lock-in.
*   **Multi Modal**: Native support for text, image, audio and video.
*   **Multi Agent**: Delegate tasks across a team of specialized agents.
*   **Memory Management**: Store user sessions and agent state in a database.
*   **Knowledge Stores**: Use vector databases for Agentic RAG or dynamic few-shot.
*   **Structured Outputs**: Make Agents respond with structured data.
*   **Monitoring**: Track agent sessions and performance in real-time on [agno.com](https://app.agno.com/).

[​](https://docs.agno.com/models/vertexai#get-started)

Get Started
---------------------------------------------------------------------

If you’re new to Agno, start here to build your first Agent.

[Build your first Agent ---------------------- Learn how to build Agents with Agno](https://docs.agno.com/get-started/agents)[Agent Playground ---------------- Chat with your Agents using a beautiful Agent UI](https://docs.agno.com/get-started/playground)[Agent Observability ------------------- Monitor your Agents on [agno.com](https://app.agno.com/)](https://docs.agno.com/get-started/monitoring)

After that, checkout the [Examples Gallery](https://docs.agno.com/examples) to discover real-world applications built with Agno.

[​](https://docs.agno.com/models/vertexai#build-with-agno)

Build with Agno
-----------------------------------------------------------------------------

Agno is a battle-tested framework with best-in-class performance, checkout the following guides to dive-in:

[Agents ------ Learn core Agent concepts](https://docs.agno.com/agents)[Models ------ Use any model, any provider, no lock-in](https://docs.agno.com/models)[Tools ----- Use 100s of tools to extend your Agents](https://docs.agno.com/tools)[Knowledge --------- Add domain-specific knowledge to your Agents](https://docs.agno.com/knowledge)[Vector Databases ---------------- Add semantic search and retrieval to your Agents](https://docs.agno.com/vectordb)[Storage ------- Persist agent states and conversations in a database](https://docs.agno.com/storage)[Memory ------ Remember user details and session summaries](https://docs.agno.com/agents/memory)[Embeddings ---------- Generate embeddings for your knowledge base](https://docs.agno.com/embedder)[Workflows --------- Build complex workflows with Agents](https://docs.agno.com/workflows)

[Your first Agent](https://docs.agno.com/get-started/agents)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com/)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.agno.com)

On this page

*   [Simple, Fast, and Agnostic](https://docs.agno.com/models/vertexai#simple-fast-and-agnostic)
*   [Key features](https://docs.agno.com/models/vertexai#key-features)
*   [Get Started](https://docs.agno.com/models/vertexai#get-started)
*   [Build with Agno](https://docs.agno.com/models/vertexai#build-with-agno)


