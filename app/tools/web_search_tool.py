from langchain_core.tools import Tool
from ddgs import DDGS


def web_search(query: str):

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

    output = "\n".join([r["body"] for r in results])

    return output


web_tool = Tool(
    name="web_search",
    func=web_search,
    description="Search the internet for latest information."
)