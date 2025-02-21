from fastapi import FastAPI, Request
from backend.git_clone import clone_repo
from backend.graph_db import store_prompt, retrieve_code_for_prompt
from backend.api_generator import generate_api

app = FastAPI()

@app.post("/clone_repo")
async def clone_repo_endpoint(request: Request):
    data = await request.json()
    github_url = data["github_url"]
    clone_repo(github_url)
    return {"message": "Repo cloned and stored in Neo4j"}

@app.post("/generate_api")
async def generate_api_endpoint(request: Request):
    data = await request.json()
    prompt_text = data["prompt"]
    store_prompt(prompt_text, "sample_repo")  
    related_code = retrieve_code_for_prompt(prompt_text)
    api_code = generate_api(prompt_text, related_code)
    return {"api_code": api_code}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
