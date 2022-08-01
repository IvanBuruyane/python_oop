class Thing:

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


class Bag:

    def __init__(self, max_weight: int) -> None:
        self.__things = []
        self.max_weight = max_weight
        self.__current_weight = 0

    @property
    def things(self) -> list:
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        self.is_there_enough_place(thing)
        self.__things.append(thing)
        self.__current_weight += thing.weight

    def remove_thing(self, indx):
        length = len(self.__things)
        if not self.__things:
            raise ValueError("Bag is empty")
        self.check_index(indx)
        minus_weight = self.__things.pop(indx).weight
        self.__current_weight -= minus_weight

    def get_total_weight(self) -> int:
        return self.__current_weight

    def is_there_enough_place(self, thing: Thing) -> bool:
        if self.__current_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, indx) -> None:
        if type(indx) is not int or (indx < 0 or indx >= len(self.__things)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int) -> Thing:
        self.check_index(item)
        return self.__things[item]

    def __setitem__(self, key: int, value: Thing) -> None:
        self.check_index(key)
        additional_value = value.weight - self.things[key].weight
        self.is_there_enough_place(Thing("", additional_value))
        self.__things[key] = value
        self.__current_weight += additional_value

    def __delitem__(self, key: int) -> None:
        self.remove_thing(key)

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4]