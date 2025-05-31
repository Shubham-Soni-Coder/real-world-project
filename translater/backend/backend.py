# backend.py
import googletrans

class TranslatorBackend:
    def __init__(self):
        self.translator = googletrans.Translator()
        self.name_to_code, self.language_names = self.get_language_mappings()

    def get_language_mappings(self):
        """Returns a mapping of full language names to codes and a sorted list of names."""
        languages = googletrans.LANGUAGES
        name_to_code = {name.title(): code for code, name in languages.items()}
        language_names = sorted(name_to_code.keys())
        return name_to_code, language_names

    def translate_text(self, text, language_name):
        """Translates the given text to the selected language."""
        lang_code = self.name_to_code.get(language_name, 'hi')
        try:
            translation = self.translator.translate(text, dest=lang_code)
            return translation.text
        except Exception:
            return ""

if __name__=='__main__':
    result = TranslatorBackend()
    print(result.translate_text("My name is shubham soni",'Hindi'))