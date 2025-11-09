from openai_agents import Agent
from openai_agents.tools import web_search
from .tools import crypto_price_tool


def get_agent() -> Agent:
    """Create and return an OpenAI Agent with web search and crypto price tools."""
    return Agent(
        name="OpenAIWebAgent",
        instructions="You are a helpful assistant that can perform web searches and fetch cryptocurrency prices.",
        tools=[web_search, crypto_price_tool],
        model="gpt-4.1"
    )
