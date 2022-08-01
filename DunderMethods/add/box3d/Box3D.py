class Box3D:

    def __init__(self, width: float, height: float, depth: float) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    @staticmethod
    def is_type_correct(value):
        if type(value) not in (Box3D, float, int):
            raise ValueError("Incorrect type")

    def __add__(self, other):
        self.is_type_correct(other)
        if type(other) is Box3D:
            args: list = [self.width + other.width, self.height + other.height, self.depth + other.depth]
        elif type(other) in (float, int):
            args = [self.width + other, self.height + other, self.depth + other]
        return Box3D(*args)

    def __radd__(self, other):
        self.is_type_correct(other)
        return self + other

    def __mul__(self, other):
        self.is_type_correct(other)
        if type(other) is Box3D:
            args: list = [self.width * other.width, self.height * other.height, self.depth * other.depth]
        elif type(other) in (float, int):
            args = [self.width * other, self.height * other, self.depth * other]
        return Box3D(*args)

    def __rmul__(self, other):
        self.is_type_correct(other)
        return self * other

    def __sub__(self, other):
        self.is_type_correct(other)
        if type(other) is Box3D:
            args: list = [self.width - other.width, self.height - other.height, self.depth - other.depth]
        elif type(other) in (float, int):
            args = [self.width - other, self.height - other, self.depth - other]
        return Box3D(*args)

    def __floordiv__(self, other):
        if type(other) not in (int, float):
            raise ValueError("Incorrect type for the floordiv")
        args = [self.width // other, self.height // other, self.depth // other]
        return Box3D(*args)

    def __mod__(self, other):
        if type(other) not in (int, float):
            raise ValueError("Incorrect type for the floordiv")
        args = [self.width % other, self.height % other, self.depth % other]
        return Box3D(*args)


