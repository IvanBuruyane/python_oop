from typing import Any


class Cell:

    def __init__(self, data: Any) -> None:
        self.__data = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        if type(value) is not type(self.__data):
            raise TypeError('неверный тип присваиваемых данных')
        self.__data = value


class TableValues:

    def __init__(self, rows: int, cols: int, type_data: Any = int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for i in range(cols)] for j in range(rows)]

    def check_index(self, indx: tuple) -> None:
        row, col = indx
        if type(row) is not int or type(row) is not int or (row < 0 or row > self.rows) or (col < 0 or col > self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: tuple) -> Any:
        self.check_index(item)
        row, col = item
        return self.table[row][col].data

    def __setitem__(self, key: tuple, value: Any) -> None:
        self.check_index(key)
        row, col = key
        self.table[row][col].data = value

    def __iter__(self):
        self.__i = 0
        self.__row_value = self.table[self.__i]
        return self

    def __next__(self):
        if self.__i < self.rows:
            res = iter([cell.data for cell  in self.__row_value])
            self.__i += 1
            if self.__i < self.rows:
                self.__row_value = self.table[self.__i]
            return res
        else:
            raise StopIteration


table = TableValues(3, 5)
for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
