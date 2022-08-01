from typing import Any


class ListInteger(list):

    def __init__(self, args):
        for arg in args:
            self.is_int(arg)
        super().__init__(args)

    def __setitem__(self, key: int, value: int) -> None:
        self.is_int(value)
        super().__setitem__(key, value)

    def append(self, obj: int) -> None:
        self.is_int(obj)
        super().append(obj)

    @staticmethod
    def is_int(val: Any) -> None:
        if type(val) is not int:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5