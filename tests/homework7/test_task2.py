from homework7.task2 import backspace_compare


def test_only_backspaces():
    """
    Testing that function works correctly
    when string contains only backspaces
    """

    string_1 = "###########"
    string_2 = ""
    assert backspace_compare(string_1, string_2)


def test_positive():
    """
    Testing that function returns correct result
    when strings are equal
    """
    assert backspace_compare("#a#cc#d", "1d####cd")


def test_negative():
    """
    Testing that function returns correct result
    when strings are not equal
    """

    assert not backspace_compare("###dss@#", "eww")


def test_if_no_backspaces_contained():
    """
    Testing that function works correctly when
    strings doesn't contain any backspaces
    """

    assert backspace_compare("asdf", "asdf")
