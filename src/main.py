from language_evolver.apps.get_input_language import get_inputted_language
from language_evolver.apps.get_translated_words import translate_words


def main(inputted_language: str | None = None):
    print("=== Language Evolver ===")

    # Ask for Language
    structed_input_lang = get_inputted_language(inputted_language)
    print()

    # Get Language Translations
    translate_words(structed_input_lang.get_google_code())
    print()

    # # Get Language IPA
    # translate_words(structed_input_lang.get_google_code())
    # print()


if __name__ == "__main__":
    main("en")
