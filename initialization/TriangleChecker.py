class TriangleChecker:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0 or not isinstance(self.a, int) or not isinstance(self.b, int) \
                or not isinstance(self.c, int):
            return 1
        elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())
