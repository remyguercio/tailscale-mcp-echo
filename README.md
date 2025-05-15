# Identity Aware MCP Server for Tailscale

<img width="1125" alt="TailscaleMCPIdentityHero" src="https://github.com/user-attachments/assets/1e05e3a6-019d-4e16-b591-3691bcee16e6" />

Create an identiy aware MCP server that runs inside your private Tailscale network (Tailnet). This example levearges identity headers that are passed through to applications running behind `tailscale serve`.

Using this as starting point you can create MCP servers that are identity aware (with access to the logged in user's email) and can access internal APIs or services on thier behalf.

## Instructions

### Starting the Server

1. If you don't already have a Tailnet setup you'll need to [signup for one](https://tailscale.com).
2. Create an [API auth key](https://login.tailscale.com/admin/settings/keys) and save it into a `.env` file in the root of this project with the following format: `TS_AUTHKEY=tskey-auth-...`
3. With Docker already installed, run `docker compose up` to start the server.

This will spin up two containers. The MCP server and a Tailscale container running `tailscale serve` as a proxy to your tailnet.

### Using the Server

If you have an MCP Client that supports direct access to Streaming HTTP MCP servers, then you should be able to connect to the server by pointing it to `https://ts-mcp-echo.yourtailnetname.ts.net/mcp`.

#### Claude Desktop

Claude desktop does not currently support remote MCP servers (only stdio), but you can use the [mcp-remote](https://github.com/geelen/mcp-remote) tool (or any other proxy) to connect to it.

1. Install mcp-remote with `npm install -g mcp-remote`
2. Add the following configuration to your `claude_desktop_config.json` file:

    ```json
        {
            "mcpServers": {
                "tailscale-remote-echo-example": {
                    "command": "npx",
                    "args": [
                        "mcp-remote",
                        "https://ts-mcp-echo.yourtailnetname.ts.net/mcp"
                    ]
                }
            }
        }
    ```

    You can find your tailnet name by visiting the [Tailscale admin console DNS page](https://login.tailscale.com/admin/dns).
3. Restart Claude Desktop.
4. You should now see a new MCP server called `tailscale-remote-echo-example` with a `greet` tool.
5. Ask Claude `Who am I logged into my tailnet as?` allow the tool, and wait for the response!
