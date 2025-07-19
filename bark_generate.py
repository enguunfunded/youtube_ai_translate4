import os
import torch
import numpy as np
import soundfile as sf
from bark import generate_audio, preload_models

# Torch model зам
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

# Unsupported pickle global зөвшөөрөх
torch.serialization._legacy_load = torch._legacy_load
torch.serialization.register_package("numpy.core.multiarray")
torch.serialization.pickle = torch.serialization.pickle if hasattr(torch.serialization, 'pickle') else __import__('pickle')

# Загваруудыг ачаалах
preload_models()

# Орчуулсан текст унших
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу үүсгэх
audio_array = generate_audio(text)

# WAV файл болгох
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
