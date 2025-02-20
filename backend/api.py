from fastapi import FastAPI
from retrieval import retrieve_code_context
from llm import generate_code

app = FastAPI()

@app.get("/generate_api/")
def generate_api(prompt: str):
    code_context = retrieve_code_context(prompt)
    new_code = generate_code("\n".join(code_context) + f"\n\n# Generate an API for {prompt}")
    return {"api_code": new_code}
