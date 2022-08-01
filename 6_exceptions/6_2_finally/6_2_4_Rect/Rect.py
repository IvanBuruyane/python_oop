class Rect:

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __is_number(self, value) -> None:
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __is_positive_number(self, value) -> None:
        self.__is_number(value)
        if value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __setattr__(self, key, value):
        if key in ("_x", "_y"):
            self.__is_number(value)
        if key in ("_width", "_height"):
            self.__is_positive_number(value)
        super().__setattr__(key, value)

    def is_collision(self, rect):
        x1_left, y1_top = self._x, self._y
        x1_right, y1_bottom = self.__get_bottom_rigth_coords()
        x2_left, y2_top = rect._x, rect._y
        x2_right, y2_bottom = rect.__get_bottom_rigth_coords()
        if not (x1_left > x2_right or x2_left > x1_right or y1_top < y2_bottom or y2_top < y1_bottom):
            raise TypeError('прямоугольники пересекаются')

    def __get_bottom_rigth_coords(self) -> tuple:
        return self._x + self._width, self._y - self._height


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1)
]

lst_not_collision = []
for i in range(len(lst_rect)):
    intersects: int = 0
    for j in range(len(lst_rect)):
        if i == j:
            continue
        try:
            _one = lst_rect[i]
            _two = lst_rect[j]
            _one.is_collision(_two)
        except:
            intersects += 1
            break
    if not intersects:
        lst_not_collision.append(lst_rect[i])

print(lst_not_collision)


