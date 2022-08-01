class ShopInterface:

    def get_id(self) -> None:
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):

    def __init__(self, name: str, weight: float, price: float) -> None:
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = hash((self._name, self._weight, self._price))

    def get_id(self) -> int:
        return self.__id

print(ShopItem("dafdf", 142.11, 232).get_id())
print(ShopItem("dafdf", 142.11, 232).get_id())