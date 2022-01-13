import pytest

from homework4.task5 import fizzbuzz_gen


@pytest.mark.parametrize("test_input,expected",
                         [(-15, []),
                          (5, [1, 2, 'Fizz', 4, 'Buzz']),
                          (15, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                                'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                                'FizzBuzz'])])
def test_fizzbuzz_gen(test_input, expected):
    """
        Testing that fizzbuzz function returns fizzbuzz sequence.
        Testing that fizzbuzz function returns [] if number is negative.
    """
    assert list(fizzbuzz_gen(test_input)) == expected
