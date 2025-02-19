import os
import ast
from graphstore import db

CODEBASE_DIR = "data/codebase"

def extract_functions(file_path, content):
    tree = ast.parse(content)
    return [(node.name, ast.unparse(node)) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def store_codebase():
    for root, _, files in os.walk(CODEBASE_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                db.store_code_file(file_path, content)
                for function_name, function_code in extract_functions(file_path, content):
                    db.store_function(file_path, function_name, function_code)

store_codebase()
print("Codebase stored in Neo4j!")
