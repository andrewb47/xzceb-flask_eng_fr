from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    this function accepts an text in English and returns a translation in French
    """

    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)

    return french_text

def french_to_english(french_text):
    """
    this function accepts an text in French and returns a translation in English
    """

    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)

    return english_text
