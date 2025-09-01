import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_ai_plan(mission: str) -> str:
    """
    Connects to the Gemini API, sends a mission, and returns a step-by-step plan.

    Args:
        mission: The natural language mission for the AI.

    Returns:
        The AI's step-by-step plan as a single string.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Create a step-by-step plan for the following mission: {mission}")
        return response.text
    except Exception as e:
        print(f"An error occurred while connecting to the Gemini API: {e}")
        return ""
