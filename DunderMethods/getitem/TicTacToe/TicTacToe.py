class Cell:

    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self) -> bool:
        return self.is_free

    def __str__(self):
        return str(self.value)


class TicTacToe:

    def __init__(self) -> None:
        self.pole = [[Cell() for i in range(3)] for j in range(3)]

    @staticmethod
    def is_iterable(obj) -> bool:
        try:
            iter(obj)
            return True
        except:
            return False

    @staticmethod
    def get_start_stop_from_slice(slc: slice, iterr) -> tuple:
        start = slc.start if slc.start else 0
        stop = slc.stop if slc.stop else len(iterr)
        step = slc.step if slc.step else 1
        return start, stop, step

    def clear(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

    def check_index(self, indx: int) -> None:
        for ind in indx:
            if type(ind) not in (int, slice):
                raise IndexError('неверный индекс клетки')
            if type(ind) is int and (ind < 0 or ind > 2):
                raise IndexError('неверный индекс клетки')
            if type(ind) is slice and ((ind.start is not None and ind.start > 2) or
                                       (ind.stop is not None and ind.stop > 2) or
                                       (ind.step is not None and ind.step > 2)):
                raise IndexError('неверный индекс клетки')

    def __getitem__(self, item: int):
        self.check_index(item)
        row = item[0]
        column = item[1]
        if type(row) is int:
            res = self.pole[row][column]
        elif type(row) is slice:
            start, stop, step = self.get_start_stop_from_slice(row, self.pole)
            res = []
            for i in range(start, stop, step):
                res.append(self.pole[i][column])
        if self.is_iterable(res):
            return tuple([cell.value for cell in res])
        else:
            return res.value

    def __setitem__(self, key: int, value: int) -> None:
        self.check_index(key)
        self.pole[key[0]][key[1]].value = value

    def __str__(self):
        res = ""
        for i in range(3):
            row = ""
            for j in range(3):
                row += str(self.pole[i][j].value) + " "
            res += "\n" + row
        return res

game = TicTacToe()
game.clear()
print(type(game[0, 0]))
game[0, 0] = 1
game[1, 0] = 2
print(game)
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
[print(cell.value, end=" ") for cell in v1]
print()
[print(cell.value, end=" ") for cell in v2]
