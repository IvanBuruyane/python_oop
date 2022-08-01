from typing import Any, Union


class CellException(Exception):
    """Base cass for cell exceptions"""

    def __str__(self):
        raise NotImplemented


class CellIntegerException(CellException):

    def __str__(self) -> str:
        return 'значение выходит за допустимый диапазон'


class CellFloatException(CellException):

    def __str__(self) -> str:
        return 'значение выходит за допустимый диапазон'


class CellStringException(CellException):

    def __str__(self) -> str:
        return 'длина строки выходит за допустимый диапазон'


class Cell:

    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._is_valid(value)
        self._value = value

    def _is_valid(self, value) -> None:
        raise NotImplemented


class CellInteger(Cell):

    def __init__(self, min_value: int, max_value: int) -> None:
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, value: int) -> None:
        if type(value) is not int or not self._min_value <= value <= self._max_value:
            raise CellIntegerException


class CellFloat(CellInteger):

    def _is_valid(self, value: float) -> None:
        if type(value) not in (int, float) or not self._min_value <= value <= self._max_value:
            raise CellFloatException


class CellString(Cell):

    def __init__(self, min_length: int, max_length: int) -> None:
        super().__init__()
        self._min_length = min_length
        self._max_length = max_length

    def _is_valid(self, value: str) -> None:
        if type(value) is not str or not self._min_length <= len(value) <= self._max_length:
            raise CellStringException


class TupleData:

    def __init__(self, *args) -> None:
        for arg in args:
            if type(arg) not in (CellInteger, CellString, CellFloat):
                raise ValueError
        self.__cells = list(args)

    def __check_index(self, indx: int) -> None:
        if type(indx) is not int or not 0 <= indx <= len(self.__cells) - 1:
            raise IndexError

    def __getitem__(self, item: int) -> Union[CellString, CellFloat, CellInteger]:
        self.__check_index(item)
        return self.__cells[item]

    def __setitem__(self, key: int, value: int) -> None:
        self.__check_index(key)
        self.__cells[key].value = value

    def __len__(self) -> int:
        return len(self.__cells)

    def __iter__(self) -> None:
        self.__counter = 0
        self.__current_value = self.__cells[self.__counter].value
        return self

    def __next__(self):
        if self.__counter < len(self.__cells):
            res = self.__current_value
            self.__counter += 1
            if self.__counter < len(self.__cells):
                self.__current_value = self.__cells[self.__counter].value
            return res
        else:
            raise StopIteration


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
else:
    print("OK")





