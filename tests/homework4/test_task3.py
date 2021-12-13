import logging

from homework4.task3 import my_precious_logger


def test_my_precious_logger_stdout(caplog):
    """
        Testing that function prints in stdout if input without
        error-word in the beginning.
    """
    caplog.set_level(logging.INFO)
    my_precious_logger('Meow')
    assert 'OK' == caplog.records[0].message


def test_my_precious_logger_stderr(caplog):
    """
        Testing that function prints in stderr if input with
        error-word in the beginning.
    """
    caplog.set_level(logging.ERROR)
    my_precious_logger('error: not found')
    assert 'error: not found' == caplog.records[0].message
