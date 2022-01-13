"""
Write a function that takes directory path, a file
extension and an optional tokenizer. It will count lines
 in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:

"""
import glob
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    def _open_every_file_in_dir():
        for filename in glob.glob(
                os.path.join(dir_path, f'*.{file_extension}')):
            with open(os.path.join(os.getcwd(), filename), 'r') as file:
                for line in file:
                    yield line

    if not os.path.exists(dir_path):
        raise ValueError(f"Filepath {dir_path} doesn't exist!")

    if tokenizer is None:
        count_lines_without_token = sum(1 for _ in _open_every_file_in_dir())
        return count_lines_without_token

    number_of_tokens = 0
    for line_from_file in _open_every_file_in_dir():
        tokens = tokenizer(line_from_file)
        number_of_tokens += len(tokens)

    return number_of_tokens
