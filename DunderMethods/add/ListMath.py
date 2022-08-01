from typing import Any


class ListMath:

    def __init__(self, lst=None) -> None:
        self.lst_math = self.get_only_numbers(lst) if lst and type(lst) == list else []

    @staticmethod
    def get_only_numbers(lst: list) -> list:
        return [el for el in lst if type(el) in (int, float)]

    @staticmethod
    def is_number(value: Any):
        if type(value) not in (int, float):
            raise ValueError("Value is not a number")

    def __add__(self, other: float):
        self.is_number(other)
        return ListMath([el + other for el in self.lst_math])

    def __radd__(self, other: float):
        self.is_number(other)
        return self + other

    def __iadd__(self, other: float):
        self.is_number(other)
        for i in range(len(self.lst_math)):
            self.lst_math[i] += other
        return self

    def __sub__(self, other: float):
        self.is_number(other)
        return ListMath([el - other for el in self.lst_math])

    def __rsub__(self, other: float):
        self.is_number(other)
        return ListMath([other - el for el in self.lst_math])

    def __isub__(self, other: float):
        self.is_number(other)
        for i in range(len(self.lst_math)):
            self.lst_math[i] -= other
        return self

    def __mul__(self, other: float):
        self.is_number(other)
        return ListMath([el * other for el in self.lst_math])

    def __rmul__(self, other: float):
        self.is_number(other)
        return self * other

    def __imul__(self, other: float):
        self.is_number(other)
        for i in range(len(self.lst_math)):
            self.lst_math[i] *= other
        return self

    def __truediv__(self, other: float):
        self.is_number(other)
        return ListMath([el / other for el in self.lst_math])

    def __rtruediv__(self, other: float):
        self.is_number(other)
        return self / other

    def __itruediv__(self, other: float):
        self.is_number(other)
        for i in range(len(self.lst_math)):
            self.lst_math[i] /= other
        return self

lst = ListMath([1, "abc", -5, 7.68, True])
lst -= 76
# print(summ.lst_math)
print(lst.lst_math)






