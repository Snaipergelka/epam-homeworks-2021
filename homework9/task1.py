"""
Write a function that merges integer from sorted files and returns an iterator
test_task1_file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from functools import reduce
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    def _opening_files(file_path):
        with open(file_path) as file:
            for line in file:
                yield int(line.strip('\n'))
    file_gens = (_opening_files(file_path) for file_path in file_list)
    initial = next(file_gens)
    return reduce(lazy_merge, file_gens, initial)


def lazy_merge(first_sorted_ints_generator, second_sorted_ints_generator):
    first_sort_ints_generator_next = next(first_sorted_ints_generator)
    second_sort_ints_generator_next = next(second_sorted_ints_generator)
    while True:
        if first_sort_ints_generator_next > second_sort_ints_generator_next:
            yield second_sort_ints_generator_next
            second_sort_ints_generator_next = next(
                                                second_sorted_ints_generator,
                                                None)
            if second_sort_ints_generator_next is None:
                yield first_sort_ints_generator_next
                yield from first_sorted_ints_generator
                return
        else:
            yield first_sort_ints_generator_next
            first_sort_ints_generator_next = next(
                                               first_sorted_ints_generator,
                                               None)
            if first_sort_ints_generator_next is None:
                yield second_sort_ints_generator_next
                yield from second_sorted_ints_generator
                return
