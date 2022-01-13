from homework9.task3 import universal_file_counter


def test_custom_tokenizer():
    """
    Testing that function works correctly with custom
    tokenizer
    """
    assert 14 == universal_file_counter(
        "tests/homework9/test3_dir", 'txt', str.split)


def test_default_tokenizer():
    """
    Testing that function works correctly with custom
    tokenizer
    """
    assert 7 == universal_file_counter(
        "tests/homework9/test3_dir", 'txt')
