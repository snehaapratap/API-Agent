from neo4j import GraphDatabase

# Create a driver instance
neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "apiagent"))

def store_prompt(prompt_text, repo_name):
    query = """
    CREATE (p:UserPrompt {text: $prompt_text, repo: $repo_name, timestamp: datetime()})
    RETURN p
    """
    with neo4j_driver.session() as session:
        session.run(query, prompt_text=prompt_text, repo_name=repo_name)

def retrieve_code_for_prompt(prompt_text):
    query = """
    MATCH (p:UserPrompt)-[:RELATED_TO]->(f:File)
    WHERE p.text CONTAINS $prompt_text
    RETURN f.content
    """
    with neo4j_driver.session() as session:
        result = session.run(query, prompt_text=prompt_text)
        return [record["f.content"] for record in result]
