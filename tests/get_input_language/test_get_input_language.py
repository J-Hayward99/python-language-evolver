from language_evolver.apps.get_input_language.get_input_language import (
    get_inputted_language,
)


def test_get_inputted_language():
    assert get_inputted_language("en")
