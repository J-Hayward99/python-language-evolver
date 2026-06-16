import pandas as pd
from phonemizer import phonemize
from language_evolver.constants import (
    translations_path,
    code_to_espeak,
    phonetics_path,
)


def _make_text_phonetic(pddf: pd.DataFrame, lang: str) -> pd.DataFrame:
    language_words = pddf["translation"].to_list()

    try:
        list_of_ipa = phonemize(
            text=language_words,
            language=code_to_espeak[lang],
        )
    except RuntimeError as e:
        code_change_error = (
            f'language "{lang}" is not supported by the espeak backend'
        )

        if not str(e).startswith(code_change_error):
            raise RuntimeError(e)

        new_lang = f"{lang}-{lang.upper()}"
        msg = f"*{lang} wasn't found in codes, trying {new_lang} due to common error*"
        print(msg)
        list_of_ipa = phonemize(
            text=language_words,
            language=code_to_espeak[new_lang],
        )

    pddf["ipa"] = list_of_ipa
    return pddf


def _save_file(pddf: pd.DataFrame, lang: str) -> None:
    file_name = f"{lang}.csv"
    file_path = phonetics_path / file_name

    if not phonetics_path.exists():
        phonetics_path.mkdir(parents=True)

    pddf.to_csv(str(file_path), index=False)


def convert_text_to_ipa(lang: str) -> None:
    # Get Translations as Pandas DataFrame
    pddf_translations = pd.read_csv(f"{translations_path / lang}.csv")

    pddf_phonetic = _make_text_phonetic(pddf_translations, lang)

    _save_file(pddf_phonetic, lang)
