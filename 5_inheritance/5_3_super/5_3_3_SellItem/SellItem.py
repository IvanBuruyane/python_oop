class SellItem:

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class House(SellItem):

    def __init__(self, name: str, price: float, material: str, square: float) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):

    def __init__(self, name: str, price: float, size: tuple, rooms: int) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):

    def __init__(self, name: str, price: float, square: float) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name: str) -> None:
        self.name = name
        self.__objects = []

    def add_object(self, obj: SellItem) -> None:
        self.__objects.append(obj)

    def remove_obj(self, obj: SellItem) -> None:
        self.__objects.remove(obj)

    def get_objects(self) -> list:
        return self.__objects

ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = list(filter(lambda x: isinstance(x, House), ag.get_objects()))
print(lst_houses)
