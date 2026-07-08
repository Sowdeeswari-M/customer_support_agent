from faster_whisper import WhisperModel

print("Loading Faster Whisper...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Faster Whisper loaded!")

def speech_to_text(audio_path):
    segments, info = model.transcribe(
        audio_path,
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()