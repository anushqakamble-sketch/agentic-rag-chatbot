from langchain_core.tools import Tool
from app.rag.rag_pipeline import build_rag_pipeline


# Lazy loading the pipeline
qa_chain = None


def rag_search(query: str):

    global qa_chain

    if qa_chain is None:
        qa_chain = build_rag_pipeline()

    result = qa_chain.invoke({"query": query})

    return result["result"]


rag_tool = Tool(
    name="rag_search",
    func=rag_search,
    description="Answer questions using the internal PDF knowledge base."
)