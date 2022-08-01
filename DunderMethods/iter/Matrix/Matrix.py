from typing import Any


class Matrix:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            lst = args[0]
            self.__check_input_list(lst)
            self.matrix = lst
            self.rows = len(lst)
            self.cols = len(lst[0])
        elif len(args) == 3:
            rows, cols, fill_value = args
            if type(rows) is not int or type(cols) is not int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows
            self.cols = cols
            self.matrix = [[fill_value for j in range(cols)] for i in range(rows)]

    @classmethod
    def __check_input_list(cls, lst: list) -> None:
        if type(lst) is not list:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        rows = len(lst)
        cols = len(lst[0])
        for row in lst:
            if len(row) != cols:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for number in row:
                if type(number) not in (int, float):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __check_index(self, indx: tuple) -> None:
        row, col = indx
        if type(row) is not int or type(col) is not int or not 0 <= row < self.rows or not 0 <= col < self.cols:
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item: tuple) -> float:
        self.__check_index(item)
        row, col = item
        return self.matrix[row][col]

    def __setitem__(self, key: tuple, value: float) -> None:
        self.__check_index(key)
        row, col = key
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[row][col] = value

    def __add__(self, other: Any):
        if type(other) is Matrix:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])
        elif type(other) in (int, float):
            return Matrix([[self.matrix[i][j] + other for j in range(self.cols)] for i in range(self.rows)])

    # def __radd__(self, other):
    #     return self + other

    def __sub__(self, other: Any):
        if type(other) is Matrix:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])
        elif type(other) in (int, float):
            return Matrix([[self.matrix[i][j] - other for j in range(self.cols)] for i in range(self.rows)])






lst1 = [[1, 2], [3, 4]]
lst2 = [[5, 6], [7, 8]]
print([[lst1[i][j] + lst2[i][j] for j in range(2)] for i in range(2)])


