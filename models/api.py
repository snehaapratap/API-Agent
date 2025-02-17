import json

class APIGenerator:
    def __init__(self, api_spec_json):
        self.api_spec = json.loads(api_spec_json)

    def generate_fastapi_code(self):
        """Dynamically generates a FastAPI backend."""
        base_url = self.api_spec["base_url"]
        endpoints = self.api_spec["endpoints"]

        code = "from fastapi import FastAPI, HTTPException\n"
        code += "app = FastAPI()\n\n"

        for endpoint in endpoints:
            route = endpoint["route"]
            method = endpoint["method"]
            response = endpoint.get("response", "{}")

            if method == "GET":
                code += f"@app.get('{base_url}{route}')\ndef get_data():\n    return {response}\n\n"
            elif method == "POST":
                code += f"@app.post('{base_url}{route}')\ndef create_data(data: dict):\n    return data\n\n"

        return code

    def generate_express_code(self):
        base_url = self.api_spec["base_url"]
        endpoints = self.api_spec["endpoints"]

        code = "const express = require('express');\nconst app = express();\napp.use(express.json());\n\n"

        for endpoint in endpoints:
            route = endpoint["route"]
            method = endpoint["method"].lower()
            response = json.dumps(endpoint.get("response", "{}"))

            code += f"app.{method}('{base_url}{route}', (req, res) => {{ res.json({response}); }});\n\n"

        return code
