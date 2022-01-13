"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
Write a test for that function using pytest library.
You should create files required for the testing
inside the test run and remove them after the test run.
(Opposite to previous homeworks when you used
files created manually before the test.)
"""


def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            first_line = file.readline()
    except Exception:
        raise ValueError("Something strange happened")

    return (first_line.replace(".", "").isdigit() and
            1 <= float(first_line) < 3)
