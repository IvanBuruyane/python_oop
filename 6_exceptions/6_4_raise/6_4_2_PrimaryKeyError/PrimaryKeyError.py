class PrimaryKeyError(Exception):

    def __init__(self, **kwargs) -> None:
        if not kwargs:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            key = list(kwargs.keys())[0]
            self.message = f"Значение первичного ключа {key} = {kwargs.get(key)} недопустимо"

    def __str__(self) -> str:
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)


