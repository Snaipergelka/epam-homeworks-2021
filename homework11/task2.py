"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""


class Order:
    """
       This class saves discount strategy and price of the goods
       in attributes self.price, self.discount and using
       class Context instance sets strategies and executes them on price.
    """
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount = discount_strategy

    def final_price(self):
        """
            This method creates Context instance sets and executes
            discount strategy on price.
        """
        context = Context()
        context.set_strategy(self.discount)
        result = context.execute_strategy(self)
        return result


class Context:
    """
        This class sets and executes discount strategies.
    """
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy
        return strategy

    def execute_strategy(self, price):
        return self._strategy(price)


def morning_discount(order):
    morning_discount_value = 0.25
    return order.price - order.price * morning_discount_value


def elder_discount(order):
    elder_discount_value = 0.9
    return order.price - order.price * elder_discount_value
