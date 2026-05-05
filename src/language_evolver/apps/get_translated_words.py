import asyncio
import csv

from googletrans import Translator
from tqdm import tqdm

from language_evolver.constants import (
    core_data_path,
    translations_path,
    language_codes_and_names,
)


def _read_and_clean_english_words(
    english_words_path: str = "english_words.txt",
) -> set[str]:
    # Get File Path
    english_words_file = core_data_path / english_words_path

    # Get File Contents
    english_words = english_words_file.read_text(encoding="utf-8")
    cleaned_words = english_words.replace(",", " ").split()

    # Get List of Words
    list_of_words = [word.strip() for word in cleaned_words]

    return set(list_of_words)


async def _get_translations(
    english_words: set[str],
    language_code: str,
    language_name: str,
) -> dict[str, str]:
    # Bootstrap
    translator = Translator()
    translation: dict[str, str] = {}

    # Translate with Progress Bar
    with tqdm(
        total=len(english_words),
        desc=f"- Translating: {language_name}",
        unit="word",
    ) as progress_bar:
        # Iterate List of English Words
        for word in english_words:
            # NOTE: Google Translate is Async
            result = await translator.translate(
                word,
                src="en",
                dest=language_code,
            )

            translation[word] = result.text
            progress_bar.update(1)

    return translation


def _save_language_translations(
    language_code: str,
    data: dict[str, str],
) -> None:
    # Pathing
    file_name = f"{language_code}.csv"
    file_path = translations_path / file_name

    # Cache Stuff
    if file_path.exists():
        return None

    # Make Folder
    if not translations_path.exists():
        translations_path.mkdir(parents=True)

    # Sort Data Alphabetically (English)
    sorted_data = dict(sorted(data.items(), key=lambda item: item[0]))

    # Write File
    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["english", "translation"])  # header
        writer.writerows(sorted_data.items())

    # Print Saved
    print(f"- Saved data to {file_path}")


def translate_words(lang_code: str) -> None:
    # Function Start Message & Bootstrapping
    lang_name = language_codes_and_names[lang_code]
    print(f"Translating EN (English) into {lang_code.upper()} ({lang_name}).")

    # Check for Existing Save File & Skip
    output_file_path = translations_path / f"{lang_code}.csv"
    if output_file_path.exists():
        print(f"- {lang_code}.csv already exists... Skipping")
        return None

    # Get English Words
    english_words = _read_and_clean_english_words()
    number_of_words = len(english_words)
    msg = f"- Translating {number_of_words:,} English words into {lang_name}"
    print(msg)

    # Translate Words into Language
    translated_words = asyncio.run(
        _get_translations(
            english_words,
            language_code=lang_code,
            language_name=lang_name,
        )
    )
    print("- Translated Words")

    # Save Data
    _save_language_translations(lang_code, translated_words)
