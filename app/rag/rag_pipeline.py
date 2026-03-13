from dotenv import load_dotenv
import os

load_dotenv()

from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from app.rag.prompt_template import custom_prompt


VECTOR_STORE_PATH = "vector_store"


def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def load_vector_store(embeddings):
    print("Loading FAISS vector store...")

    db = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db


def load_llm():
    print("Loading LLM from Ollama...")

    return OllamaLLM(
        model="mistral",
        temperature=0
    )


def build_rag_pipeline():

    embeddings = load_embeddings()

    db = load_vector_store(embeddings)

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
    )

    llm = load_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": custom_prompt}
    )

    return qa_chain


# Test run
if __name__ == "__main__":

    qa_chain = build_rag_pipeline()

    query = "What is Transformer?"

    result = qa_chain.invoke({"query": query})

    print("\nAnswer:\n", result["result"])