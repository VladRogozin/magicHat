import deepl

def translation(word):
    auth_key = "9f177660-4b25-458a-8734-50dcfc539572:fx"  # Replace with your key
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(text=word, source_lang="DE", target_lang="RU")
    return (result.text)