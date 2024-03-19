import json
from .Language import Language

class Translator:
    def __init__(self, config_file):
        self.languages = {}
        self.load_languages(config_file)

    def load_languages(self, config_file):
        with open(config_file, 'r') as file:
            data = json.load(file)
            for lang_data in data:
                lang = Language(lang_data['name'], lang_data['greeting_morning'], lang_data['greeting_evening'], lang_data['goodbye'], lang_data['palindrome_response'], lang_data['enter_text_prompt'], lang_data['exit_word'], lang_data['mirrored_text'])
                self.languages[lang.name.lower()] = lang

    def get_language(self, lang_name):
        return self.languages.get(lang_name.lower())