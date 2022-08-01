class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value: int = 0) -> None:
        self.value = start_value


class TableValues:

    def __init__(self, rows: int, cols: int, cell=None) -> None:
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = [[cell() for j in range(cols)] for i in range(rows)]

    def __getitem__(self, item: int) -> int:
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()