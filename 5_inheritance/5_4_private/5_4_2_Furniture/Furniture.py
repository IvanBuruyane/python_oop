class Furniture:

    def __init__(self, name: str, weight: float) -> None:
        self._name = name
        self._weight = weight

    @staticmethod
    def __verify_name(name: str) -> None:
        if type(name) is not str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight: float) -> None:
        if type(weight) not in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(value)
        elif key == "_weight":
            self.__verify_weight(value)
        super().__setattr__(key, value)

    def get_attrs(self) -> tuple:
        return tuple(self.__dict__.values())


class Closet(Furniture):

    def __init__(self, name: str, weight: float, tp: bool, doors: int) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):

    def __init__(self, name: str, weight: float, height: float) -> None:
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):

    def __init__(self, name: str, weight: float, height: float, square: float) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square

cl = Closet('шкаф-купе', 342.56, True, 3)
print(cl.__dict__)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
# fr = Furniture(10, 10)
# fr._name = 11
print(tb.get_attrs())