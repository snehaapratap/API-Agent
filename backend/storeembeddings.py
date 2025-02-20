from graphstore import db
from embeddings import store_embedding

def store_code_embeddings():
    with db.driver.session() as session:
        result = session.run("MATCH (fn:Function) RETURN fn.name AS name, fn.code AS code")
        for record in result:
            store_embedding(record["code"], record["name"])

store_code_embeddings()
print("Embeddings stored in ChromaDB!")
