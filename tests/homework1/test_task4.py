from homework1.task4 import check_sum_of_four


def test_negative_case():
    """Testing with length of lists > 0 and 0 needed tuples"""
    assert check_sum_of_four(
            [1, 2, 3, 6, 7],
            [2, 3, 5, 7, 9],
            [0, 8, 5, 7, 9],
            [1, 2, 3, 4, 5]
            ) == 0


def test_positive_case():
    """Testing with 4 needed tuples"""
    assert check_sum_of_four(
            [1, 5, 9, 8],
            [2, 6, 7, 4],
            [-2, -5, 9, 8],
            [-1, -6, 7, 4]
            ) == 4


def test_zero_case():
    """Testing that lists with zeroes give 16"""
    assert check_sum_of_four([0, 0], [0, 0], [0, 0], [0, 0]) == 16


def test_corner_case():
    """Testing that lists with the same integers != 0 give 0"""
    assert check_sum_of_four([1, 1], [1, 1], [1, 1], [1, 1]) == 0
