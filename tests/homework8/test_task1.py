from homework8.task1 import KeyValueStorage


def test_check_access_methods():
    """
    Tests that file is read correctly and access via
    attributes and [key] is supported
    """
    storage = KeyValueStorage("tests/homework8/correct.txt")
    assert storage['sdd'] == 'hurma' and \
           storage.key == "value234"


def test_digit_transformation():
    """
    Tests that if string is a number, it is casted to
    Python number
    """
    storage = KeyValueStorage("tests/homework8/correct.txt")
    assert storage.a == 342


def test_invalid_key(capsys):
    """
    Tests that ValueError is raised in case of errors
    """
    try:
        KeyValueStorage("tests/homework8/wrong.txt")
    except ValueError:
        assert True
    except Exception:
        assert False
