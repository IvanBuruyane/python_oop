class Cart:
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{good.name}: {good.price}" for good in self.goods]


class Good:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Table(Good):
    pass


class TV(Good):
    pass


class Notebook(Good):
    pass


class Cup(Good):
    pass


cart = Cart()
cart.add(TV("LG", 20499))
cart.add(TV("Samsung", 25499))
cart.add(Table("IKEA Table", 4499.99))
cart.add(Notebook("HP", 24999))
cart.add(Notebook("MacBook Pro 16", 70999))
cart.add(Cup("IKEA Cup", 9.99))

print(cart.get_list())
