import os
import sys
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

transport = os.getenv("MCP_TRANSPORT", "streamable-http").strip()

# Validate transport
if transport not in {"streamable-http", "sse"}:
    print(f"ERROR: Unsupported transport '{transport}'", file=sys.stderr)
    sys.exit(1)

mcp = FastMCP(name="Tailscale Identity Echo Server")

@mcp.tool()
async def greet() -> str:
    req: Request = get_http_request()
    return (
        f"Hello, {req.headers.get('Tailscale-User-Name','Unknown')}! "
        f"You are logged in as {req.headers.get('Tailscale-User-Login','Unknown')}."
    )

def main():
    print(f"Starting FastMCP with transport={transport}", file=sys.stderr)
    try:
        mcp.run(transport=transport, port=8080, host="0.0.0.0")
    except Exception as e:
        print(f"FATAL: Server startup failed: {e}", file=sys.stderr)
        sys.exit(1)
    print("i exit")

# When run with "python main.py", this fires.
if __name__ == "__main__":
    main()
