from math import sqrt


class Line:

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __len__(self) -> float:
        return int(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))

