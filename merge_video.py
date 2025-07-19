import ffmpeg
import os

def merge_all(video_path="temp/input.mp4", audio_path="temp/voice.mp3", subtitle_path="temp/subtitles.srt", output_path="output/final_video.mp4"):
    ffmpeg.input(video_path).output("temp/video_no_audio.mp4", an=None).run(overwrite_output=True)
    
    ffmpeg.output(
        ffmpeg.input("temp/video_no_audio.mp4"),
        ffmpeg.input(audio_path),
        output_path,
        vf=f"subtitles={subtitle_path}"
    ).run(overwrite_output=True)
