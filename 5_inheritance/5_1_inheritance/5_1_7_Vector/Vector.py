class Vector:

    def __init__(self, *coords) -> None:
        self.coords = list(coords)

    @staticmethod
    def check_if_vector_len_equal(v1, v2) -> None:
        if not (type(v1) == type(v2) == list) or len(v1) != len(v2):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self) -> tuple:
        return tuple(self.coords)

    def __add__(self, other):
        self.check_if_vector_len_equal(self.coords, other.coords)
        return Vector(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other):
        self.check_if_vector_len_equal(self.coords, other.coords)
        return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])


class VectorInt(Vector):

    def __init__(self, *coords) -> None:
        self.__validate_coords(coords)
        super().__init__(*coords)

    def __validate_coords(self, coords: tuple) -> None:
        if not self.__all_coords_int(coords):
            raise ValueError('координаты должны быть целыми числами')

    @staticmethod
    def __all_coords_int(coords: tuple) -> bool:
        for coord in coords:
            if type(coord) is not int:
                return False
        return True

    def __add__(self, other):
        res = super().__add__(other)
        if self.__all_coords_int(res.coords):
            return VectorInt(*res.coords)
        else:
            return res

    def __sub__(self, other):
        res = super().__sub__(other)
        if self.__all_coords_int(res.coords):
            return VectorInt(*res.coords)
        else:
            return res


v = VectorInt(1, 2, 3, 4)
v2 = Vector(5, 6, 7.4, 8)
# v1 = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
summ = v + v2
print(type(summ), summ.coords)


