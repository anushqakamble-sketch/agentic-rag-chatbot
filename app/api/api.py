# app/api/api.py
from fastapi import FastAPI, Query
from app.agent.agent import ask_agent

app = FastAPI(title="Agentic RAG Chatbot API")

@app.get("/ask")
def ask(query: str = Query(..., description="Your question for the agent")):
    """
    Receives a query and returns the answer from the Agentic RAG Chatbot.
    """
    try:
        answer = ask_agent(query)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}