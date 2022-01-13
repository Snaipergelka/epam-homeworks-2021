"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest
from typing import Generator


def process_backspaces(m_string: str) -> Generator:
    # how many chars to skip, skip is equal to delete
    skip = 0

    for m_char in reversed(m_string):
        if m_char == "#":
            skip += 1
        else:
            # it is true when we processed all backspaces
            if skip == 0:
                yield m_char
            else:
                skip -= 1


def backspace_compare(left: str, right: str):
    return all(a == b for (a, b) in
               zip_longest(
                   process_backspaces(left),
                   process_backspaces(right))
               )
