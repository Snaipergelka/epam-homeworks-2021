import homework5.task2


def test_my_wraps():
    homework5.task2.custom_sum(1, 2, 3, 4)
    assert homework5.task2.custom_sum.__doc__ == "This function can sum " \
                                                 "any objects which have " \
                                                 "__add___" \
           and homework5.task2.custom_sum.__name__ == "custom_sum"
