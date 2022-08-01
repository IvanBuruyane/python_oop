class Triangle:

    def __init__(self, a: float, b: float, c: float) -> None:
        self._a = a
        self._b = b
        self._c = c
        self.__check_triangle(a, b, c)

    @staticmethod
    def __check_triangle(a: float, b: float, c: float) -> None:
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    @staticmethod
    def __is_positive_number(value) -> None:
        if type(value) not in (int, float) or value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

    def __setattr__(self, key, value):
        if key in ("_a", "_b", "_c"):
            self.__is_positive_number(value)
        super().__setattr__(key, value)

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for inp in input_data:
    try:
        lst_tr.append(Triangle(*inp))
    except Exception as e:
        pass
print(lst_tr)
