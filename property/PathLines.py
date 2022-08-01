class LineTo:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.__start = (0, 0)

    @property
    def start(self) -> ():
        return self.__start

    @start.setter
    def start(self, start: ()) -> None:
        self.__start = start

    def get_length(self) -> float:
        return ((self.x - self.__start[0]) ** 2 + (self.y - self.__start[1]) ** 2) ** 0.5


class PathLines:

    def __init__(self, *args) -> None:
        lines_count = len(args)
        self.route = list(args)
        if lines_count > 1:
            for i in range(1, lines_count):
                self.route[i].start = (self.route[i - 1].x, self.route[i - 1].y)

    def get_path(self) -> list:
        return self.route

    def add_line(self, line: LineTo) -> None:
        self.route.append(line)
        if len(self.route) > 1:
            self.route[-1].start = (self.route[-2].x, self.route[-2].y)

    def get_length(self) -> float:
        length = 0
        for line in self.route:
            length += line.get_length()
        return length

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
[print(line.start) for line in p.route]
print(dist)

