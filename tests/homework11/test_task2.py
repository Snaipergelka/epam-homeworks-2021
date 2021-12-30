from homework11.task2 import Order, elder_discount, morning_discount


def test_strategies():
    """
        Testing that method final price sets strategy and
        executes them correctly.
    """
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10 and order_1.final_price() == 75


def discrimination_strategy(order):
    return order.price * 2


def test_setting_new_strategy():
    """
        Testing that Context and Order classes can set and execute
        new strategies.
    """
    order = Order(50, discrimination_strategy)
    assert order.final_price() == 100
