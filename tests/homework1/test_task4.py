import pytest

from homework1.task4 import check_sum_of_four


@pytest.mark.parametrize("A,B,C,D,expected",
                         [([1, 2, 3, 6, 7], [2, 3, 5, 7, 9], [0, 8, 5, 7, 9],
                           [1, 2, 3, 4, 5], 0),
                          ([1, 1], [1, 1], [1, 1], [1, 1], 0)])
def test_negative_case(A, B, C, D, expected):
    """Testing that if input arrays don't have sum of four elements
       equal to 0 function gives 0."""
    assert check_sum_of_four(A, B, C, D) == expected


@pytest.mark.parametrize("A,B,C,D,expected",
                         [([1, 5, 9, 8], [2, 6, 7, 4], [-2, -5, 9, 8],
                           [-1, -6, 7, 4], 4),
                          ([0, 0], [0, 0], [0, 0], [0, 0], 16)])
def test_positive_case(A, B, C, D, expected):
    """Testing  if input arrays have sum of four elements
       equal to 0 function gives an appropriate result."""
    assert check_sum_of_four(A, B, C, D) == expected
