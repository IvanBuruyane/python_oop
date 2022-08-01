class Animal:

    def __init__(self, name: str, kind: str, old: int) -> None:
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, value) -> None:
        self.__kind = value

    @property
    def old(self) -> int:
        return self.__old

    @old.setter
    def old(self, value) -> None:
        self.__old = value

animals = [
    Animal("Васька",  "дворовый кот", 5),
    Animal("Рекс", "немецкая овчарка", 8),
    Animal("Кеша", "попугай", 3)
]