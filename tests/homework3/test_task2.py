from homework3.task2 import check_slow_calculate


def test_slow_calculate():
    """Testing that function calculates numbers
    for less than 60 seconds."""
    assert check_slow_calculate(60) < 60
