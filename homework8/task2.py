import sqlite3
import string
from typing import Iterable, List, Optional


# Plain filter for validating table names
def sanitize_table_name(table_name: str) -> str:
    for char in table_name:
        if char in string.punctuation:
            raise ValueError("Not valid table name")
    return table_name


class TableData(Iterable):

    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_name)

    def __getitem__(self, key: str) -> Optional[str]:
        rows = self.__select_name(key)
        return rows[0] if rows else None

    def __contains__(self, item: str) -> bool:
        rows = self.__select_name(item)
        return len(rows) > 0

    # implemented as select * where name=? because
    # db backend is more optimized
    def __select_name(self, name: str) -> List[str]:
        cursor = self.connection.cursor()

        string_select = 'SELECT * from ' + \
                        sanitize_table_name(self.table_name) + \
                        ' where name=:name'
        cursor.execute(string_select, {"name": name})
        rows = cursor.fetchall()

        cursor.close()
        return rows

    def __iter__(self):
        self.cursor = self.connection.cursor()
        string_select = 'SELECT * from ' + sanitize_table_name(self.table_name)
        self.cursor.execute(string_select)
        return self

    def __next__(self) -> dict:
        next_row = self.cursor.fetchone()
        names = list(map(lambda x: x[0], self.cursor.description))

        if next_row:
            return dict(zip(names, next_row))
        else:
            self.cursor.close()
            raise StopIteration

    def __del__(self):
        self.connection.close()
