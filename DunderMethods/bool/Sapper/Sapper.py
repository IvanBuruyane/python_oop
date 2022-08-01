import random


class Cell:

    def __init__(self) -> None:
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @staticmethod
    def check_type(value, tp) -> None:
        if type(value) is not tp:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        self.check_type(value, bool)
        self.__is_mine = value

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        self.check_type(value, int)
        if value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        self.check_type(value, bool)
        self.__is_open = value

    def __bool__(self) -> bool:
        return not self.is_open


class GamePole:

    __POLE = None

    def __new__(cls, *args, **kwargs):
        if cls.__POLE is None:
            cls.__POLE = super().__new__(cls)
        return cls.__POLE

    @staticmethod
    def generate_mines(n: int, m: int, total_mines: int) -> list:
        total_cells: int = n * m
        mines: list = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            if not total_mines:
                break
            for j in range(m):
                if not total_mines:
                    break
                probability: float = total_mines / total_cells
                mine: bool = True if random.random() <= probability else False
                if mine:
                    mines[i][j] = mine
                    total_mines -= 1
                total_cells -= 1
        return mines

    @staticmethod
    def generate_around_mines(mines: list) -> list:
        n: int = len(mines)
        m: int = len(mines[0])
        around_mines = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                count = 0
                around_cells = [
                    (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                    (i, j - 1), (i, j + 1),
                    (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                ]
                for cell in around_cells:
                    if cell[0] < 0 or cell[0] > n - 1 or cell[1] < 0 or cell[1] > m - 1:
                        continue
                    if mines[cell[0]][cell[1]]:
                        count += 1
                around_mines[i][j] = count
        return around_mines

    def __init__(self, n: int, m: int, total_mines: int) -> None:
        self.__pole_cells = []
        self.__mines = None
        self.__around_mines = None
        self.__n = n
        self.__m = m
        self.__total_mines = total_mines

    @property
    def pole(self) -> list:
        return self.__pole_cells

    def init_pole(self) -> None:
        n: int = self.__n
        m: int = self.__m
        total_mines: int = self.__total_mines
        total_cells: int = n * m
        if total_mines > total_cells:
            raise ValueError("Number of mines can't be > than number of cells")
        self.__mines = self.generate_mines(n, m, total_mines)
        self.__around_mines = self.generate_around_mines(self.__mines)
        for i in range(n):
            row = []
            for j in range(m):
                row.append(Cell())
                if self.__mines[i][j]:
                    row[-1].is_mine = True
                else:
                    row[-1].number = self.__around_mines[i][j]
            self.__pole_cells.append(row)

    def open_cell(self, i: int, j: int) -> None:
        if i < 0 or i > self.__n or j < 0 or j > self.__m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def count_mines(self) -> int:
        count: int = 0
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__mines[i][j]:
                    count += 1
        return count

    def show_pole(self) -> None:
        for row in self.__pole_cells:
            for cell in row:
                if not cell:
                    if cell.is_mine:
                        print("!", end=" ")
                    else:
                        print(cell.number, end=" ")
                else:
                    print("#", end=" ")
            print()



pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
[[pole.open_cell(i, j) for j in range(20)] for i in range(10)]
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
