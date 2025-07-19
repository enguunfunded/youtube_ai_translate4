def create_srt(text, output_path="temp/subtitles.srt"):
    lines = text.split('. ')
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, line in enumerate(lines):
            start = f"00:00:{i*4:02},000"
            end = f"00:00:{(i+1)*4:02},000"
            f.write(f"{i+1}\n{start} --> {end}\n{line.strip()}\n\n")
