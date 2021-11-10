from homework1.task5 import find_maximal_subarray_sum


def test_positive_case():
    """Testing that array with length > 0 gives 16"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_negative_test():
    """Testing that list with length == 0 gives None"""
    assert find_maximal_subarray_sum([], 3) is None


def test_negative_numbers_case():
    """Testing that list with only negative numbers returns -1"""
    assert find_maximal_subarray_sum([-1, -2, -2], 3) == -1


def test_when_k_more_length():
    """Testing that if k more length function gives an appropriate result"""
    assert find_maximal_subarray_sum([0, 1, 2], 5) == 3


def test_when_k_equals_length():
    """Testing that if k equals length function gives an appropriate result"""
    assert find_maximal_subarray_sum([0, 1, 2], 3) == 3


def test_last_element():
    """Testing that if last element is the largest
    gives an appropriate result"""
    assert find_maximal_subarray_sum([9, 7, -1000, 2000], 3) == 2000
