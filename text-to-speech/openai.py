from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

lines = [
    "Welcome.",
    "This video will guide you through using the command line interface.",
    "The `help` command will give you an overview of all available commands.",
    "Enter `help <command name>` for command-specific information.",
]

for i in range(len(lines)):
    filename = "speech" + str(i) + ".mp3"
    speech_file_path = Path(__file__).parent / filename
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=lines[i]
    )

    with open(speech_file_path, "wb") as f:
        for chunk in response.iter_bytes(chunk_size=8192):
            f.write(chunk)