class Point:

    def __init__(self, x: int, y: int, color: str = "black") -> None:
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1000):
    if i == 1:
        points.append(Point(2 * i + 1, 2* i + 1, "yellow"))
    else:
        points.append(Point(2 * i + 1, 2 * i + 1))

print(points)
