from backend.transcriber import transcribe_audio

file_path = "uploads/harvard.wav"

text = transcribe_audio(file_path)

print("\nTRANSCRIPT:\n")
print(text)