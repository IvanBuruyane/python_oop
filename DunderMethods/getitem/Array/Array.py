class Integer:

    def __init__(self, start_value: int = 0) -> None:
        self.__value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError('должно быть целое число')
        self.__value = value

    def __str__(self):
        return str(self.__value)


class Array:

    def __init__(self, max_length: int, cell: Integer) -> None:
        self.array = [cell() for i in range(max_length)]

    def check_index(self, indx: int) -> None:
        if type(indx) is not int or (indx < 0 or indx >= len(self.array)):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item: int):
        self.check_index(item)
        return self.array[item].value

    def __setitem__(self, key: int, value) -> None:
        self.check_index(key)
        self.array[key].value = value

    def __str__(self):
        return " ".join([str(item.value) for item in self.array])


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[9] = 1
print(ar_int)