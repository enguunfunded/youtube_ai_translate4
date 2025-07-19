import os
import torch
import numpy as np
import soundfile as sf
from bark import generate_audio, preload_models
from numpy.core.multiarray import scalar  # ✅ Зөв обьектоор оруулж байна

# Torch model cache замууд
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

# Torch pickle whitelist тохиргоо
try:
    torch.serialization.add_safe_globals({'numpy.core.multiarray.scalar': scalar})
except Exception as e:
    print("⚠️ Torch whitelist тохиргоо амжилтгүй:", e)

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
