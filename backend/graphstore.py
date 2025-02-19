from neo4j import GraphDatabase

class GraphDB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def store_code_file(self, file_path, content):
        with self.driver.session() as session:
            session.run("MERGE (f:File {path: $path, content: $content})", path=file_path, content=content)

    def store_function(self, file_path, function_name, function_code):
        with self.driver.session() as session:
            session.run("""
                MATCH (f:File {path: $file_path})
                MERGE (fn:Function {name: $function_name, code: $function_code})
                MERGE (f)-[:CONTAINS]->(fn)
            """, file_path=file_path, function_name=function_name, function_code=function_code)

db = GraphDB("bolt://localhost:7687", "neo4j", "password")
