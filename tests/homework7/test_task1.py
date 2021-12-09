from homework7.task1 import find_occurrences


first_tmp = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "a": "BLUE",
        "RED": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}

second_tmp = {
    "first": [1, 2],
    "second": {
        "simple_key": ["simple", 1, "1", "RED", "valued"],
    },
    "third": {},
    "fourth": 1
}

third_tmp = {}


def test_find_occurrences():
    assert find_occurrences(first_tmp, "RED") == 7 \
           and find_occurrences(second_tmp, 2) == 1 \
           and find_occurrences(third_tmp, 4) == 0
