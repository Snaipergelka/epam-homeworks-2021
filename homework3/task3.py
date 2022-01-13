# There are multiple bugs in this code.
# Find them all and write tests for faulty cases.
# I decided to write a code that generates data filtering object
# from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


def create_filter_func(key, value):
    def keyword_filter_func(element):
        if key not in element:
            return True
        return element[key] == value
    return keyword_filter_func


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(create_filter_func(key, value))
    return Filter(*filter_funcs)
