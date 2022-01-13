from homework2.task5 import custom_range


def test_positive_custom_range():
    """Testing that function gives a list considering
    start, stop, step values"""
    assert custom_range('abcdertgfswdfgh', 'd', 't', -2) == ['d', 'b']


def test_negative_custom_range():
    """Testing that function returns input if there are no parameters
    except iterator"""
    assert custom_range(['a', 'b', 'c'], 'd') == ['a', 'b', 'c']
