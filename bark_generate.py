from bark import generate_audio, preload_models
import soundfile as sf

# Загваруудыг ачааллах (анх удаа бол удаж болно)
preload_models()

# Орчуулагдсан текст (монголоор бичнэ)
text = """
Кристиано Роналдо энэ тоглолтонд шилдэг гоолуудыг хийсэн юм. Тэр бол домог.
"""

# Аудио гаргах
audio_array = generate_audio(text)

# MP3 файл болгож хадгалах
sf.write("temp/voice_bark.wav", audio_array, 24000)
print("🎧 Bark дуу хоолой voice_bark.wav файлд хадгалагдлаа.")
