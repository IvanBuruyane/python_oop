class FloatValidator:

    def __init__(self, min_value: float, max_value: float) -> None:
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value, *args, **kwargs) -> None:
        if type(value) is not float or not self._min_value <= value <= self._max_value:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(FloatValidator):

    def __call__(self, value, *args, **kwargs) -> None:
        if type(value) is not int or not self._min_value <= value <= self._max_value:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst: list, validators: list) -> list:
    res = []
    for value in lst:
        for validator in validators:
            try:
                validator(value)
                if value not in res:
                    res.append(value)
            except:
                continue
    return res

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)