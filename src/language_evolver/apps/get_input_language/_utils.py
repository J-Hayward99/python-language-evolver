from ._models import InputLanguage
from language_evolver.constants import codes_available, lang_names


def _get_lang_code(lang: str | None) -> str | None:
    if lang is None:
        return None

    bool_already_code = lang in codes_available
    bool_need_to_convert = lang.title() in lang_names

    if bool_already_code:
        return lang

    if bool_need_to_convert:
        return lang_names[lang.title()]

    return None


def _find_language(language: str | None) -> InputLanguage | None:
    # Convert Language to Code if Needed
    language = _get_lang_code(language)

    # Check if Language is None
    if language is None:
        return None

    struct_lang = InputLanguage(lang=language)

    if struct_lang.can_be_translated is False:
        return None

    return struct_lang
