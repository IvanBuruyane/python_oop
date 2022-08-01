class Validator:

    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):

    def __init__(self, min_value: float, max_value: float) -> None:
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data) -> bool:
        return type(data) is float and self._min_value <= data <= self._max_value

    def __call__(self, data, *args, **kwargs) -> bool:
        return self._is_valid(data)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
print(res_1, res_2, res_3)