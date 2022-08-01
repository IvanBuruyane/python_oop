class Animal:

    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old

    def get_info(self) -> str:
        info = f"{self.name}: {self.old}"
        for key in self.__dict__:
            if key not in ("name", "old"):
                info = info + ", " + str(self.__dict__[key])
        return info


class Cat(Animal):

    def __init__(self, name: str, old: int, color: str, weight: float) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):

    def __init__(self, name: str, old: int, breed: str, size: tuple) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size

cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())