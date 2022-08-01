from typing import Any


class Record:

    def __init__(self, **fields) -> None:
        for key in fields:
            setattr(self, key, fields[key])

    def __getitem__(self, item: int) -> Any:
        self.__check_index(item)
        return self.__dict__[self.__dir__()[item]]

    def __setitem__(self, key: int, value: Any) -> None:
        self.__check_index(key)
        attrib = self.__dir__()[key]
        setattr(self, attrib, value)

    def __check_index(self, indx: int) -> None:
        if type(indx) is not int or (indx < 0 or indx >= len(self.__dict__)):
            raise IndexError('неверный индекс поля')

r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[2])
r[3] # генерируется исключение IndexError