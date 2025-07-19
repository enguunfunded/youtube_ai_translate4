import os
import requests
from tqdm import tqdm

# Загваруудыг хадгалах хавтас
model_dir = "./bark_model"
os.makedirs(model_dir, exist_ok=True)

# Татах шаардлагатай загвар файлууд
model_files = [
    "https://huggingface.co/suno/bark/resolve/main/config.json",
    "https://huggingface.co/suno/bark/resolve/main/preprocessor_config.json",
    "https://huggingface.co/suno/bark/resolve/main/pytorch_model.bin.index.json",
    "https://huggingface.co/suno/bark/resolve/main/pytorch_model-00001-of-00002.bin",
    "https://huggingface.co/suno/bark/resolve/main/pytorch_model-00002-of-00002.bin",
    "https://huggingface.co/suno/bark/resolve/main/tokenizer_config.json",
    "https://huggingface.co/suno/bark/resolve/main/tokenizer.json",
    "https://huggingface.co/suno/bark/resolve/main/vocab.json",
]

# Файл татах функц
def download_file(url, save_dir):
    local_filename = os.path.join(save_dir, url.split("/")[-1])
    if os.path.exists(local_filename):
        print(f"[✓] {local_filename} аль хэдийн байна.")
        return
    print(f"⬇️ Татаж байна: {local_filename}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=8192)):
                f.write(chunk)
    print(f"[✔] Хадгаллаа: {local_filename}")

# Бүх загвар файлуудыг татах
for url in model_files:
    download_file(url, model_dir)

print("\n✅ Bark модел файлууд амжилттай татагдлаа.")
