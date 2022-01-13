import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize("test_input",
                         [[0, 1, 1, 2, 6, 5, 8],
                          (0, 1, 3, 1), [0, 0, 0, 0, 0],
                          [-1, -1, -2, -3, -4], [2, 2, 4, 6, 10]])
def test_negative_cases(test_input):
    """Testing that non-Fibonacci sequence gives False"""
    assert not check_fibonacci(test_input)


@pytest.mark.parametrize("test_input",
                         [[0, 1, 1, 2, 3, 5, 8],
                          (0, 1, 1)])
def test_positive_cases(test_input):
    """Testing that Fibonacci sequence gives True"""
    assert check_fibonacci(test_input)
