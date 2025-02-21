import os
import git
import neo4j
from neo4j import GraphDatabase

class GraphDB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_file(self, repo_name, file_path, content):
        query = """
        MERGE (f:File {repo: $repo_name, path: $file_path})
        SET f.content = $content
        """
        with self.driver.session() as session:
            session.run(query, repo_name=repo_name, file_path=file_path, content=content)

def clone_repo(github_url, db):
    repo_name = github_url.split("/")[-1].replace(".git", "")
    repo_path = f"cloned_repos/{repo_name}"
    if not os.path.exists(repo_path):
        git.Repo.clone_from(github_url, repo_path)

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py") or file.endswith(".js"):  
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    db.add_file(repo_name, file_path, content)

if __name__ == "__main__":
    neo4j_db = GraphDB("bolt://localhost:7687", "neo4j", "apiagent")
    github_url = "https://github.com/snehaapratap/To-Do-List-App.git"
    clone_repo(github_url, neo4j_db)
    neo4j_db.close()
