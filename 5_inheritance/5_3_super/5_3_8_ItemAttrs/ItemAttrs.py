class ItemAttrs:

    def __getitem__(self, item):
        return list(self.__dict__.items())[item][1]

    def __setitem__(self, key, value):
        setattr(self, list(self.__dict__.items())[key][0], value)


class Point(ItemAttrs):

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]
print(x, y)
pt[0] = 10
print(pt[0])