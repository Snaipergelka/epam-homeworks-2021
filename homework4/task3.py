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
import logging


def my_precious_logger(text: str):
    if text.lower().startswith('error'):
        logging.error(text)
    else:
        logging.info('OK')


my_precious_logger('Error ')
