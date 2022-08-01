import math


class PolyLine:

    def __init__(self, *args) -> None:
        self.points = list(args)

    def add_coord(self, x: int, y: int) -> None:
        self.points.append((x, y))

    def remove_coord(self, indx: int) -> None:
        self.points.pop(indx)

    def get_coords(self) -> list:
        return self.points

    @staticmethod
    def distance_between_points(start: tuple, finish: tuple) -> float:
        return math.sqrt((finish[0] - start[0]) + (finish[1] - start[1]))

    def get_total_distance(self) -> float:
        total_distance: float = 0
        for i in range(len(self.points) - 1):
            total_distance += self.distance_between_points(self.points[i + 1], self.points[i])
        return total_distance
