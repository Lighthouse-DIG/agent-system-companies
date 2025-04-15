from typing import Any
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server import Server  # Base server class

from mcp import McpError

from mcp.server.sse import SseServerTransport  # SSE transport implementation
from starlette.applications import Starlette  # ASGI framework
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Mount, Route
from starlette.responses import PlainTextResponse

import uvicorn  # ASGI server
from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten



name = "companies"
USER_AGENT = f"{name}-app/1.0"
formatter_ = KeyValueRecursiveFlatten()
# Initialize FastMCP server
mcp = FastMCP(name)

load_dotenv()
env_path = find_dotenv()
print(f"Loading .env from: {env_path}")  # Debug
load_dotenv(env_path)


#ALPHAVANTAGE APIKEY
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
if not apikey:
        mcp.send_log_message(
        level=McpError.error,
        data="API key not found. Set ALPHAVANTAGE_API_KEY environment variable."
    )
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
async def get_balance_sheet(symbol: str) -> str:
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
        return formatter_(data)
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_income_statement(symbol: str) -> str:
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
        return formatter_(data)
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_cash_flow(symbol: str) -> str:
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
        return formatter_(data)
    
    return f"Unexpected error : {data}"


@mcp.tool()
async def get_earnings(symbol: str) -> str:
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
        return formatter_(data)
    
    return f"Unexpected error : {data}"





async def verification_file(request: Request) -> PlainTextResponse:
    content=os.getenv("VERIFICATION_KEY")
    return PlainTextResponse(content)


# HTML for the homepage that displays "MCP Server"
async def homepage(request: Request) -> HTMLResponse:
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MCP Server</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            h1 {
                margin-bottom: 10px;
            }
            button {
                background-color: #f8f8f8;
                border: 1px solid #ccc;
                padding: 8px 16px;
                margin: 10px 0;
                cursor: pointer;
                border-radius: 4px;
            }
            button:hover {
                background-color: #e8e8e8;
            }
            .status {
                border: 1px solid #ccc;
                padding: 10px;
                min-height: 20px;
                margin-top: 10px;
                border-radius: 4px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <h1>MCP Server</h1>
        
        <p>Server is running correctly!</p>
        
        <button id="connect-button">Connect to SSE</button>
        
        <div class="status" id="status">Connection status will appear here...</div>
        
        <script>
            document.getElementById('connect-button').addEventListener('click', function() {
                // Redirect to the SSE connection page or initiate the connection
                const statusDiv = document.getElementById('status');
                
                try {
                    const eventSource = new EventSource('/sse');
                    
                    statusDiv.textContent = 'Connecting...';
                    
                    eventSource.onopen = function() {
                        statusDiv.textContent = 'Connected to SSE';
                    };
                    
                    eventSource.onerror = function() {
                        statusDiv.textContent = 'Error connecting to SSE';
                        eventSource.close();
                    };
                    
                    eventSource.onmessage = function(event) {
                        statusDiv.textContent = 'Received: ' + event.data;
                    };
                    
                    // Add a disconnect option
                    const disconnectButton = document.createElement('button');
                    disconnectButton.textContent = 'Disconnect';
                    disconnectButton.addEventListener('click', function() {
                        eventSource.close();
                        statusDiv.textContent = 'Disconnected';
                        this.remove();
                    });
                    
                    document.body.appendChild(disconnectButton);
                    
                } catch (e) {
                    statusDiv.textContent = 'Error: ' + e.message;
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html_content)


# Create a Starlette application with SSE transport
def create_starlette_app(mcp_server: Server, *, debug: bool = False) -> Starlette:
    """Create a Starlette application that can server the provied mcp server with SSE.
    
    This sets up the HTTP routes and SSE connection handling.
    """
    # Create an SSE transport with a path for messages
    sse = SseServerTransport("/messages/")

    # Handler for SSE connections
    async def handle_sse(request: Request) -> None:
        async with sse.connect_sse(
                request.scope,
                request.receive,
                request._send,  # access private method
        ) as (read_stream, write_stream):
            # Run the MCP server with the SSE streams
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options(),
            )

    # Create and return the Starlette application
    return Starlette(
        debug=debug,
        routes=[
            Route("/", endpoint=homepage),  # Add the homepage route
            Route("/sse", endpoint=handle_sse),  # Endpoint for SSE connections
            Mount("/messages/", app=sse.handle_post_message),  # Endpoint for messages
            Route("/mcp-verification.txt", endpoint=verification_file)
        ],
    )

# Instanciar la aplicación Starlette antes del bloque main
mcp_server = mcp._mcp_server
starlette_app = create_starlette_app(mcp_server, debug=True)

if __name__ == "__main__":
    # Get the underlying MCP server from FastMCP wrapper
    #mcp_server = mcp._mcp_server

    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Run MCP SSE-based server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=8080, help='Port to listen on')
    args = parser.parse_args()

    # Create and run the Starlette application
    #starlette_app = create_starlette_app(mcp_server, debug=True)
    uvicorn.run(starlette_app, host=args.host, port=args.port)