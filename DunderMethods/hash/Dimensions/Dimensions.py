class Dimensions:

    def __init__(self, a: float, b: float, c: float) -> int:
        for value in (a, b, c):
            self.raise_error_if_not_positive(value)
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    def __gt__(self, other):
        return hash(self) > hash(other)

    @staticmethod
    def raise_error_if_not_positive(value) -> None:
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")


# lst_dims = sorted([Dimensions(*list(map(float, line.split()))) for line in input().split(";")])
# print(list(map(hash, lst_dims)))

d = Dimensions(0, 343, 41)