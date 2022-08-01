class TupleLimit(tuple):

    def __new__(cls, lst: list, max_length: int, *args, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls)

    def __init__(self, lst: list, max_length: int) -> None:
        self.lst = lst

    def __str__(self) -> str:
        return " ".join(list(map(str, self.lst)))

    def __repr__(self) -> str:
        return " ".join(list(map(str, self.lst)))


digits = list(map(float, input().split()))

try:
    tl = TupleLimit(digits, 5)
    print(tl)
except Exception as e:
    print(e)