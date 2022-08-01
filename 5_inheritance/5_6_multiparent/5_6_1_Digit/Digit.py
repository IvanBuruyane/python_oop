class Digit:

    def __init__(self, value: float) -> None:
        self.is_digit(value)
        self.value = value

    def is_digit(self, value) -> None:
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):

    def __init__(self, value: float) -> None:
        super().__init__(value)
        self.is_digit(value)


    def is_digit(self, value) -> None:
        super().is_digit(value)
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):

    def __init__(self, value: float) -> None:
        super().__init__(value)
        self.is_digit(value)

    def is_digit(self, value) -> None:
        super().is_digit(value)
        if type(value) is not float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):

    def __init__(self, value: float) -> None:
        super().__init__(value)
        self.is_digit(value)

    def is_digit(self, value) -> None:
        super().is_digit(value)
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):

    def __init__(self, value: float) -> None:
        super().__init__(value)
        self.is_digit(value)


    def is_digit(self, value) -> None:
        super().is_digit(value)
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):

    def __init__(self, value) -> None:
        super().__init__(value)


class FloatPositive(Float, Positive):

    def __init__(self, value) -> None:
        super().__init__(value)


digits = [
    PrimeNumber(1),
    PrimeNumber(3),
    PrimeNumber(5),
    FloatPositive(1.1244),
    FloatPositive(4.1343),
    FloatPositive(5.432434),
    FloatPositive(14135.3434),
    FloatPositive(0.434441)
]

lst_positive = list(filter(lambda x: True if isinstance(x, Positive) else False, digits))
lst_float = list(filter(lambda x: True if isinstance(x, Float) else False, digits))
print(lst_positive)
FloatPositive(-1.4)