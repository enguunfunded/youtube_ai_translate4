import os
import requests
from tqdm import tqdm

model_dir = "./bark_model"
os.makedirs(model_dir, exist_ok=True)

model_files = [
    "https://huggingface.co/suno/bark-small/resolve/main/config.json",
    "https://huggingface.co/suno/bark-small/resolve/main/pytorch_model.bin",
    "https://huggingface.co/suno/bark-small/resolve/main/tokenizer.json",
    "https://huggingface.co/suno/bark-small/resolve/main/tokenizer_config.json",
    "https://huggingface.co/suno/bark-small/resolve/main/preprocessor_config.json",
    "https://huggingface.co/suno/bark-small/resolve/main/vocab.json"
]

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

for url in model_files:
    download_file(url, model_dir)

print("\n✅ bark_model хавтас bark-small модел ашиглан амжилттай бүрдлээ.")
