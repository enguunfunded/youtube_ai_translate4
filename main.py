from yt_downloader import download_youtube_video
from transcribe import transcribe_audio
from translate import translate_text
from voiceover import generate_voice
from subtitle import create_srt
from merge_video import merge_all
import os

def main():
    url = input("YouTube линк оруулна уу: ")

    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    print("1. Видео татаж байна...")
    download_youtube_video(url)

    print("2. Аудио-г текст рүү хөрвүүлж байна...")
    english_text = transcribe_audio()

    print("3. Орчуулж байна...")
    mongolian_text = translate_text(english_text)

    print("4. Дуу хоолой үүсгэж байна...")
    generate_voice(mongolian_text)

    print("5. Subtitle үүсгэж байна...")
    create_srt(mongolian_text)

    print("6. Видео руу буцааж нэгтгэж байна...")
    merge_all()

    print("✅ Амжилттай! 'output/final_video.mp4' файлд хадгалагдлаа.")

if __name__ == "__main__":
    main()
