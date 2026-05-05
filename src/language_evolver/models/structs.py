from language_evolver.constants import (
    language_codes_and_names,
    language_dialects,
)


class InputLanguage:
    lang_full: str

    lang_core: str
    dialect: str | None

    has_dialect: bool
    gtrans_use_dialect: bool

    def __init__(self, lang: str):
        # Full Language
        self.lang_full = lang

        # Core Language
        lang_comp = self.lang_full.split("-")
        self.lang_core = lang_comp[0]

        # Dialect
        self.has_dialect = len(lang_comp) == 2
        self.dialect = lang_comp[1] if self.has_dialect else None

        # Google Translate
        self.gtrans_use_dialect = (
            self.has_dialect and self.lang_full in language_codes_and_names
        )

    @property
    def can_be_translated(self) -> bool:
        # If Language in Base Sheet
        if self.lang_full in language_codes_and_names:
            return True

        # If Has Dialect
        # NOTE: Languages can have dialects (e.g., "en-GB") but Google only has
        #       lang (e.g., "en") available.
        dialect_entry = language_dialects.get(self.lang_core)
        if (
            self.has_dialect
            and dialect_entry
            and self.lang_full in dialect_entry["dialects"]
        ):
            return True

        return False

    def get_google_code(self):
        return self.lang_full if self.gtrans_use_dialect else self.lang_core

    def print_info(self):
        print("Found")
