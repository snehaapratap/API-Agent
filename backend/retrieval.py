from embeddings import retrieve_similar
from graphstore import db

def retrieve_code_context(prompt):
    similar_codes = retrieve_similar(prompt)
    related_code = []
    
    for code in similar_codes:
        with db.driver.session() as session:
            result = session.run("MATCH (fn:Function {code: $code})-[:CONTAINS]-(f:File) RETURN f.content", code=code['code'])
            for record in result:
                related_code.append(record["f.content"])
    
    return related_code
