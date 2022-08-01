from random import choice
from pprint import pprint


class Cell:

    def __init__(self) -> None:
        self.value = 0

    def __bool__(self) -> bool:
        return not self.value


class TicTacToe:

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self) -> None:
        self.pole = [[Cell() for i in range(3)] for j in range(3)]

    def init(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    # @staticmethod
    # def is_iterable(obj) -> bool:
    #     try:
    #         iter(obj)
    #         return True
    #     except:
    #         return False
    #
    # @staticmethod
    # def get_start_stop_from_slice(slc: slice, iterr) -> tuple:
    #     start = slc.start if slc.start else 0
    #     stop = slc.stop if slc.stop else len(iterr)
    #     step = slc.step if slc.step else 1
    #     return start, stop, step
    #
    # def clear(self) -> None:
    #     for row in self.pole:
    #         for cell in row:
    #             cell.value = 0
    #             cell.is_free = True

    def __check_index(self, indx: tuple) -> None:
        row, col = indx
        if type(row) is not int or type(col) is not int or not 0 <= row < 3 or not 0 <= col < 3:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item: tuple) -> int:
        self.__check_index(item)
        row, col = item
        return self.pole[row][col].value

    def __setitem__(self, key: tuple, value: int) -> None:
        self.__check_index(key)
        row, col = key
        self.pole[row][col].value = value

    def __str__(self):
        res = ""
        for i in range(3):
            row = ""
            for j in range(3):
                row += str(self.pole[i][j].value) + " "
            res += "\n" + row
        return res

    def show(self) -> None:
        print(self)

    def __get_free_cells(self) -> list:
        free_cells: list = []
        for i in range(3):
            for j in range(3):
                if self.pole[i][j]:
                    free_cells.append((i, j))
        return free_cells

    def __go(self, is_human: bool = True) -> None:
        free_cells: list = self.__get_free_cells()
        if not free_cells:
            raise ValueError("No free cells to move")
        val: int = self.HUMAN_X if is_human else self.COMPUTER_O
        self[choice(free_cells)] = val

    def human_go(self) -> None:
        self.__go()

    def computer_go(self) -> None:
        self.__go(False)

    def __win(self, is_human: bool = True) -> bool:
        val = self.HUMAN_X if is_human else self.COMPUTER_O
        win_row = [val, val, val]
        rows = [[self.pole[i][j].value for j in range(3)] for i in range(3)]
        cols = [[self.pole[j][i].value for j in range(3)] for i in range(3)]
        diagonals = [[self.pole[i][i].value for i in range(3)], [self.pole[i][2 - i].value for i in range(3)]]
        if win_row in rows or win_row in cols or win_row in diagonals:
            return True
        return False

    @property
    def is_human_win(self) -> bool:
        return self.__win()

    @property
    def is_computer_win(self) -> bool:
        return self.__win(False)

    @property
    def is_draw(self) -> bool:
        if len(self.__get_free_cells()) == 9:
            return False
        return not (self.is_human_win or self.is_computer_win)

    def __bool__(self) -> bool:
        free_cells: list = self.__get_free_cells()
        if (free_cells and self.is_draw) or len(free_cells) == 9:
            return True
        else:
            return False


game = TicTacToe()
pprint(game.__dict__)
game.init()
pprint(game.is_draw)
step_game = 0
game.show()
while game:

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1
    game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")