import requests

GROQ_API_URL = "https://api.groq.com/v1/completions"
GROQ_API_KEY = "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"

def generate_code(prompt):
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "codellama-7b", "prompt": prompt, "max_tokens": 200}
    
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("text", "").strip()
