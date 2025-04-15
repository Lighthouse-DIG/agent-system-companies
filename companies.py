from typing import Any
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from mcp.server.fastmcp import FastMCP
from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten
from tools.filter_date import filter_annual_reports

name = "companies"
USER_AGENT = f"{name}-app/1.0"
formatter_ = KeyValueRecursiveFlatten()
# Initialize FastMCP server
mcp = FastMCP(name)

load_dotenv()
env_path = find_dotenv()
print(f"Loading .env from: {env_path}")  # Debug
load_dotenv(env_path)

apikey = os.getenv("ALPHAVANTAGE_API_KEY")
print(f"API Key: {'Loaded correctly' if apikey else 'Not found'}")

if not apikey:
    raise ValueError("ALPHAVANTAGE_API_KEY is not set in the environment variables.")

data_request = FundamentalData(apikey=apikey)

async def async_call(function, symbol):
    try:
        # Ejecuta la llamada en un hilo aparte (no bloquea el event loop)
        return await asyncio.to_thread(getattr(data_request, function), symbol=symbol)
        #return getattr(data_request, function)(symbol=symbol)
    except Exception as error:
        print(f"Error en async_call: {error}, {symbol}")
        return f"Error en async_call: {error}, {symbol}"

@mcp.tool()
async def get_overview(symbol: str) -> str:
    """Get Overview from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_overview", symbol=symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(data)
    
    return f"Unexpected error : {data}"

@mcp.tool()
async def get_balance_sheet(symbol: str, start_date:str|None, end_date:str|None) -> str:
    """Get Balance Sheet from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_balance_sheet", symbol=symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(filter_annual_reports(data, start_date=start_date, end_date=end_date))
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_income_statement(symbol: str, start_date:str|None, end_date:str|None) -> str:
    """Get Income Statement from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_income_statement", symbol=symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(filter_annual_reports(data, start_date=start_date, end_date=end_date))
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_cash_flow(symbol: str, start_date:str|None, end_date:str|None) -> str:
    """Get CASH FLOW from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_cash_flow", symbol=symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(filter_annual_reports(data, start_date=start_date, end_date=end_date))
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_earnings(symbol: str, start_date:str|None, end_date:str|None) -> str:
    """Get Earnings from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_earnings", symbol=symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(filter_annual_reports(data, start_date=start_date, end_date=end_date))
    
    return f"Unexpected error : {data}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')