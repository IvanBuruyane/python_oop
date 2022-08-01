import re


class WordString:

    def __init__(self, string: str = "") -> None:
        self.__string = string

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str) -> None:
        self.__string = string

    def __len__(self) -> int:
        return len(re.split(r'\W+', self.__string.strip()))

    def __call__(self, indx: int, *args, **kwargs) -> str:
        return re.split(r'\W+', self.__string.strip())[indx]

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

# string = "adf      FDA  fdfdf dfdfdf     "
# # new_string = string.replace("  ", " ")
# print(re.split(r'\W+', string))