"""
In previous homework task 4, you wrote a cache function
 that remembers other function output value.
 Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Example:
@cache(times=2)
def f():
    return input('? ')
f()
? 1
'1'

f()     # will remember previous value
'1'

f()     # but use it up to two times only
'1'

f()
? 2
'2'
"""
from typing import Callable


def cache_fabric(times):

    def my_cache(func: Callable) -> Callable:
        cache_dict = {}

        def wrapped(*args, **kwargs):
            key = (args, str(sorted(kwargs.items())))
            if key in cache_dict:
                cache_dict[key][1] -= 1
                if cache_dict[key][1] > -1:
                    return cache_dict[key][0]
                else:
                    del(cache_dict[key])
            result = func(*args, **kwargs)
            cache_dict[key] = [result, times]
            return result

        return wrapped

    return my_cache
