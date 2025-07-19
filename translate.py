from deep_translator import GoogleTranslator

def split_text(text, max_chars=5000):
    parts = []
    while len(text) > max_chars:
        split_at = text.rfind('. ', 0, max_chars)
        if split_at == -1:
            split_at = max_chars
        parts.append(text[:split_at+1].strip())
        text = text[split_at+1:].strip()
    parts.append(text)
    return parts

def translate_text(text, source="en", target="mn"):
    chunks = split_text(text)
    translated = ""
    for chunk in chunks:
        translated += GoogleTranslator(source=source, target=target).translate(chunk) + " "
    return translated.strip()
