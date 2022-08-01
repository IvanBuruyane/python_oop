class Product:

    __ids = []

    def __new__(cls, *args, **kwargs):
        if not cls.__ids:
            cls.__ids.append(1)
        else:
            cls.__ids.append(cls.__ids[-1] + 1)
        return super().__new__(cls)

    def __init__(self, name: str, weight: [int, float], price: [int, float]):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.__ids[-1]


    def __setattr__(self, key, value):
        keys = {
            "name": str,
            "weight": (int, float),
            "price": (int, float),
            "id": int
        }
        if key in keys:
            if isinstance(keys[key], tuple) and type(value) not in keys[key]:
                raise TypeError("Неверный тип присваиваемых данных.")
            elif not isinstance(keys[key], tuple) and type(value) != keys[key]:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:

    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
print(book.__dict__)
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")