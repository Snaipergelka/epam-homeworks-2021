import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize("test_input,expected",
                         [(0, True), (1, True),
                          (9, True), (370, True),
                          (371, True), (407, True),
                          (1634, True), (8208, True),
                          (9474, True), (54748, True),
                          (92727, True), (93084, True),
                          (548834, True)])
def test_is_armstrong_positive_cases(test_input, expected):
    """Testing that function detects Armstrong numbers"""
    assert is_armstrong(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [(-10, False), (10, False),
                          (150, False), (415, False),
                          (380, False), (420, False),
                          (1638, False), (8200, False),
                          (9374, False), (54848, False),
                          (92456, False), (93345, False),
                          (5478834, False)])
def test_is_armstrong_negative_cases(test_input, expected):
    """Testing that function detects non-Armstrong numbers"""
    assert is_armstrong(test_input) == expected
