"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    result = []
    inp = list(args)

    def permutations(lists: List[List[Any]], depth: int, current: List[Any]):
        if depth == len(lists):
            result.append(current)
            return
        for i in lists[depth]:
            permutations(lists, depth + 1, current + [i])
        return result
    return list(sorted(permutations(inp, 0, [])))
