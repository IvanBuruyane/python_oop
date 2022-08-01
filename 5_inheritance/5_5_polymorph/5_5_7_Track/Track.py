from typing import Any


class PointTrack:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def __is_number(value) -> None:
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')

    def __setattr__(self, key, value):
        if key in ("x", "y"):
            self.__is_number(value)
        super().__setattr__(key, value)

    def __str__(self) -> str:
        return f"PointTrack: {self.x}, {self.y}"


class Track:

    def __init__(self, *args) -> None:
        if len(args) == 2 and type(args[0]) in (int, float) and type(args[1]) in (int, float):
            x, y = args
            self.__points: list = [PointTrack(x, y)]
        elif self.__all_points(args):
            self.__points = list(args)

    @staticmethod
    def __all_points(args: tuple) -> bool:
        for arg in args:
            if type(arg) is not PointTrack:
                return False
        return True

    @property
    def points(self) -> tuple:
        return tuple(self.__points)

    def add_back(self, pt: PointTrack) -> None:
        self.__points.append(pt)

    def add_front(self, pt: PointTrack) -> None:
        self.insert_in_list(pt, self.__points, 0)

    def pop_back(self) -> None:
        self.__points.pop(-1)

    def pop_front(self) -> None:
        self.__points.pop(0)

    @staticmethod
    def insert_in_list(obj: Any, lst: list, position: int) -> None:
        length: int = len(lst)
        if position > length or position < 0:
            raise IndexError
        if position == length:
            lst.append(obj)
        else:
            lst.append(None)
            for i in range(-1, -(length - position + 1), -1):
                lst[i] = lst[i - 1]
            lst[-(length - position + 1)] = obj

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)