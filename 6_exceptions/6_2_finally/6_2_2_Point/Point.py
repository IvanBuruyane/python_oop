class Point:

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

lst = input().split()

try:
    x, y = map(int, lst)
    pt = Point(x, y)
except:
    try:
        x, y = map(float, lst)
        pt = Point(x, y)
    except:
        _sum = "".join(lst)
        pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")