from typing import Any


class FloatValue:

    @staticmethod
    def is_float(value: Any) -> bool:
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        else:
            return True

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.is_float(value):
            setattr(instance, self.name, value)


class Cell:

    value = FloatValue()

    def __init__(self, value: float) -> None:
        self.value = value


class TableSheet:

    def __init__(self, n: int,  m: int, ) -> None:
        self.cells = [[Cell(float(0)) for i in range(n)] for j in range(m)]

m = 3
n = 5
table = TableSheet(n, m)
for i in range(n):
    for j in range(m):
        print(table.cells[i][j].value, end=" ")
    print()
for i in range(n):
    for j in range(m):
        table.cells[i][j].value = float(i * m + j + 1)
print()
for i in range(n):
    for j in range(m):
        print(table.cells[i][j].value, end=" ")
    print()