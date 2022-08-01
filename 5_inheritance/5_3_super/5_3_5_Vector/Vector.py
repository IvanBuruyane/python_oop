from typing import Callable


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


def integer_params_decorated(func: Callable) -> None:
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if type(arg) is not int:
                raise TypeError("аргументы должны быть целыми числами")
        for value in kwargs.values():
            if type(value) is not int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)
    return wrapper



@integer_params
class Vector:

    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
vector.set_coords((4, 5), reverse=True)

