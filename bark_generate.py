import os
import torch
import numpy as np
import soundfile as sf
from bark import generate_audio, preload_models

# Torch model cache замууд
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

# Torch pickle ачаалалтад зөвшөөрөгдөөгүй global-уудыг whitelist хийх
try:
    torch.serialization._internal_torch_pickler._allowed_globals.add("numpy.core.multiarray.scalar")
except Exception:
    pass  # Torch хувилбараас хамаарч өөр байж болно

# Загвар ачаалах
preload_models()

# Орчуулсан текст унших
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу үүсгэх
audio_array = generate_audio(text)

# WAV файл хадгалах
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
