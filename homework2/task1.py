"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import string
import unicodedata
from typing import List


class Token:

    def __init__(self, value):
        self.value = value


def tokenize(file_content):
    word_buffer = ''
    for line in file_content:
        for symbol in line:
            if unicodedata.category(symbol)[0] == 'L':
                word_buffer += symbol
            else:
                if word_buffer:
                    yield Token(value=word_buffer)
                    word_buffer = ''


def open_file(file_path: str, encoding="UTF-8", errors="replace"):
    with open(file_path, encoding=encoding, errors=errors) as fi:
        for line in fi:
            yield line


def get_longest_diverse_words(file_path: str) -> List[str]:
    d_words = {}
    for token in tokenize(open_file(file_path, encoding="unicode-escape")):
        # Count amount of every word's unique characters
        d_chars = {}
        for char in token.value.lower():
            if char in d_chars:
                d_chars[char] += 1
            else:
                d_chars[char] = 1

        # Count total sum of unique characters in word
        d_words[token.value] = len([x for x in d_chars.values() if x == 1])

    # Sort words in groups by amount of unique chars,
    # then sort in groups by length
    d_words = sorted(d_words.items(),
                     key=lambda x: (x[1], len(x[0]), x[0]),
                     reverse=True)
    result = list(d_words)[:10]
    return result


def get_rarest_char(file_path: str) -> str:
    symbol_frequency = {}
    for line in open_file(file_path, encoding="unicode-escape"):
        for char in line:
            if char in symbol_frequency:
                symbol_frequency[char] += 1
            else:
                symbol_frequency[char] = 1
    return min(symbol_frequency,
               key=symbol_frequency.get) if symbol_frequency != {} else ''


def count_punctuation_chars(file_path: str) -> int:
    punctuation_chars = set(string.punctuation)
    count_punc = 0
    for line in open_file(file_path, encoding="unicode-escape"):
        for char in line:
            if char in punctuation_chars:
                count_punc += 1
    return count_punc


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii_chars = []
    for line in open_file(file_path, encoding="unicode-escape"):
        non_ascii_chars.extend(re.findall(r'[^\x00-\x7F]', line))
    return len(non_ascii_chars)


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii_chars = {}
    for line in open_file(file_path, encoding="unicode-escape"):
        string_of_chars = re.findall(r'[^\x00-\x7F]', line)
        for char in string_of_chars:
            if char in non_ascii_chars:
                non_ascii_chars[char] += 1
            else:
                non_ascii_chars[char] = 1
    return max(non_ascii_chars,
               key=non_ascii_chars.get) if non_ascii_chars != {} else ''
