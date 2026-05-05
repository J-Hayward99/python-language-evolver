# Bootstrap
import json
from pathlib import Path

# Paths
# # Base Paths
base_path = Path("src")
data_path = base_path / "data"
core_data_path = data_path / "core"

# # Core File Paths
language_codes_and_names = json.loads(
    (core_data_path / "lang_code_to_name.json").read_text(encoding="utf-8")
)
language_dialects = json.loads(
    (core_data_path / "lang_dialects_google.json").read_text(encoding="utf-8")
)

# # Output Paths
translations_path = data_path / "translations"


# Derived Files
code_dialects = set(
    [
        element
        for value in language_dialects.values()
        for element in value["dialects"]
    ]
)
codes_base_file = set(language_codes_and_names)
codes_available = codes_base_file | code_dialects

lang_names = {
    value["name"]: key for key, value in language_dialects.items()
} | {value: key for key, value in language_codes_and_names.items()}
