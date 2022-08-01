import time

class Filter:

    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and self.date:
            return self.date
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.__filters = [None, None, None]
        self.__filter_types = [Mechanical, Aragon, Calcium]

    def add_filter(self, slot_num: [0, 1, 2], filter: Filter) -> None:
        corrected_slot_num = slot_num - 1
        if self.__filters[corrected_slot_num] is None and isinstance(filter, self.__filter_types[corrected_slot_num]):
            self.__filters[corrected_slot_num] = filter
            # print(f"Filter is set to the slot {corrected_slot_num}")

    def remove_filter(self, slot_num: [0, 1, 2]) -> None:
        corrected_slot_num = slot_num - 1
        self.__filters[corrected_slot_num] = None

    def get_filters(self) -> tuple:
        return tuple(self.__filters)

    def water_on(self) -> bool:
        return self.all_filters_installed(self.__filters, self.__filter_types) and \
               self.all_filters_are_not_expired(self.__filters)

    @staticmethod
    def all_filters_installed(list_of_filters, list_of_types) -> bool:
        for i in range(len(list_of_filters)):
            if list_of_filters[i] is None or not isinstance(list_of_filters[i], list_of_types[i]):
                return False
        return True

    @classmethod
    def all_filters_are_not_expired(cls, list_of_filters):
        for filter in list_of_filters:
            if time.time() - filter.date < 0 or time.time() - filter.date > cls.MAX_DATE_FILTER:
                return False
        return True



my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
print(my_water.__dict__)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
print(my_water.__dict__)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
