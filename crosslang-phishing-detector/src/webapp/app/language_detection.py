from langdetect import detect as langdetect_detect

def detect_language(text):
    """
    Detect the language of the given text using langdetect.
    Returns the ISO 639-1 language code (e.g., 'en', 'fr', 'de').
    """
    try:
        lang_code = langdetect_detect(text)
        return lang_code
    except Exception as e:
        print(f"[DEBUG] langdetect error: {e}")
        return 'en'  # Fallback to English