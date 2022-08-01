from typing import ClassVar


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: [int, float] = 0, y: [int, float] = 0) -> None:
        if self.is_valid(x):
            self.__x = x
        if self.is_valid(y):
            self.__y = y

    @classmethod
    def is_valid(cls, x):
        return type(x) in [int, str] and cls.MIN_COORD <= x <= cls.MAX_COORD

    @property
    def x(self) -> [int, float]:
        return self.__x

    @x.setter
    def x(self, x: [int, float]) -> None:
        if self.is_valid(x):
            self.__x = x

    @property
    def y(self) -> [int, float]:
        return self.__y

    @y.setter
    def y(self, y: [int, float]) -> None:
        if self.is_valid(y):
            self.__y = y

    @staticmethod
    def norm2(vector: ClassVar) -> [int, float]:
        return vector.x ** 2 + vector.y ** 2

