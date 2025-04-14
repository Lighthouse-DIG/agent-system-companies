from typing import Any
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from mcp.server.fastmcp import FastMCP
from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten

name = "companies"
USER_AGENT = f"{name}-app/1.0"
formatter_ = KeyValueRecursiveFlatten()
# Initialize FastMCP server
mcp = FastMCP(name)

load_dotenv()
env_path = find_dotenv()
print(f"Cargando .env desde: {env_path}")  # Debug
load_dotenv(env_path)

apikey = os.getenv("ALPHAVANTAGE_API_KEY")
print(f"API Key: {'Cargada correctamente' if apikey else 'No se encontró'}")

if not apikey:
    raise ValueError("ALPHAVANTAGE_API_KEY is not set in the environment variables.")

data_request = FundamentalData(apikey=apikey)

async def async_call(function, data):
    try:
        # Ejecuta la llamada en un hilo aparte (no bloquea el event loop)
        return await asyncio.to_thread(getattr(data_request, function)(symbol=data))
    except Exception as error:
        print(f"Error en async_call: {error}")
        return error

@mcp.tool()
async def get_overview(symbol: str) -> str:
    """Get Overview from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_overview", symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(data)
    
    return f"Unexpected error : {data}"

@mcp.tool()
async def get_balance_sheet(symbol: str) -> str:
    """Get Balance Sheet from company

    Args:
        symbol: company stock symbol
    """
    
    #data = await asyncio.to_thread(data_request.get_overview, symbol)
    data = await async_call("get_balance_sheet", symbol)

    if isinstance(data, tuple):
        return "Unable to fetch company data."

    #if not data["features"]:
    #    return "No active alerts for this state."
    elif isinstance(data, dict):
        return formatter_(data)
    
    return f"Unexpected error : {data}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')