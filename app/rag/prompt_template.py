from langchain_core.prompts import PromptTemplate

template = """
You are an AI assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer in a clear and concise way.
"""

custom_prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)