from typing import List
import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data: List[str]) -> None:
        for string in data:
            dct = {DataBase.FIELDS[i]: string.split(" ")[i] for i in range(len(DataBase.FIELDS))}
            self.lst_data.append(dct)

    def select(self, a: int, b: int) -> List[str]:
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
