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
        if self.is_there_enough_place(thing):
            self.__things.append(thing)
            self.__current_weight += thing.weight

    def remove_thing(self, indx):
        length = len(self.__things)
        if not self.__things:
            raise ValueError("Bag is empty")
        if indx > length:
            raise ValueError("Provided index is bigger than the total amount of things in the bag")
        minus_weight = self.__things.pop(indx).weight
        self.__current_weight -= minus_weight

    def get_total_weight(self) -> int:
        return self.__current_weight

    def is_there_enough_place(self, thing: Thing) -> bool:
        return self.__current_weight + thing.weight <= self.max_weight

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")