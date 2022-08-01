class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):

    def __init__(self, name: str) -> None:
        if "name" not in self.__dict__:
            self.name = name


game1 = Game("wwwww")
game2 = Game("431434")
print(game2.name)
