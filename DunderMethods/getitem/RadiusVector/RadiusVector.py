class RadiusVector:

    def __init__(self, *coords) -> None:
        self.coords = list(coords)

    def __getitem__(self, item):
        res = self.coords[item]
        if self.is_iterable(res):
            return tuple(self.coords[item])
        else:
            return res

    @staticmethod
    def is_iterable(obj) -> bool:
        try:
            iter(obj)
            return True
        except:
            return False

    def __setitem__(self, key, value):
        if type(key) is int:
            self.coords[key] = value
        if type(key) is slice:
            start = key.start if key.start else 0
            stop = key.stop if key.stop else len(self.coords)
            step = key.step if key.step else 1
            j = 0
            for i in range(start, stop, step):
                self.coords[i] = value[j]
                j += 1


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5