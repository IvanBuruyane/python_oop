class StringValue:

    def is_valid(self, string):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length

    def __init__(self, min_length: int = 2, max_length: int = 50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.is_valid(value):
            setattr(instance, self.name, value)


class PriceValue(StringValue):

    def is_valid(self, price):
        return type(price) in (int, float) and 0 <= price <= self.max_value

    def __init__(self, max_value: [int, float] = 10000) -> None:
        self.max_value = max_value


class Product:

    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str, price: [int, float]) -> None:
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

