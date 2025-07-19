import os
os.environ["XDG_CACHE_HOME"] = "./bark_model"
os.environ["HF_HOME"] = "./bark_model"
os.environ["TORCH_HOME"] = "./bark_model"

from bark import generate_audio, preload_models
import soundfile as sf

# Загваруудыг ачаалах
preload_models()

# Орчуулсан текстийг унших
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу хоолой үүсгэх
audio_array = generate_audio(text)

# WAV файл болгон хадгалах
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
