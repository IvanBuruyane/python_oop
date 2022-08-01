from typing import Any, Union


class Money:

    def __init__(self, value: Union[int, float]) -> None:
        self._money: Union[int, float] = value

    @staticmethod
    def is_number(value: Any) -> None:
        if type(value) not in (float, int):
            raise TypeError('сумма должна быть числом')

    @property
    def money(self) -> float:
        return self._money

    @money.setter
    def money(self, value: Union[int, float]) -> None:
        self._money = value

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "_money":
            self.is_number(value)
        super().__setattr__(key, value)


class MoneyOperators:

    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"

m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
print(m)
m = m1 + m2