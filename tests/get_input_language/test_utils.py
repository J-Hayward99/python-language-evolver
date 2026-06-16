from language_evolver.apps.get_input_language._utils import (
    _find_language,
    _get_lang_code,
)


def test_get_lang_code():
    assert _get_lang_code("en") == "en"
    assert _get_lang_code("en-GB") == "en-GB"
    assert _get_lang_code("english") == "en"
    assert _get_lang_code("ENGLISH") == "en"

    assert _get_lang_code("en-AA") is None
    assert _get_lang_code("aa") is None
    assert _get_lang_code(None) is None


def test_find_language():
    assert _find_language("en")
