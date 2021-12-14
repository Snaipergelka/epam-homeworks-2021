from itertools import zip_longest

from homework8.task2 import TableData


def test_iteration():
    """
    Tests that iteration works correctly
    """
    table = TableData("tests/homework8/example.sqlite", "presidents")
    records = [
        {'name': 'Yeltsin', 'age': 999, 'country': 'Russia'},
        {'name': 'Trump', 'age': 1337, 'country': 'US'},
        {'name': 'Big Man Tyrone', 'age': 101, 'country': 'Kekistan'}
    ]

    assert all(map(lambda x: x[0] == x[1], zip_longest(records, table)))


def test_get():
    """
    Tests that obj[key] works correctly
    """
    table = TableData("tests/homework8/example.sqlite", "presidents")

    assert table['Yeltsin'] == ('Yeltsin', 999, 'Russia') and \
           table['Meow'] is None


def test_in():
    """
    Tests that 'in' works correctly
    """
    table = TableData("tests/homework8/example.sqlite", "presidents")

    assert 'Trump' in table and 'Meow' not in table
