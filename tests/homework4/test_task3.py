from homework4.task3 import my_precious_logger


def test_my_precious_logger_stdout(capsys):
    """
        Testing that function prints in stdout if input without
        error-word in the beginning.
    """
    my_precious_logger('Meow')
    captured = capsys.readouterr()
    assert captured.out == 'INFO:root:OK\n' and captured.err == ''


def test_my_precious_logger_stderr(capsys):
    """
        Testing that function prints in stderr if input with
        error-word in the beginning.
    """
    my_precious_logger('error: not found')
    captured = capsys.readouterr()
    assert captured.err == 'error: not found\n' and captured.out == ''
