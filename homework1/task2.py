"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts
    a Sequence of integers, and returns if the given
    sequence is a Fibonacci sequence.

We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def fibonacci_gen():
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i + j


def check_fibonacci(data: Sequence[int]) -> bool:
    for our_element, original_element in zip(data, fibonacci_gen()):
        if our_element != original_element:
            return False
    return True
