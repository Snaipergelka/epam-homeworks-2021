"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.
"""


def fizzbuzz_gen(n):
    for current in range(1, n+1):
        yield "Fizz"*(current % 3 == 0) + "Buzz"*(current % 5 == 0)\
              or current
