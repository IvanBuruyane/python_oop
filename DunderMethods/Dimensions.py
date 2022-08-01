from typing import Any


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a: [int, float], b: [int, float], c: [int, float]) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if (key in ("a", "b", "c", "_Dimensions__a", "_Dimensions__b", "_Dimensions__c")) \
                and (value < self.MIN_DIMENSION or value > self.MAX_DIMENSION):
            return
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)

    @property
    def a(self) -> [int, float]:
        return self.__a

    @a.setter
    def a(self, value: Any) -> None:
        self.__a = value

    @property
    def b(self) -> [int, float]:
        return self.__b

    @b.setter
    def b(self, value: Any) -> None:
        self.__b = value

    @property
    def c(self) -> [int, float]:
        return self.__c

    @c.setter
    def c(self, value: Any) -> None:
        self.__c = value

d = Dimensions(10.5, 20.1, 30)
print(d.__dict__)
d.a = 8
d.b = 15
print(d.__dict__)
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b, c)
# d.MAX_DIMENSION = 10  # исключение AttributeError