import pytest

from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


@pytest.mark.parametrize("test_input,expected",
                         [("test_task1_cases/data_2.txt",
                           [('exploration', 9), ('boulangerie', 9),
                            ('Bartholdi', 9), ('magnifique', 8),
                            ('pralines', 8), ('limonade', 8),
                            ('typiquement', 7), ('lyonnaise', 7),
                            ('croissant', 7), ('rejoint', 7)]),
                          ("test_task1_cases/data_3.txt",
                           [('vorgebahnte', 9), ('Betrachtung', 9),
                            ('ausführen', 9), ('vielmehr', 6),
                            ('verbirgt', 6), ('bedenkli', 6),
                            ('machen', 6), ('hinter', 6),
                            ('gefaßt', 6), ('sondern', 5)])])
def test_get_longest_diverse_words(test_input, expected):
    """Testing that function gives 10 longest and most unique
     words in list of tuples."""
    assert get_longest_diverse_words(test_input, encoding="unicode-escape") == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt", 'ä'),
                          ("tests/homework2/test_task1_cases/data_2.txt", 'Ã'),
                          ("tests/homework2/test_task1_cases/data_3.txt",
                           'ü')])
def test_get_most_common_non_ascii_char(test_input, expected):
    """Testing that function gets most common non-ascii symbol from file"""
    assert get_most_common_non_ascii_char(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt", '›'),
                          ("tests/homework2/test_task1_cases/data_2.txt", 'V'),
                          ("tests/homework2/test_task1_cases/data_3.txt",
                           '1')])
def test_get_rarest_char(test_input, expected):
    """Testing that function gets rarest char from file"""
    assert get_rarest_char(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_2.txt",
                           58),
                          ("tests/homework2/test_task1_cases/data_3.txt", 32)])
def test_count_non_ascii_chars(test_input, expected):
    """Testing that function counts all non-ascii chars from file"""
    assert count_non_ascii_chars(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_2.txt",
                          26),
                          ("tests/homework2/test_task1_cases/data_3.txt", 9)])
def test_count_punctuation_chars(test_input, expected):
    """Testing that function counts all punctuation chars from file"""
    assert count_punctuation_chars(test_input) == expected
