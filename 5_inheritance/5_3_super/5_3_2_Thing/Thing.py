class Thing:

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


class ArtObject(Thing):

    def __init__(self, name: str, weight: float, author: str, date: str) -> None:
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):

    def __init__(self, name: str, weight: float, memory: int, CPU: str) -> None:
        super().__init__(name, weight)
        self.memory = memory
        self.CPU = CPU


class Auto(Thing):

    def __init__(self, name: str, weight: float, dims: tuple) -> None:
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):

    def __init__(self, name: str, weight: float, dims: tuple, model: str, old: int) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):

    def __init__(self, name: str, weight: float, dims: tuple, model: str, wheel: bool) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel