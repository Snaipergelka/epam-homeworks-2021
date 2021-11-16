import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize("test_input,expected",
                         [([2, 2, 1, 1, 1, 2, 2], (2, 1)),
                          ([2, 3, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5, 6, 5], (5, 3)),
                          ([1, 2, 3, 4, 5], (0, 0))])
def test_major_and_minor_elem(test_input, expected):
    assert major_and_minor_elem(test_input) == expected
