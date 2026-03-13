# app/agent/agent.py
from app.tools.rag_tool import rag_tool
from app.tools.search_tool import search_tool
from app.tools.web_search_tool import web_tool
from app.tools.calculator_tool import calculator_tool

def ask_agent(query: str):
    """
    Simple router to automatically decide which tool to run
    based on the type of query.
    """
    query_lower = query.lower()

    # Math queries
    if any(char in query for char in "+-*/"):
        return calculator_tool.func(query)

    # PDF / RAG queries
    if "paper" in query_lower or "attention all you need" in query_lower or "pdf" in query_lower:
        return rag_tool.func(query)

    # Otherwise, use web search
    return web_tool.func(query)