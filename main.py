
import uvicorn
from fastapi import FastAPI
from routes.routes import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "AI API Generation Agent is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
