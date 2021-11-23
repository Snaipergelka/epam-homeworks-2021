"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
"""
import sys


def my_precious_logger(text: str):
    if text[0:5].lower() == 'error':
        print(text, file=sys.stderr)
    else:
        print('OK')
