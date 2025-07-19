from gtts import gTTS

def generate_voice(text, output_path="temp/voice.mp3", lang='mn'):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)
