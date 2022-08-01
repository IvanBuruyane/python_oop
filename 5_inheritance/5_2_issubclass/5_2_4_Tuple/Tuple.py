from typing import Any


class Tuple:

    def __init__(self, iter_obj) -> None:
        self.obj = tuple(iter_obj)

    @staticmethod
    def is_iterable(obj: Any) -> bool:
        try:
            iter(obj)
            return True
        except:
            return False

    def __add__(self, other):
        if not self.is_iterable(other):
            raise ValueError("Only iterable object can be added to the Tuple")
        return Tuple(self.obj + tuple(other))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t.obj)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t.obj)

