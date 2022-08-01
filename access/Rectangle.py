class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:

    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        elif (len(args) == 4 and type(args[0]) in (int, float) and type(args[1]) in (int, float)
              and type(args[2]) in (int, float) and type(args[3]) in (int, float)):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            raise ValueError("Please set 2 Points or coordinates in the following order: x1, y1, x2, y2")

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__ep, self.__sp

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")

rect = Rectangle(0, 0, 20, 34)

rect.draw()