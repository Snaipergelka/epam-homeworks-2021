"""
Write a test for that function using pytest library.
You should create files required for the testing inside
the test run and remove them after the test run.
(Opposite to previous homeworks when you used files
 created manually before the test.)
"""
import os
import random
import tempfile
import unittest

from homework4.task1 import read_magic_number


def make_test_data(start: int, end: int, random_char=None):
    """
        Making new test file.
    """
    file = tempfile.NamedTemporaryFile(suffix='.txt',
                                       prefix='test_data',
                                       mode="w",
                                       dir='tests/homework4',
                                       delete=False)
    # Writing chars and/or numbers in file.
    if random_char is not None:
        file.write(str(random_char))
    element = random.randrange(start, end)
    file.write(str(element))
    # Save data in file and close it.
    file.flush()
    file.close()
    return file.name


def test_positive_magic_number():
    """
        Testing that when first line is a num [1,3) function returns True.
    """
    f_name = make_test_data(1, 2)
    assert read_magic_number(f_name)
    print(f_name)
    os.remove(f_name)


def test_negative_magic_number():
    """
        Testing that if file starts with not num function returns False.
    """
    f_name = make_test_data(3, 10, random_char='c')
    assert not read_magic_number(f_name)
    os.remove(f_name)


class TestStringMethods(unittest.TestCase):
    """
        Testing that except catches errors and raises ValueError.
    """
    def test_errors(self):
        with self.assertRaises(ValueError):
            (read_magic_number("//"),
             read_magic_number("2", 1),
             read_magic_number(2))
