class StringException(Exception):
    """String exception"""


class NegativeLengthString(StringException):
    """ошибка, если длина отрицательная"""


class ExceedLengthString(StringException):
    """ошибка, если длина превышает заданное значение"""