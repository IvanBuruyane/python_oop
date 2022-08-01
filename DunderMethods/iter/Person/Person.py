from typing import Any


class Person:

    def __init__(self, fio: str, job: str, old: int, salary: float, year_job: int) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def check_indx(self, indx: int) -> None:
        if type(indx) is not int or (indx < 0 or indx > 4):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int) -> Any:
        self.check_indx(item)
        return getattr(self, self.__dir__()[item])

    def __setitem__(self, key: int, value: Any) -> None:
        self.check_indx(key)
        setattr(self, self.__dir__()[key], value)

    def __iter__(self):
        self.__start = 0
        return self

    def __next__(self):
        if self.__start <= 4:
            res = getattr(self, self.__dir__()[self.__start])
            self.__start += 1
            return res
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123