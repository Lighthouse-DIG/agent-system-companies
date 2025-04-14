from typing import Any
import os
import asyncio
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_overview import format_overview
# Initialize FastMCP server
mcp = FastMCP("companies")

load_dotenv()

# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")

if not apikey:
    raise ValueError("ALPHAVANTAGE_API_KEY is not set in the environment variables.")

data_request = FundamentalData(apikey=apikey)


@mcp.tool()
async def get_overview(symbol: str) -> str:
    """Get Overview from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_overview, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company data."


@mcp.tool()
async def get_dividends(symbol: str) -> str:
    """Get Dividends from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_dividends, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company dividends."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company dividends."


@mcp.tool()
async def get_splits(symbol: str) -> str:
    """Get Splits from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_splits, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company splits."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company splits."


@mcp.tool()
async def get_balance_sheet(symbol: str) -> str:
    """Get Balance Sheet from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_balance_sheet, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company balance sheet."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company balance sheet."


@mcp.tool()
async def get_income_statement(symbol: str) -> str:
    """Get Income Statement from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_income_statement, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company income statement."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company income statement."


@mcp.tool()
async def get_cash_flow(symbol: str) -> str:
    """Get Cash Flow from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_cash_flow, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company cash flow."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company cash flow."


@mcp.tool()
async def get_earnings(symbol: str) -> str:
    """Get Earnings from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_earnings, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company earnings."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company earnings."


@mcp.tool()
async def get_etf_metrics(symbol: str) -> str:
    """Get ETF Metrics from company

    Args:
        symbol: company stock symbol
    """
    
    data = await asyncio.to_thread(data_request.get_etf_metrics, symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company ETF metrics."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return format_overview(data)
    
    return "Unexpected error fetching company ETF metrics."


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')