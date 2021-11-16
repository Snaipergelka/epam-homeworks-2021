"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']
"""
from typing import Any, Iterable, List, Optional


def custom_range(iterable: Iterable[Any],
                 start_val=None,
                 stop_val=None,
                 step_val=1) -> Optional[List]:
    result = []
    if stop_val is None:
        return None
    # Change start and stop value
    if step_val < 0:
        start_val, stop_val = stop_val, start_val
    # Append i in result until stop_val
    for i in iterable:
        result.append(i)
        if i == stop_val:
            break
    # Slice result from the start
    for i, j in enumerate(result):
        if j == start_val:
            result = result[i:]
    # Delete stop value from list
    if step_val > 0:
        result.pop()

    result = result[::step_val]
    return result
