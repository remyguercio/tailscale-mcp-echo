from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

mcp = FastMCP(name="Tailscale Identity Echo Server")


@mcp.tool()
async def greet() -> str:
    """Reads the indentity request headers passed in from Tailscale Serve and returns a greeting.

    Returns:
        str: A greeting containing the user's name, login (typically an email or Github handle),
        and profile picture URL.
    """

    request: Request = get_http_request()

    user_login = request.headers.get("Tailscale-User-Login", "Unknown")
    user_name = request.headers.get("Tailscale-User-Name", "Unknown")
    user_profile_picture = request.headers.get("Tailscale-User-Profile-Pic", "Unknown")

    return f"""Hello, {user_name}!
You're logged in to Tailscale as {user_login}.
With a profile picture at this URL: {user_profile_picture}."""
