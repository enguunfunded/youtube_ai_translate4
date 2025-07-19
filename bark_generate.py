import os
import torch
import numpy as np
import soundfile as sf
from bark import generate_audio, preload_models

# Torch model cache замууд
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

# Torch pickle ачаалалтад зөвшөөрөгдөөгүй global-ууд whitelist хийх
try:
    torch.serialization._open_file = torch.serialization._open_file  # for compatibility
    torch.serialization.pickle._Unpickler = torch._utils._import_dotted_name(
        "torch.serialization._open_file_like"
    )
    torch.serialization._legacy_load = lambda f, *args, **kwargs: torch.load(
        f, *args, weights_only=False, **kwargs
    )
    torch.serialization.set_safe_globals({
        "numpy.core.multiarray.scalar": np.core.multiarray.scalar
    })
except Exception:
    pass  # Torch хувилбараас хамаарч өөр байх боломжтой

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
