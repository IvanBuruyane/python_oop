from typing import Any


class Validator:

    def _is_valid(self, data: Any) -> bool:
        return True

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True


class IntegerValidator(Validator):

    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: Any) -> bool:
        return type(data) is int and self.min_value <= data <= self.max_value


class FloatValidator(Validator):

    def __init__(self, min_value: float, max_value: float) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: Any) -> bool:
        return type(data) is float and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
print(res1)
res2 = float_validator(10)

