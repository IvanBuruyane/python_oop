import math


class Sides:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.raise_error_if_not_positive(value)
        instance.__dict__[self.name] = value

    @staticmethod
    def raise_error_if_not_positive(value) -> None:
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")


class Triangle:

    a = Sides()
    b = Sides()
    c = Sides()

    def __init__(self, a: float, b: float, c: float) -> None:
        if a > b + c or b > a + c or c > a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

tr = Triangle(3, 4, 5)
print(tr())
print(tr.__dict__)