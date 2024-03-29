"""
    Write down the function, which reads input line-by-line,
    and find maximum and minimum values.

    Function should return a tuple with the max and min values.
    For example for [1, 2, 3, 4, 5], function should return [1, 5]
    We guarantee, that file exists and contains line-delimited integers.
    To read file line-by-line you can use this snippet:
    with open("some_file.txt") as fi:
        for line in fi:
            ...
"""
from collections import namedtuple
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    result_tuple = namedtuple(typename='min_and_max',
                              field_names=('minimum', 'maximum'))
    with open(file_name) as fi:
        ma = int(fi.readline())
        mi = ma
        for line in fi:
            if int(line) > ma:
                ma = int(line)
            if int(line) < mi:
                mi = int(line)
    return result_tuple(minimum=mi, maximum=ma)
