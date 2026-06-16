from ._models import InputLanguage

from ._utils import _find_language


def get_inputted_language(inputted_language: str | None) -> InputLanguage:
    # Edge Cases
    if (
        inputted_language is not None
        and inputted_language.lower() == "mandarin"
    ):
        inputted_language = "Chinese (Simplified)"

    initial_language = inputted_language
    prompt = "What language code do you want to use? "
    while True:
        if inputted_language is None:
            inputted_language = input(prompt)

        tested_language = _find_language(inputted_language)

        if initial_language is not None and tested_language is None:
            msg = f'Language "{inputted_language}" cannot be translated'
            raise ValueError(msg)

        if tested_language is not None:
            return tested_language

        print(f"The language {inputted_language} doesn't exist, try again.")
        print()
        inputted_language = input(prompt)
