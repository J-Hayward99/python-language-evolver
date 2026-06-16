from dataclasses import dataclass, field

from language_evolver.constants import (
    language_codes_and_names,
    language_dialects,
)


@dataclass(slots=True)
class InputLanguage:
    """
    This dataclass is used to handle the input language in a way that
    supports and extracts the information from the language codes. Primarily to
    handle how dialects are processed.

    Examples:
        -   `en`
        -   `fr`
        -   `en-GB`

    Args:
        language_full_code (str): Full language code such as `en` or `en-GB`.
    """

    # Input Code
    language_full_code: str

    # Components
    main_code: str = field(init=False)
    dialect_code: str | None = field(init=False)

    has_dialect: bool = field(init=False)
    gtrans_use_dialect: bool = field(init=False)

    def __post_init__(self) -> None:

        if not self.language_full_code:
            raise ValueError("Language code cannot be empty")

        lang_core, sep, dialect = self.language_full_code.partition("-")
        has_dialect = bool(sep)

        self.main_code = lang_core
        self.has_dialect = has_dialect
        self.dialect_code = dialect or None
        self.gtrans_use_dialect = (
            has_dialect and self.language_full_code in language_codes_and_names
        )

    @property
    def can_be_translated(self) -> bool:
        if self.language_full_code in language_codes_and_names:
            return True

        if not self.has_dialect:
            return False

        dialect_entry = language_dialects.get(self.main_code)
        dialects = dialect_entry.get("dialects", []) if dialect_entry else []

        return self.language_full_code in dialects

    @property
    def google_code(self) -> str:

        return (
            self.language_full_code
            if self.gtrans_use_dialect
            else self.main_code
        )
