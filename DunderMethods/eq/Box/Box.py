from copy import copy


class Thing:

    def __init__(self, name: str, mass: float) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


class Box:

    def __init__(self) -> None:
        self.things = []

    def add_thing(self, obj: Thing) -> None:
        self.things.append(obj)

    def get_things(self) -> list:
        return self.things

    def __eq__(self, other) -> bool :
        things1: list = self.get_things()
        things2: list = other.get_things()
        if len(things1) != len(things2):
            return False
        things_2_copy: list = copy(things2)
        result: bool = True
        i: int = 0
        while result and i < len(things1):
            result = False
            for thing in things_2_copy:
                if things1[i] == thing:
                    result = True
                    things_2_copy.remove(things1[i])
                    break
            i += 1
        return result

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2
print(res)

