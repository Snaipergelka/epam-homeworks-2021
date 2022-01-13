import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize("test_input,k,expected",
                         [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                          ([-1, -2, -2], 3, -1),
                          ([0, 1, 2], 5, 3), ([0, 1, 2], 3, 3),
                          ([9, 7, -1000, 2000], 3, 2000)])
def test_find_maximum_subarray_sum(test_input, k, expected):
    """Testing that if length of array is longer, shorter or equal to k
       function calculates max subarray."""
    assert find_maximal_subarray_sum(test_input, k) == expected
