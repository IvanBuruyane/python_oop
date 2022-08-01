import random

class MaxPooling:

    def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
        self.step = step
        self.size = size

    def __call__(self, matrix: list, *args, **kwargs) -> list:
        self.is_matrix_valid(matrix)
        return self.__max_pooling(matrix, self.step[0], self.step[1], self.size[0], self.size[1])

    @staticmethod
    def is_matrix_valid(matrix: list) -> None:
        error = "Неверный формат для первого параметра matrix."
        if type(matrix) is not list:
            raise ValueError(error)
        if len(list(filter(lambda x: type(x) is list, matrix))) != len(matrix):
            raise ValueError(error)
        width = len(matrix[0])
        for line in matrix:
            if len(line) != width:
                raise ValueError(error)
            for element in line:
                if type(element) not in (int, float):
                    raise ValueError(error)

    @staticmethod
    def __max_pooling(matrix: list, kernel_width: int, kernel_height: int, step_hor: int, step_ver: int) -> list:
        matrix_height: int = len(matrix)
        matrix_width: int = len(matrix[0])
        current_row: int = 0
        result: list = []
        kernel_size: int = kernel_width * kernel_height
        while current_row + kernel_height <= matrix_height:
            result_row: list = []
            current_column: int = 0
            while current_column + kernel_width <= matrix_width:
                kernel: list = []
                for i in range(current_row, current_row + kernel_height):
                    for j in range(current_column, current_column + kernel_width):
                        try:
                            kernel.append(matrix[i][j])
                        except:
                            pass
                if len(kernel) == kernel_size:
                    result_row.append(max(kernel))
                current_column += step_hor
            result.append(result_row)
            current_row += step_ver
        return result


# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
# print(MaxPooling.max_pooling(lst, 2, 2, 2, 2))
# lst = [4,4 ,5 ,5,1, 3, "dfdsfd", True, None]
# filtered = filter(lambda x: (type(x) in (int, float)), lst)
# print(list(filtered))
# print(len(filtered))

