class Box:

    def __init__(self, name: str, max_weight: float) -> None:
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj: tuple) -> None:
        if self.get_current_weight() + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        else:
            self._things.append(obj)

    def get_current_weight(self) -> float:
        current_weight = 0
        for thing in self._things:
            current_weight += thing[1]
        return current_weight


class BoxDefender:

    def __init__(self, box: Box) -> None:
        self._box = box

    def __enter__(self):
        self.__temp = self._box.__class__(self._box._name, self._box._max_weight)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            for thing in self.__temp._things:
                self._box.add_thing(thing)
        return False

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    # b.add_thing(("шина", 500))

print(box._things)