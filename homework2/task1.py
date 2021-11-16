"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = set()
    with open(file_path, "r", encoding="unicode-escape",
              errors="replace") as file:
        for line in file:
            # Split line in words
            line = re.split(r"\W", line)
            for word in line:
                text.add(word)
        text = list(text)
        # Count amount of every word's unique characters
        d_words = {}
        for word in text:
            d = {}
            word = word.lower()
            for char in word:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            # Count total sum of unique characters in word
            d_words[word] = sum(x for x in d.values() if x == 1)
        # Sort words in groups by amount of unique chars,
        # then sort in groups by length
        d_words = sorted(d_words.items(),
                         key=lambda x: (x[1], len(x[0]), x[0]), reverse=True)
        result = list(d_words)[:10]
    return result


def get_rarest_char(file_path: str) -> str:
    symbol_frequency = {}
    with open(file_path, "r", encoding="unicode-escape",
              errors="replace") as file:
        for line in file:
            for char in line:
                if char in symbol_frequency:
                    symbol_frequency[char] += 1
                else:
                    symbol_frequency[char] = 1
    return min(symbol_frequency,
               key=symbol_frequency.get) if symbol_frequency != {} else ''


def count_punctuation_chars(file_path: str) -> int:
    count_punc = {}
    with open(file_path, "r", encoding="unicode-escape",
              errors="replace") as file:
        for line in file:
            line = re.findall(r'\W', line)
            for char in line:
                if char in count_punc:
                    count_punc[char] += 1
                else:
                    count_punc[char] = 1
    if ' ' in count_punc:
        del(count_punc[' '])
    return sum(count_punc.values())


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii_chars = []
    with open(file_path, "r", encoding="unicode-escape",
              errors="replace") as file:
        for line in file:
            line = re.findall(r'[^\x00-\x7F]', line)
            for char in line:
                non_ascii_chars.append(char)
    return len(non_ascii_chars)


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii_chars = {}
    with open(file_path, "r", encoding="unicode-escape",
              errors="replace") as file:
        for line in file:
            line = re.findall(r'[^\x00-\x7F]', line)
            for char in line:
                if char in non_ascii_chars:
                    non_ascii_chars[char] += 1
                else:
                    non_ascii_chars[char] = 1
    return max(non_ascii_chars,
               key=non_ascii_chars.get) if non_ascii_chars != {} else ''
