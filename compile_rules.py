"""Compile all the YARA rules into a single binary file."""
import os
from typing import Generator
import yara

RULES_DIR = ""


def get_rules_dir():
    RULES_DIR = str(os.path.dirname(os.path.realpath(__file__))) + "\public"
    return os.listdir(RULES_DIR)


def _find_yara_files() -> Generator[str, None, None]:
    for root, _, files in os.walk(RULES_DIR):
        for filename in files:
            lower_filename = filename.lower()
            if lower_filename.endswith('.yar') or lower_filename.endswith('.yara'):
                yield os.path.relpath(os.path.join(root, filename), start=RULES_DIR)


def compile_rules() -> None:
    global RULES_DIR
    for dir in get_rules_dir():
        if ".yara" in str(dir):
            pass
        else:
            print(str(os.path.dirname(os.path.realpath(__file__))) + "\public\\" + str(dir))
            RULES_DIR = str(os.path.dirname(os.path.realpath(__file__))) + "\public\\" + str(dir)

            yara_filepaths = {relative_path: os.path.join(RULES_DIR, relative_path)
                                for relative_path in _find_yara_files()}

            rules = yara.compile(
                filepaths=yara_filepaths,
                externals={'extension': '', 'filename': '', 'filepath': '', 'filetype': ''}
            )

            rules.save(str(dir) + ".bin")


# compile_rules()
