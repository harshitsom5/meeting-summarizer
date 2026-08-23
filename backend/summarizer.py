from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_transcript(transcript):
    prompt = f"""
You are a meeting summarization assistant.

Analyze the following meeting transcript and return:

1. A concise meeting summary
2. Key decisions
3. Action items, including the responsible person if mentioned

Meeting Transcript:
{transcript}

Use clear headings and simple bullet points.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text