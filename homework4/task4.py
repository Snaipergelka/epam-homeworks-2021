"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
        Testing that fizzbuzz function returns fizzbuzz sequence.
        >>> fizzbuzz(5)
        [1, 2, 'Fizz', 4, 'Buzz']

        >>> fizzbuzz(15)
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7,
         8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']

        Testing that fizzbuzz function returns [] if number is negative.
        >>> fizzbuzz(-15)
        []
    """
    if n < 1:
        return []
    numbers = []
    for number in range(1, n+1):
        if number % 15 == 0:
            numbers.append('Fizz Buzz')
        elif number % 3 == 0:
            numbers.append('Fizz')
        elif number % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(number)
    return numbers
