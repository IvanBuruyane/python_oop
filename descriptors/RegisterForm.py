class ValidateString:

    def __init__(self, min_length: int = 3, max_length: int = 100) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string: str) -> bool:
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class StringValue:

    def __init__(self, validator: ValidateString) -> None:
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

class RegisterForm:

    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login: str, password: str, email: str) -> None:
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> list:
        return list(self.__dict__.values())

    def show(self) -> None:
        print(f"<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>")

r = RegisterForm("123", "2345", "sc_lib@list.ru")
print(r.get_fields())
print(r.__dict__)