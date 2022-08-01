from typing import Any


class Circle:

    def __init__(self, x: [int, float], y: [int, float], radius: [int, float]) -> None:
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self) -> [int, float]:
        return self.__x

    @x.setter
    def x(self, value: [int, float]) -> None:
        self.__x = value

    @property
    def y(self) -> [int, float]:
        return self.__y

    @y.setter
    def y(self, value: [int, float]) -> None:
        self.__y = value

    @property
    def radius(self) -> [int, float]:
        return self.__radius

    @radius.setter
    def radius(self, value: [int, float]) -> None:
        self.__radius = value

    @staticmethod
    def is_number(number: Any) -> bool:
        return type(number) in [int, float]

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if (key in ("x", "y", "radius", "_Circe__x", "_Circle__y", "_Circle__radius") and not self.is_number(value)) \
                or (key == "_Circle__radius" and value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == "radius" and value <= 0:
            return object.__setattr__(self, key, self.__radius)
        object.__setattr__(self, key, value)

circle = Circle(10.5, 7, 22)
print(circle.__dict__)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
print(circle.__dict__)
x, y = circle.x, circle.y
res = circle.name
print(circle.radius)
print(x, y)
print(res)
circle2 = Circle(10, 2, 0)
print(circle2.__dict__)



