print("importing torch..")
import torch
print("importing TTS..")
from TTS.api import TTS
print("imports completed!")

# https://github.com/coqui-ai/TTS

# Installation
# https://github.com/coqui-ai/TTS?tab=readme-ov-file#installation
# pip install TTS

# Running a multi-speaker and multi-lingual model
# https://github.com/coqui-ai/TTS?tab=readme-ov-file#running-a-multi-speaker-and-multi-lingual-model

print("Starting TTS script..")

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Selected device: {device}")

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS

sample_text = "Hello world! I am an AI voice. Let's do a quick mic check - check check 1 2 3. The quick brown fox jumps over the lazy dog. What do you think?"

# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language

# Text to speech list of amplitude values as output
# wav = tts.tts(text=sample_text, speaker_wav="./example_1.wav", language="en")

# Text to speech to a file
tts.tts_to_file(text=sample_text, speaker_wav="./speech1.mp3", language="en", file_path="coqui_output.wav")

print("Voice sample successfully generated!")