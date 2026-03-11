from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

mcp = FastMCP("travel-tools")

search = DuckDuckGoSearchRun()


@mcp.tool()
def web_search(query: str) -> str:
    """
    Search web for travel information.
    """
    return search.invoke(query)


if __name__ == "__main__":
    mcp.run()