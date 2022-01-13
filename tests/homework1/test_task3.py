from homework1.task3 import find_maximum_and_minimum


def test_positive_case():
    """Testing that input file with positive integers (from 1 to 5)
    gives (1, 5)"""
    assert find_maximum_and_minimum(
        'tests/homework1/test_task3_cases/case_positive.txt') == (1, 5)


def test_negative_number_case():
    """Testing that input file with unsorted
    sequence of negative integers (from -15 to -300)
    gives (-300, -15)"""
    assert find_maximum_and_minimum(
            'tests/homework1/test_task3_cases/case_negative_integers.txt'
            ) == (-300, -15)
