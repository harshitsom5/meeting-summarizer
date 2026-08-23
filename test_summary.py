from backend.summarizer import summarize_transcript

transcript = """
Today we discussed the meeting summarizer project.
Harshit will complete the backend API by Friday.
Rahul will prepare the frontend interface.
The team decided to use Whisper for speech transcription.
"""

summary = summarize_transcript(transcript)

print("\nSUMMARY:\n")
print(summary)