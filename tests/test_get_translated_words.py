from language_evolver.apps.get_translated_words import (
    _read_and_clean_english_words,
)


def test_read_english_words_file():
    assert len(_read_and_clean_english_words()) == 2_000
