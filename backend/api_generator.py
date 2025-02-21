import requests

GROQ_API_KEY = "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"

def generate_api(prompt, related_code):
    response = requests.post(
        "https://api.groq.com/generate",
        json={"prompt": f"Generate an API for {prompt} using:\n{related_code}"},
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"}
    )
    return response.json()["text"]
