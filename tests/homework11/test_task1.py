import pytest

from homework11.task1 import ColorsEnum, SimplifiedEnum, SizesEnum


@pytest.mark.parametrize('input_data,output', [
    (ColorsEnum.RED, "RED"), (SizesEnum.XL, "XL"),
    (ColorsEnum.BLUE, "BLUE"), (SizesEnum.L, "L"),
    (ColorsEnum.ORANGE, "ORANGE"), (SizesEnum.S, "S"),
    (ColorsEnum.BLACK, "BLACK"), (SizesEnum.M, "M")])
def test_positive_cases(input_data, output):
    """
        Testing that metaclass SimplifiedEnum creates
        attributes from keys.
    """
    assert input_data == output


def test_negative_cases():
    try:
        class EmptyStrInKeys(metaclass=SimplifiedEnum):
            __keys = ('', "C")

        class IntInKeys(metaclass=SimplifiedEnum):
            __keys = (1, 2, 3)
    except SyntaxError:
        assert True
