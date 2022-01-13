from itertools import zip_longest

from homework9.task1 import merge_sorted_files


def test_one_by_one_case():
    """
    Testing that function merges files and returns sorted iterator
    """
    merged = merge_sorted_files([
        "tests/homework9/test_task1_file1.txt",
        "tests/homework9/test_task1_file2.txt"])
    assert all(x[0] == x[1] for x in zip_longest(merged, range(0, 8)))


def test_negative_numbers():
    """
    Testing that function merges correctly when they contain negative numbers
    """
    merged = merge_sorted_files([
            "tests/homework9/test_task1_file1.txt",
            "tests/homework9/test_task1_file3.txt"])
    correct = [-7, -5, 0, 1, 3, 4, 5, 7]
    assert all(x[0] == x[1] for x in zip_longest(merged, correct))


def test_symmetric():
    """
    Testing that merge_sorted_files(x, y) == merge_sorted_files(y, x)
    """
    merged1 = merge_sorted_files([
        "tests/homework9/test_task1_file1.txt",
        "tests/homework9/test_task1_file3.txt"])
    merged2 = merge_sorted_files([
        "tests/homework9/test_task1_file3.txt",
        "tests/homework9/test_task1_file1.txt"])
    assert all(x[0] == x[1] for x in zip_longest(merged1, merged2))


def test_iterator():
    """
    Testing that merge_sorted_files returns Iterator
    """
    merged1 = merge_sorted_files([
        "tests/homework9/test_task1_file1.txt",
        "tests/homework9/test_task1_file3.txt"])
    correct = [-7, -5, 0, 1, 3, 4, 5, 7]
    assert all(x[0] == x[1] for x in zip_longest(merged1, correct)) and \
        next(merged1, None) is None
