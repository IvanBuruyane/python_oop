import random
from typing import List


class Cell:

    def __init__(self, around_mines: int, mine: bool) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    @staticmethod
    def generate_mines(n: int, m: int) -> List[List[bool]]:
        total_cells = n * n
        mines = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            if not m:
                break
            for j in range(n):
                if not m:
                    break
                probability = m / total_cells
                mine = True if random.random() <= probability else False
                if mine:
                    mines[i][j] = mine
                    m -= 1
                total_cells -= 1
        return mines

    @staticmethod
    def generate_around_mines(mines: List[List[bool]]) -> List[List[int]]:
        n = len(mines)
        around_mines = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                count = 0
                around_cells = [
                    (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                    (i, j - 1), (i, j + 1),
                    (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                ]
                for cell in around_cells:
                    if cell[0] < 0 or cell[0] > n - 1 or cell[1] < 0 or cell[1] > n - 1:
                        continue
                    if mines[cell[0]][cell[1]]:
                        count += 1
                around_mines[i][j] = count
        return around_mines

    def __init__(self, n: int, m: int) -> None:
        self.mines = None
        self.around_mines = None
        self.pole = None
        self.n = n
        self.m = m

    def init(self) -> None:
        n = self.n
        m = self.m
        total_cells = n * n
        if m > total_cells:
            raise ValueError("Number of mines can't be > than number of cells")
        self.mines = self.generate_mines(n, m)
        self.around_mines = self.generate_around_mines(self.mines)
        self.pole = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(Cell(self.around_mines[i][j], self.mines[i][j]))
            self.pole.append(row)

    def count_mines(self) -> int:
        length = len(self.mines)
        count = 0
        for i in range(length):
            for j in range(length):
                if self.mines[i][j]:
                    count += 1
        return count

    def show(self) -> None:
        for row in self.pole:
            for cell in row:
                if cell.fl_open:
                    print(cell.around_mines, end=" ")
                elif not cell.fl_open:
                    print("#", end= " ")
            print()



pole = GamePole(5, 5)
pole.init()
[print(row) for row in pole.mines]
print()
[print(row) for row in pole.around_mines]
print()
pole.show()
