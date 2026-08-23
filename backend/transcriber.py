from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")


def transcribe_audio(file_path):
    segments, info = model.transcribe(file_path)

    transcript = []

    for segment in segments:
        transcript.append(segment.text.strip())

    return " ".join(transcript)