from homework2.task5 import custom_range


def test_positive_custom_range():
    assert custom_range('abcdertgfswdfgh', 'd', 't', -2) == ['d', 'b']


def test_negative_custom_range():
    assert custom_range(['a', 'b', 'c']) is None
