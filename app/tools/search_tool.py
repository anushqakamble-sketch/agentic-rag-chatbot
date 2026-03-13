from langchain_core.tools import Tool
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# load vector database
db = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 4})


def search_knowledge_base(query: str):
    docs = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in docs])


search_tool = Tool(
    name="knowledge_base_search",
    func=search_knowledge_base,
    description="Search information from the PDF knowledge base."
)