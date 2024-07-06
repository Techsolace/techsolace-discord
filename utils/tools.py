import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

async def generate_from_prompt(prompt: str):
    response = model.generate_content(prompt)
    return response