from homework9.task2 import SuppressorClass, suppression_gen


def test_specified_exception():
    """
    Testing that suppressor suppresses exceptions which
     are specified
    """
    try:
        with SuppressorClass(IndexError, FileExistsError):
            [][3]
            with open('m.txt') as fi:
                print(fi)
        assert True
    except Exception:
        assert False


def test_not_specified_exceptions():
    """
    Testing that suppressor doesn't suppresses exceptions which
     are not specified
    """
    try:
        with SuppressorClass(FileExistsError):
            [][3]
            with open('m.txt') as fi:
                print(fi)
        assert False
    except IndexError:
        assert True


def test_generator_suppressor():
    """
    Testing that generator-based suppressor works correctly
    """
    try:
        with suppression_gen(KeyError, FileExistsError):
            {}[3]
        assert True
    except Exception:
        assert False


def test_generator_suppressor_superclass():
    """
    Testing that generator-based suppressor works if
    pass superclass
    """
    try:
        with suppression_gen(Exception):
            {}[3]
        assert True
    except Exception:
        assert False
