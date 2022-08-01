# class TelecastDescriptor:
#
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)

class Telecast:

    LAST_TELECAST = 0
    # id = TelecastDescriptor()
    # name = TelecastDescriptor()
    # duration = TelecastDescriptor()

    def __new__(cls, *args, **kwargs):
        if args[0] != cls.LAST_TELECAST + 1:
            raise ValueError("Cast has incorrect id")
        cls.LAST_TELECAST += 1
        return super().__new__(cls)

    def __init__(self, id: int, name: str, duration: int) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def __del__(self):
        Telecast.LAST_TELECAST -= 1


class TVProgram:

    def __init__(self, channel_name: str) -> None:
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl: Telecast) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx):
        length = len(self.items)
        if not self.items:
            raise ValueError("There are no telecast on the channel")
        if indx - 1 > length:
            raise ValueError("Provided index is bigger than the total amount of telecasts on the channel")
        self.items.pop(indx - 1)
        for i in range(indx, length - 1):
            self.items[i].id -= 1

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(1)
for t in pr.items:
    print(f"{t.id} {t.name}: {t.duration}")
print(Telecast.LAST_TELECAST)