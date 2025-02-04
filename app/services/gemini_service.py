import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from flask import current_app

class GeminiService:
    def __init__(self):
        genai.configure(api_key=current_app.config["API_KEY"])

    def generate_response(self, user_prompt="hello"):
        user_prompt = user_prompt.lower()

        # Basic conversational logic
        if "hello" in user_prompt or "hi" in user_prompt:
            return "Hello! How can I assist you today?"

        elif "how are you" in user_prompt:
            return "I'm doing great, thanks for asking! How about you?"

        elif "bye" in user_prompt:
            return "Goodbye! Have a great day!"

        # You can add more conversational conditions here
        else:
            return self.generate_content(user_prompt)

    def generate_content(self, prompt):
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-exp")
            response = model.generate_content(prompt)
            if response and response.text:
                return f"{response.text.strip()}"
            return "Sorry, I couldn't generate a response. Please try again."
        except Exception as e:
            return f"Oops! I ran into an issue while generating the response. Error: {str(e)}"
