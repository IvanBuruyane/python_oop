from copy import copy
from random import randint, choice, seed


class CollisionError(Exception):
    pass


class OutOfPoleError(Exception):
    pass


class Ship:

    def __init__(self, length: int, tp: int = 1, x: int = None, y: int = None) -> None:
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for i in range(self._length)]
        self.coords = self._calculate_coords() if self._x is not None and self._y is not None else []

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def _calculate_coords(self) -> list:
        return [(self._x + i, self._y) for i in range(self._length)] if self._tp == 1 \
            else [(self._x, self._y + i) for i in range(self._length)]

    def set_start_coords(self, x: int, y: int) -> None:
        """Set coords of the first cell of the ship"""
        self._x = x
        self._y = y
        self.coords = self._calculate_coords()

    def get_start_coords(self) -> tuple:
        """Get coords of the first cell of the ship"""
        return self._x, self._y

    def move(self, go: int) -> None:
        """Move ship to the 'go' cells forward/backward"""
        if self._is_move:
            x, y = self.get_start_coords()
            if self._tp == 1:
                self.set_start_coords(x + go, y)
            elif self._tp == 2:
                self.set_start_coords(x, y + go)
            self.is_out_pole()


    def is_collide(self, ship) -> bool:
        """Return true if self ship collides another ship"""
        flag = False
        cells_around_ship = self.get_cells_around()
        for cell in ship.coords:
            if cell in cells_around_ship:
                flag = True
                break
        return flag

    def get_cells_around(self) -> list:
        """Get coordinates of all cell around the ship + coordinates of the ship"""
        x, y = self.get_start_coords()
        res = []
        if self._tp == 1:
            res.append((x - 1, y))
            res.extend(self.coords)
            res.append((x + self._length, y))
            center = copy(res)
            res.extend([(el[0], el[1] + 1) for el in center])
            res.extend([(el[0], el[1] - 1) for el in center])
        elif self._tp == 2:
            res.append((x, y - 1))
            res.extend(self.coords)
            res.append((x, y + self._length))
            center = copy(res)
            res.extend([(el[0] + 1, el[1]) for el in center])
            res.extend([(el[0] - 1, el[1]) for el in center])
        i = 0
        while i < len(res):
            cell = res[i]
            if not 0 <= cell[0] < 10 or not 0 <= cell[1] < 10:
                res.remove(cell)
                i -= 1
            i += 1
        return res

    def is_out_pole(self, size=10):
        """Return true if any cell of the ship is out of game pole"""
        flag = False
        for cell in self.coords:
            if not 0 <= cell[0] < size or not 0 <= cell[1] < size:
                flag = True
                break
        return flag


class GamePole:

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._ships = []
        self._free_cells = [(i // size, i % size) for i in range(size * size)]

    def init(self) -> None:
        """Create ships and position them on the game pole"""
        self._ships = [Ship(4, tp=randint(1, 2)),
                       Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)),
                       ]
        for ship in self._ships:
            self._position_ship(ship)

    def get_ships(self) -> list:
        return self._ships

    def _get_occupied_cells(self) -> list:
        """Get all cells of the pole that is occupied by ships"""
        occupied_cells = []
        for ship in self._ships:
            occupied_cells.extend(ship.coords)
        return occupied_cells

    def _position_ship(self, ship: Ship) -> None:
        """Position ship in the free cells"""
        free_cells = copy(self._free_cells)
        positioned_ships = [shp for shp in self._ships if shp.get_start_coords()[0] is not None
                            and shp.get_start_coords()[1] is not None]
        while True:
            ch = choice(free_cells)
            try:
                x, y = ch
                ship.set_start_coords(x, y)
                if ship.is_out_pole():
                    raise OutOfPoleError
                for pos_ship in positioned_ships:
                    if ship.is_collide(pos_ship):
                        raise CollisionError
            except:
                free_cells.remove(ch)
            else:
                occupied_cells = ship.get_cells_around()
                for cell in occupied_cells:
                    try:
                        self._free_cells.remove(cell)
                    except:
                        continue
                break

    def get_pole(self) -> tuple:
        """Get list representation of the game pole"""
        res = []
        occupied_cells = self._get_occupied_cells()
        for i in range(self._size):
            row = ()
            for j in range(self._size):
                value = 1 if (i, j) in occupied_cells else 0
                row = row + (value,)
            res.append(row)
        return tuple(res)

    def show(self) -> None:
        """Pring game pole in the console"""
        pole = list(map(list, self.get_pole()))
        for i in range(self._size):
            for j in range(self._size):
                print(pole[i][j], end=" ")
            print()

    def _is_collide_others(self, ship: Ship) -> None:
        """Check if given ship collides any other ship"""
        for another_ship in self._ships:
            if ship.get_start_coords() != another_ship.get_start_coords():
                if ship.is_collide(another_ship):
                    raise CollisionError

    def move_ships(self) -> None:
        """Move all ships for 1/-1 cell forward/backward"""
        go = choice([-1, 1])
        for ship in self._ships:
            try:
                ship.move(go)
                if ship.is_out_pole():
                    raise OutOfPoleError
                self._is_collide_others(ship)
            except:
                try:
                    ship.move(-go)
                    if ship.is_out_pole():
                        raise OutOfPoleError
                    self._is_collide_others(ship)
                except:
                    pass



SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
print(pole.get_pole())
pole.show()

pole.move_ships()
print()
pole.show()

# print(Ship(4, 1, 0, 0).is_collide(Ship(3, 2, 0, 2)))

# sp = Ship(4, 1, 3, 3)
# sp2 = Ship(1, 1, 8, 2)
# sp.move(1)
# sp.move(1)
# sp.move(1)
# print(sp._coords)
# sp.is_out_pole()
# sp = Ship(4, 1)
# sp._x = 3
# print(sp._coords)
# sp._y = 4
# print(sp._coords)
# sp.set_start_coords(3, 4)
# print(sp._coords)
