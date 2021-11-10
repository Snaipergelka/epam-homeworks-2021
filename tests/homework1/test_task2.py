from homework1.task2 import check_fibonacci


def test_negative_case():
    """Testing that non-Fibonacci sequence gives False"""
    assert not check_fibonacci([0, 1, 1, 2, 6, 5, 8])


def test_positive_case():
    """Testing that Fibonacci sequence gives True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13])


def test_corner_case():
    """Testing that sequence with 1 element gives False"""
    assert not check_fibonacci((0, 1, 3, 1, 2))


def test_corner_zeroes_case():
    """Testing that sequence of zeroes gives False"""
    assert not check_fibonacci([0, 0, 0, 0, 0])


def test_start_of_sequence_case():
    """Testing that sequence which does not start from zero and one
    gives False"""
    assert not check_fibonacci((2, 3, 5, 8, 13))


def test_negative_sequence():
    """Testing that sequence of negative numbers gives False"""
    assert not check_fibonacci([-1, -1, -2, -3, -4])
