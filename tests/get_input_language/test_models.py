from language_evolver.apps.get_input_language._models import InputLanguage

import pytest


def test_input_language_methods_language():
    # Check Methods without Dialect
    struct = InputLanguage("en")
    assert struct.language_full_code == "en"
    assert struct.main_code == "en"
    assert struct.dialect_code is None
    assert struct.has_dialect is False
    assert struct.gtrans_use_dialect is False
    assert struct.can_be_translated is True


def test_input_language_methods_dialect():
    struct_with_dialect = InputLanguage("en-GB")
    assert struct_with_dialect.language_full_code == "en-GB"
    assert struct_with_dialect.main_code == "en"
    assert struct_with_dialect.dialect_code == "GB"
    assert struct_with_dialect.has_dialect is True
    assert struct_with_dialect.gtrans_use_dialect is False
    assert struct_with_dialect.can_be_translated is True


@pytest.mark.parametrize(
    "language",
    [
        "en",
        "en-GB",
    ],
)
def test_input_language_handle_good_languages(language):
    struct = InputLanguage(language)

    assert struct.can_be_translated


@pytest.mark.parametrize(
    "language",
    [
        # Outright Bad Values
        "aa",
        "aa-AA",
        # Just Bad Dialect
        "en-AA",
        # Just Bad Language
        "aa-GB",
    ],
)
def test_input_language_handle_bad_languages(language):
    struct = InputLanguage(language)

    assert not struct.can_be_translated
