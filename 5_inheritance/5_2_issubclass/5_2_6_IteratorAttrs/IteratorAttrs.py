class IteratorAttrs:

    def __iter__(self):
        self.__keys = list(self.__dict__.keys())
        self.__i = 0
        return self

    def __next__(self):
        if self.__i < len(self.__keys):
            attr = self.__keys[self.__i]
            res = (attr, getattr(self, attr))
            self.__i += 1
            return res
        else:
            raise StopIteration


class SmartPhone(IteratorAttrs):

    def __init__(self, model: str, size: tuple, memory: int) -> None:
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone("adfdf", (12, 13), 341)
attrs = phone.__dir__()
# [print(attr) for attr in attrs if not attr.startswith("__")]
# print(phone.__dict__)
for attr, value in phone:
    print(attr, value)
