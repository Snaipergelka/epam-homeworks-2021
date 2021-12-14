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

        self.text = self.reading_text_lines(file_path)
        try:
            self.dict = self.making_dict_from_text(self.text)
        except Exception:
            ValueError("Some problem happened!")

        if not all(map(self.validate_key, self.dict.keys())):
            raise ValueError("Some problem happened!")

        for k, v in self.dict.items():
            if hasattr(self, k) and k not in self.dict:
                raise ValueError("Name clashes with standard attribute name!")

            setattr(self, k, v)

    @staticmethod
    def reading_text_lines(file_path: str):

        file = open(file_path)
        file_text = file.readlines()
        file.close()
        return file_text

    @staticmethod
    def making_dict_from_text(text):

        file_dict = {}
        for word in text:
            key, value = word.replace("\n", "").split("=")

            if "." in value and value.replace(".", "").isdigit():
                value = float(value)

            if type(value) is str and value.isdigit():
                value = int(value)

            file_dict[key] = value

        return file_dict

    @staticmethod
    def validate_key(key):
        return type(key) is str and (not iskeyword(key)) and key.isidentifier()

    def __getitem__(self, key):
        return self.dict[key]
