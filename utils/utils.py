import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def process_api_prompt(prompt):
    
    model = genai.GenerativeModel("gemini-pro")  # Use "gemini-1.5-pro" for newer models
    
    response = model.generate_content(f"Convert the following prompt into a structured API specification in JSON format:\n\n{prompt}")
    return response.text
