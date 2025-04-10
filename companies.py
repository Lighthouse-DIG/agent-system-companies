from typing import Any
import httpx
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_overview import format_overview
# Initialize FastMCP server
mcp = FastMCP("companies")

load_dotenv()

# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
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

    return format_overview(data)



if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')