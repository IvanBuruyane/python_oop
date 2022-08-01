class Thing:

    __id = 0

    def __new__(cls, *args, **kwargs):
        Thing.__id += 1
        return super().__new__(cls)

    def __init__(self, name: str, price: float) -> None:
        self.id = self.__id
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):

    def __init__(self, name: str, price: float, weight: float, dims: tuple) -> None:
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name: str, price: float, memory: int, frm: str) -> None:
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())