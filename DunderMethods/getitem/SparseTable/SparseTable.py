from typing import Any


class Cell:

    def __init__(self, value: Any) -> None:
        self.value = value


class SparseTable:

    def __init__(self) -> None:
        self.rows: int = 0
        self.cols: int = 0
        self.cells = {}

    def add_data(self, row: int, col: int, data) -> None:
        if row >= self.rows:
            self.rows = row + 1
        if col >= self.cols:
            self.cols = col + 1
        if type(data) is Cell:
            self.cells[(row, col)] = data
        if type(data) is not Cell:
            if self.cells.get((row, col)):
                self.cells[(row, col)].value = data
            else:
                self.cells[(row, col)] = Cell(data)

    def remove_data(self, row: int, col: int) -> None:
        self.check_if_cell_exists(row, col, IndexError('ячейка с указанными индексами не существует'))
        del self.cells[(row, col)]
        if row == self.rows:
            rows: list = [key[0] for key in self.cells]
            self.rows = max(rows)
        if col == self.cols:
            cols: list = [key[1] for key in self.cells]
            self.cols = max(cols)

    def check_if_cell_exists(self, row: int, col: int, er) -> None:
        if not self.cells.get((row, col)):
            raise er

    def __getitem__(self, item: tuple) -> Any:
        row, col = item
        self.check_if_cell_exists(row, col, ValueError('данные по указанным индексам отсутствуют'))
        return self.cells[(row, col)].value

    def __setitem__(self, key: tuple, value: any) -> None:
        row, col = key
        self.add_data(row, col, value)

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError



