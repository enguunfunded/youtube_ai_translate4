import os
import numpy as np
import torch

# 🛠️ Torch Pickle алдаанаас сэргийлэх тохиргоо
torch.serialization.pickle._Unpickler.dispatch[np.core.multiarray.scalar.__reduce_ex__] = lambda self, protocol: (np.core.multiarray.scalar, ())

# Модел татах замыг локал болгож өөрчилнө
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

from bark import generate_audio, preload_models
import soundfile as sf

# Загваруудыг эхлүүлж ачаална
preload_models()

# Орчуулсан текстийг уншина
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу хоолой үүсгэнэ
audio_array = generate_audio(text)

# WAV файл болгож хадгална
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
