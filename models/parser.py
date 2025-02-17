import os
import ast

class CodeParser:
    def __init__(self, project_path):
        self.project_path = project_path
        self.code_structure = {"functions": [], "classes": []}

    def parse_python_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=file_path)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                self.code_structure["functions"].append(node.name)
            elif isinstance(node, ast.ClassDef):
                self.code_structure["classes"].append(node.name)

    def analyze_codebase(self):
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    self.parse_python_file(os.path.join(root, file))

        return self.code_structure
