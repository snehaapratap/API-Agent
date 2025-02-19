import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="data/chromadb_store")
collection = client.get_or_create_collection(name="code_embeddings")

def store_embedding(code_snippet, code_id):
    embedding = model.encode(code_snippet).tolist()
    collection.add(ids=[code_id], embeddings=[embedding], metadatas=[{"code": code_snippet}])

def retrieve_similar(query):
    query_embedding = model.encode(query).tolist()
    return collection.query(query_embeddings=[query_embedding], n_results=5)["metadatas"]
