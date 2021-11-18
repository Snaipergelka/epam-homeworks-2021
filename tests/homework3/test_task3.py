import pytest

from homework3.task3 import Filter, make_filter


@pytest.mark.parametrize("test_input,expected",
                         [(range(5), [2, 4]),
                          (range(2, 10), [2, 4, 6, 8]),
                          (range(20, 11, -1), [20, 18, 16, 14, 12])])
def test_filter_positive_cases(test_input, expected):
    """Testing that class supports more than 1 argument input.
    And method apply returns
    filtered list using all input-filters."""
    positive_even = Filter(lambda a: a % 2 == 0,
                           lambda a: a > 0,
                           lambda a: isinstance(a, int))
    assert positive_even.apply(test_input) == expected


test_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    },
    {
        "name": "mary",
        "kind": "parrot",
        "type": "bird"
    }
]


@pytest.mark.parametrize("test_input,expected",
                         [(["polly", "bird"],
                          [{
                              "is_dead": True,
                              "kind": "parrot",
                              "type": "bird",
                              "name": "polly"
                          }]),
                          (["mary", "human"], [])])
def test_make_filter(test_input, expected):
    """Testing that function generates filters for 1 and more criteria."""
    assert make_filter(
                        name=test_input[0],
                        type=test_input[1]
                      ).apply(test_data) == expected


def test_negative_make_filter():
    """Testing that function returns even if key not in data."""
    assert make_filter(
                        name="mary",
                        bug="human"
                      ).apply(test_data) == [{
                                                "name": "mary",
                                                "kind": "parrot",
                                                "type": "bird"
                                            }]
