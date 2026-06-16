from dataclasses import dataclass


@dataclass(slots=True)
class Language:
    language_words: list[str]
    ipa_set: set[str]
