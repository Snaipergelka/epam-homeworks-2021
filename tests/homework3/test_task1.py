from homework3.task1 import cache_fabric

i = 1


@cache_fabric(times=2)
def f(a, b):
    return a + b + i


def test_cache_f():
    """Testing that cache saves result of function 2 times after first call.
    For the third time result calculates again"""
    f(2, 3)
    global i
    i = 5
    first, second, third = (f(2, 3) for _ in range(3))
    assert first != third and first == second
