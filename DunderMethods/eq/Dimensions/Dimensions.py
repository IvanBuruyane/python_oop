class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a: int, b: int, c: int) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def __is_dimension_valid(cls, value: int) -> bool:
        if type(value) is int and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
            return True
        else:
            return False

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, value: int) -> None:
        if self.__is_dimension_valid(value):
            self.__a = value

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, value: int) -> None:
        if self.__is_dimension_valid(value):
            self.__b = value

    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, value: int) -> None:
        if self.__is_dimension_valid(value):
            self.__c = value

    def get_volume(self) -> int:
        return self.a * self.b * self.c

    def __ge__(self, other) -> bool:
        return self.get_volume() >= other.get_volume()

    def __gt__(self, other):
        return self.get_volume() > other.get_volume()

    def __le__(self, other) -> bool:
        return self.get_volume() <= other.get_volume()

    def __lt__(self, other):
        return self.get_volume() < other.get_volume()


class ShopItem:

    def __init__(self, name: str, price: float, dim: Dimensions) -> None:
        self.name = name
        self.price = price
        self.dim = dim


lst_shop: list = [
    ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
    ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
    ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
    ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
]
lst_shop_sorted: list = sorted(lst_shop, key=lambda item: item.dim.get_volume())

[print(item.dim.get_volume(), item.name) for item in lst_shop]
print()
[print(item.dim.get_volume(), item.name) for item in lst_shop_sorted]

d = Dimensions(40, 30, 120)
print(d.__dict__.get("m"))
print(d.__dict__)
print(getattr(d, "a"))
print(type(3432424))