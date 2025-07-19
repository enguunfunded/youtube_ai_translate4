import yt_dlp
import os

def download_youtube_video(url, output_path="temp/input.mp4"):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': output_path,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
