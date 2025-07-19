from bark import generate_audio, preload_models
import soundfile as sf

# Загваруудыг ачааллах
preload_models()

# Орчуулагдсан текстийг унших
with open("temp/translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Дуу хоолой үүсгэх
audio_array = generate_audio(text)

# WAV файл болгон хадгалах
sf.write("temp/voice_bark.wav", audio_array, 24000)

print("✅ voice_bark.wav файл амжилттай үүсгэгдлээ.")
