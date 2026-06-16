from language_evolver.apps.get_input_language.get_input_language import (
    get_inputted_language,
)
from language_evolver.apps.ipa_converter.get_ipa_words import (
    convert_text_to_ipa,
)
from language_evolver.apps.language_translater.get_translated_words import (
    translate_words,
)


def main(inputted_languages: list[str] | str | None = None):
    print("=== Language Evolver ===")

    if not isinstance(inputted_languages, list):
        processed_lang = [inputted_languages]
    else:
        processed_lang = inputted_languages

    for lang in processed_lang:
        # Ask for Language
        structed_input_lang = get_inputted_language(lang)
        google_code = structed_input_lang.google_code()
        print()

        # Get Language Translations
        translate_words(google_code)
        print()

        # Get Language IPA
        convert_text_to_ipa(google_code)
        print()


def main_multiple():
    list_of_languages = [
        "english",
        "czech",
        "german",
        "french",
        "welsh",
        "hungarian",
        "mandarin",
        "arabic",
        "danish",
        "italian",
        "turkish",
        "russian",
        "polish",
        "irish",
    ]
    list_of_langs = sorted(list_of_languages)
    main(list_of_langs)


if __name__ == "__main__":
    # main("en")
    main_multiple()
