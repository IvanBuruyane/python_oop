class Track:

    def __init__(self, start_x: float, start_y: float) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.__segments = []

    def check_index(self, index) -> None:
        if type(index) is not int or (index < 0 or index >= len(self.__segments)):
            raise IndexError('некорректный индекс')

    def add_point(self, x: float, y: float, speed: float) -> None:
        self.__segments.append([(x, y), speed])

    def __getitem__(self, item: int) -> tuple:
        self.check_index(item)
        return self.__segments[item][0], self.__segments[item][1]

    def __setitem__(self, key: int, value: float) -> None:
        self.check_index(key)
        self.__segments[key][1] = value

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]

