"""
Write a doctest for function.
"""
from homework4.task4 import fizzbuzz


def test_fizzbuzz():
    """
        Testing that fizzbuzz function returns fizzbuzz sequence.
        >>> fizzbuzz(5)
        [1, 2, 'Fizz', 4, 'Buzz']

        >>> fizzbuzz(15)
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']

        Testing that fizzbuzz function returns [] if number is negative.
        >>> fizzbuzz(-15)
        []
    """
    assert fizzbuzz(3) == [1, 2, 'Fizz']
