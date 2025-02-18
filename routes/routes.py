from fastapi import APIRouter
from models.api import APIGenerator
from utils.utils import process_api_prompt

router = APIRouter()

@router.post("/generate_api")
def generate_api(prompt: str, framework: str = "fastapi"):
    api_json = process_api_prompt(prompt)
    generator = APIGenerator(api_json)

    if framework.lower() == "fastapi":
        return {"code": generator.generate_fastapi_code()}
    elif framework.lower() == "express":
        return {"code": generator.generate_express_code()}
    else:
        return {"error": "Unsupported framework"}
