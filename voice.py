import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def speak(text):

    audio = client.text_to_speech.convert(

        voice_id="JBFqnCBsd6RMkjVDRZzb",

        model_id="eleven_multilingual_v2",

        text=text

    )

    output = "response.mp3"

    with open(output, "wb") as f:

        for chunk in audio:

            f.write(chunk)

    return output