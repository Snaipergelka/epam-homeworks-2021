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
                 *args) -> Optional[List]:
    start_val = None
    stop_val = None
    step_val = 1

    if len(args) == 1:
        stop_val = args[0]

    if len(args) == 2:
        start_val = args[0]
        stop_val = args[1]

    if len(args) == 3:
        start_val = args[0]
        stop_val = args[1]
        step_val = args[2]

    result = []
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
    if step_val > 0 and stop_val in iterable:
        result.pop()
    result = result[::step_val]
    return result
