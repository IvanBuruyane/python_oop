class ValidatorString:

    def __init__(self, min_length: int, max_length: int, chars: str) -> None:
        self._min_length: int = min_length
        self._max_length: int = max_length
        self._chars: int = chars

    def is_valid(self, string) -> None:
        if not self._min_length <= len(string) <= self._max_length:
            raise ValueError('недопустимая строка')
        if self._chars:
            flag: bool = False
            for symbol in string:
                if symbol in self._chars:
                    flag = True
                    break
            if not flag:
                raise ValueError('недопустимая строка')


class LoginForm:

    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString) -> None:
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request: dict) -> None:
        self.__check_request(request)
        login, password = request.get("login"), request.get("password")
        self._login = login
        self._password = password

    def __setattr__(self, key, value):
        if key == "_login":
            self.login_validator.is_valid(value)
        if key == "_password":
            self.password_validator.is_valid(value)
        super().__setattr__(key, value)

    @staticmethod
    def __check_request(request: dict) -> None:
        if request.get("login") is None or request.get("password") is None:
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)

