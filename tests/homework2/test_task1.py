import pytest

from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt",
                           [('unmißverständliche', 12),
                            ('vernachlässigt', 12),
                            ('fingerabdrucks', 12),
                            ('außenpolitisch', 12),
                            ('verständlich', 12),
                            ('außerordentliche', 11),
                            ('zwingherrschaft', 11),
                            ('vorausgeschickt', 11),
                            ('machtbewußtsein', 11),
                            ('überwältigende', 11)]),
                          ("tests/homework2/test_task1_cases/data_2.txt",
                           [('exploration', 9),
                            ('boulangerie', 9),
                            ('bartholdi', 9),
                            ('magnifique', 8),
                            ('pralines', 8),
                            ('limonade', 8),
                            ('typiquement', 7),
                            ('lyonnaise', 7),
                            ('croissant', 7),
                            ('rejoint', 7)]),
                          ('tests/homework2/test_task1_cases/data_3.txt', [])])
def test_get_longest_diverse_words(test_input, expected):
    assert get_longest_diverse_words(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt", 'ä'),
                          ("tests/homework2/test_task1_cases/data_2.txt", 'Ã'),
                          ('tests/homework2/test_task1_cases/data_3.txt', '')])
def test_get_most_common_non_ascii_char(test_input, expected):
    assert get_most_common_non_ascii_char(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt", '›'),
                          ("tests/homework2/test_task1_cases/data_2.txt", 'V'),
                          ('tests/homework2/test_task1_cases/data_3.txt', '')])
def test_get_rarest_char(test_input, expected):
    assert get_rarest_char(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt",
                           2970),
                          ("tests/homework2/test_task1_cases/data_2.txt",
                           58),
                          ('tests/homework2/test_task1_cases/data_3.txt', 0)])
def test_count_non_ascii_chars(test_input, expected):
    assert count_non_ascii_chars(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [("tests/homework2/test_task1_cases/data_1.txt",
                           9377),
                          ("tests/homework2/test_task1_cases/data_2.txt",
                           68),
                          ('tests/homework2/test_task1_cases/data_3.txt', 0)])
def test_count_punctuation_chars(test_input, expected):
    assert count_punctuation_chars(test_input) == expected
