class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def clone(self):
        copy = super().__new__(Point)
        for attr in self.__dict__:
            setattr(copy, attr, self.__dict__[attr])
        return copy


pt = Point(4343, 3434.343)
pt_clone = pt.clone()
print(pt.__dict__)
print(pt_clone.__dict__)