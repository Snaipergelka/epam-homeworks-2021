"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

"""
from contextlib import contextmanager


class SuppressorClass:

    def __init__(self, *errors):
        self.errors = errors

    def __enter__(self):
        pass

    def __exit__(self, err_type, err_val, err_tb):
        return err_type is not None \
               and issubclass(err_type, self.errors)


@contextmanager
def suppression_gen(*exceptions):
    try:
        yield exceptions
    except exceptions:
        pass
