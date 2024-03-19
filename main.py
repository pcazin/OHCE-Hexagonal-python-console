import datetime
import json
from app_class.Translator import Translator
from app_class.MirrorApp import MirrorApp

def main():
    translator = Translator('languages.json')
    lang = input("Choose a language (English/French): ").lower()
    app = MirrorApp(translator)
    app.run(lang)

if __name__ == "__main__":
    main()
