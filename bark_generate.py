import os
import numpy as np
import torch
import torch.serialization

# Torch Pickle алдаанаас сэргийлэх глобал зөвшөөрөл
torch.serialization._default_restore_location = lambda storage, location: storage
torch.serialization.register_package('numpy.core.multiarray')
torch.serialization.pickle._Unpickler.dispatch[np.core.multiarray.scalar.__reduce_ex__] = lambda self, protocol: (np.core.multiarray.scalar, ())

# Загвар татах зам
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

from bark import generate_audio, preload_models
import soundfile as sf

# Загваруудыг ачаалах
preload_models()

# Орчуулсан текст унших
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу үүсгэх
audio_array = generate_audio(text)

# WAV файл болгон хадгалах
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
