import math

# Descriptor
from typing import Any


class Number:

    @staticmethod
    def is_number(value: float) -> bool:
        return type(value) in (int, float)

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.is_number(value):
            setattr(instance, self.name, value)
        else:
            raise ValueError("Неверный тип данных.")


class Complex:

    # real = Number()
    # img = Number()

    def __init__(self, real: float, img: float) -> None:
        self.__real = real
        self.__img = img

    @property
    def real(self) -> float:
        return self.__real

    @real.setter
    def real(self, value: Any) -> None:
        if Number.is_number(value):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self) -> float:
        return self.__img

    @img.setter
    def img(self, value: Any) -> None:
        if Number.is_number(value):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.img ** 2)


cmp = Complex(7, 8)
cmp.real, cmp.img = 3, 4
c_abs = abs(cmp)
print(cmp.__dict__, c_abs)





