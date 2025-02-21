import chromadb

chroma_client = chromadb.PersistentClient(path="chroma_db/")
collection = chroma_client.get_or_create_collection("codebase")

def store_code_embedding(file_path, content):
    collection.add(documents=[content], metadatas={"file": file_path}, ids=[file_path])

def query_similar_code(query_text):
    results = collection.query(query_texts=[query_text], n_results=3)
    return results["documents"]
