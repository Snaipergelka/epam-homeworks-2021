"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def iterate_over_tree(tree: dict, element: Any) -> int:

    if isinstance(tree, dict):
        for key, val in tree.items():
            if isinstance(val, (list, tuple, set, dict)):
                yield from iterate_over_tree(val, element)
            else:
                yield val
            if isinstance(key, (tuple, set)):
                yield from iterate_over_tree(key, element)
            else:
                yield key
    elif isinstance(tree, (list, tuple, set)):
        for val in tree:
            if isinstance(val, (list, tuple, set, dict)):
                yield from iterate_over_tree(val, element)
            else:
                yield val


def find_occurrences(tree: dict, element: Any) -> int:

    return sum((1 if leaf == element else 0
                for leaf in iterate_over_tree(tree, element)))
