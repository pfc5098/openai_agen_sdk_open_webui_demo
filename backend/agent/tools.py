from openai_agents.tools import web_search
from openai_agents import Tool
import requests


def crypto_price(symbol: str = "bitcoin", currency: str = "usd") -> str:
    """
    Fetch the current price of a cryptocurrency using the CoinGecko API.
    Args:
        symbol: The slug of the cryptocurrency (e.g., 'bitcoin').
        currency: The fiat currency to quote the price in (e.g., 'usd').
    Returns:
        A human-readable string with the price information.
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get(symbol, {}).get(currency)
        if price is None:
            return f"Price information for {symbol} in {currency} is not available."
        return f"The current price of {symbol} is {price} {currency.upper()}."
    except Exception as e:
        return f"Error fetching price: {e}"


# Tool instance for the crypto price function
crypto_price_tool = Tool.from_function(
    crypto_price,
    name="crypto_price",
    description="Get the current price of a cryptocurrency. Provide the 'symbol' and optional 'currency'.",
)

# Export the built-in web search tool for use by the agent
web_search_tool = web_search
