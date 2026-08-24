from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

DEMO_MODE = True


def summarize_transcript(transcript):

    if DEMO_MODE:
        return """
### Meeting Summary

The meeting discussed the current project progress and the tasks required for the next development phase.

### Key Decisions

* The team will continue development according to the planned requirements.
* Pending issues will be reviewed before the next meeting.

### Action Items

* Complete the remaining development tasks.
* Review the implementation and prepare the next update.
"""

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