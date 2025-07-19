import whisper

def transcribe_audio(input_video="temp/input.mp4"):
    model = whisper.load_model("base")
    result = model.transcribe(input_video)
    return result['text']
