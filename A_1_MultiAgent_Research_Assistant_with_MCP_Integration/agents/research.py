import os
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0
)


async def call_search(query):

    server_params = StdioServerParameters(
        command="python",
        args=["mcp/server.py"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "web_search",
                {"query": query}
            )

            return result.content[0].text


def research_agent(state):

    query = state["plan"]

    search_result = asyncio.run(call_search(query))

    prompt = f"""
You are a travel research assistant.

Context:
{search_result}

User request:
{state['question']}

Generate a travel plan.
"""

    response = llm.invoke(prompt)

    return {
        "research_result": search_result,
        "final_answer": response.content
    }