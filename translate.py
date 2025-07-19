from deep_translator import GoogleTranslator

def translate_text(text, source="en", target="mn"):
    translated = GoogleTranslator(source=source, target=target).translate(text)
    return translated
