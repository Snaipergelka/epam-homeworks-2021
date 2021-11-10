"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts
    a Sequence of integers, and returns if the given
    sequence is a Fibonacci sequence.

We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    if data[0] != 0 or data[1] != 1:
        return False
    for d in range(len(data) - 1, 1, -1):
        if data[d] < 0:
            return False
        if data[d] != data[d - 1] + data[d - 2]:
            return False
    return True
