import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Path to knowledge base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_PATH = os.path.join(BASE_DIR, "knowledge_base")

# Load all .txt files
loader = DirectoryLoader(
    KB_PATH,
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()
print(f"Loaded {len(documents)} documents.")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks.")

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector store
vector_db = FAISS.from_documents(chunks, embedding_model)

# Save locally
vector_db.save_local("faiss_index")

print("✅ FAISS index created successfully!")