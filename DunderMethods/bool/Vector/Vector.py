class Vector:

    def __init__(self, *coords) -> None:
        self.coords = coords

    @staticmethod
    def check_dim_equal(vector1, vector2) -> None:
        if len(vector1.coords) != len(vector2.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        # if type(other) in (int, float):
        #     return Vector(*tuple(map(lambda x: x + other, self.coords)))
        # if type(other) is Vector:
        #     self.check_dim_equal(self, other)
        #     return Vector(*tuple(map(lambda x, y: x + y, self.coords, other.coords)))
        self.math_operation(self, other, "add")

    # def __radd__(self, other):
    #     return self + other

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.coords = tuple(map(lambda x: x + other, self.coords))
        if type(other) is Vector:
            self.check_dim_equal(self, other)
            self.coords = tuple(map(lambda x, y: x + y, self.coords, other.coords))
        return self

    def __sub__(self, other):
        if type(other) in (int, float):
            return Vector(*tuple(map(lambda x: x - other, self.coords)))
        if type(other) is Vector:
            self.check_dim_equal(self, other)
            return Vector(*tuple(map(lambda x, y: x - y, self.coords, other.coords)))

    def __isub__(self, other):
        if type(other) in (int, float):
            self.coords = tuple(map(lambda x: x - other, self.coords))
        if type(other) is Vector:
            self.check_dim_equal(self, other)
            self.coords = tuple(map(lambda x, y: x - y, self.coords, other.coords))
        return self

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(*tuple(map(lambda x: x * other, self.coords)))
        if type(other) is Vector:
            self.check_dim_equal(self, other)
            return Vector(*tuple(map(lambda x, y: x * y, self.coords, other.coords)))

    def __imul__(self, other):
        if type(other) in (int, float):
            self.coords = tuple(map(lambda x: x * other, self.coords))
        if type(other) is Vector:
            self.check_dim_equal(self, other)
            self.coords = tuple(map(lambda x, y: x * y, self.coords, other.coords))
        return self

    def __eq__(self, other):
        for i in range(len(self.coords)):
            if self.coords[i] != other.coords[i]:
                return False
        return True

    @staticmethod
    def math_operation(self, other, operation):
        operations = {
            "add": [lambda x: x + other, lambda x, y: x + y],
            "sub": [lambda x: x - other, lambda x, y: x - y],
            "mul": [lambda x: x * other, lambda x, y: x + y]
        }
        if operation[0] == "i":
            if type(other) in (int, float):
                self.coords = tuple(map(lambda x: x + other, self.coords))
            if type(other) is Vector:
                self.check_dim_equal(self, other)
                self.coords = tuple(map(lambda x, y: x + y, self.coords, other.coords))
            return self
        else:
            if type(other) in (int, float):
                return Vector(*tuple(map(operations[operation[1:]][0], self.coords)))
            if type(other) is Vector:
                self.check_dim_equal(self, other)
                return Vector(*tuple(map(operations[operation[1:]][1], self.coords, other.coords)))




v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True


