from typing import Any


class Thing:

    def __init__(self, name: str, price: float, weight: float) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):

    @staticmethod
    def is_thing(key: Any) -> None:
        if type(key) is not Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __init__(self, things: dict = {}) -> None:
        if type(things) is not dict:
            raise TypeError('аргумент должен быть словарем')
        for key in things:
            self.is_thing(key)
        super().__init__(things)

    def __setitem__(self, key, value) -> None:
        self.is_thing(key)
        super().__setitem__(key, value)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

dict_things[1] = th_1

for x in dict_things:
    print(x.name)