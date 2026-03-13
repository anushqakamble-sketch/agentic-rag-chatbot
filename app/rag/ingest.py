import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


PDF_FOLDER = "data/pdfs"
VECTOR_STORE_PATH = "vector_store"


def load_documents():
    documents = []

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, file)
            print(f"Loading {file}")

            loader = PyPDFLoader(path)
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} pages")
    return documents


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(documents)

    print(f"Created {len(docs)} chunks")
    return docs


def create_vector_store(docs):

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local(VECTOR_STORE_PATH)

    print("Vector database created successfully!")


def main():

    documents = load_documents()

    docs = split_documents(documents)

    create_vector_store(docs)


if __name__ == "__main__":
    main()