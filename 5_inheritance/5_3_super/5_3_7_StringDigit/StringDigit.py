from pprint import pprint

class StringDigit(str):

    def __init__(self, string: str) -> None:
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        self.__string = string

    def __str__(self) -> str:
        return self.__string

    def __add__(self, other):
        return StringDigit(self.__string + other)

    def __radd__(self, other):
        return StringDigit(other + self.__string)

# pprint(str.__dict__)
sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
sd = sd + "12f" # ValueError
