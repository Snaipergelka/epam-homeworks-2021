"""
We have a file that works as key-value storage, each line
is represented as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string,
it is treated as number.

Write a wrapper class for this key value storage
that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible
as collection items and as attributes. Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something)
ValueError should be raised.
File size is expected to be small, you are permitted
to read it entirely into memory.

name=kek
last_name=top
power=9001
song=shadilay
"""
from keyword import iskeyword


class KeyValueStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        lines = self.reading_text_lines(file_path)
        pairs = [self.__convert_line_to_pairs(line) for line in lines]

        # validate pairs for key validity
        if not all(map(lambda x: self.validate_key(x[0]), pairs)):
            raise ValueError("Not valid Key")

        self.__internal_storage = dict(pairs)

        for k, v in self.__internal_storage.items():
            setattr(self, k, v)

    @staticmethod
    def reading_text_lines(file_path: str):
        file = open(file_path)
        file_text = file.readlines()
        file.close()
        return file_text

    @staticmethod
    def __convert_line_to_pairs(line: str):
        key, value = line.replace("\n", "").split("=")
        # condition for case when value is int
        if type(value) is str and value.isdigit():
            return key, int(value)

        # condition for case when value is float
        if type(value) is str and "." in value and \
                value.replace(".", "").isdigit():
            return key, float(value)

        return key, value

    @staticmethod
    def validate_key(key):
        """
        Checks conditions:
            1. if key is str, it is needed to create attribute
            2. if key is suitable identifier
            3. if key is not built-in attribute
        """
        return (
                type(key) is str
                and (not iskeyword(key))
                and key.isidentifier()
                and key not in dir(object)
        )

    def __getitem__(self, key):
        return self.__internal_storage[key]
