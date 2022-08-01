from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def get_pk(self):
        """get_pk"""

    def get_info(self) -> str:
        return "Базовый класс Model"


class ModelForm(Model):

    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._id = hash((self._login, self._password))

    def get_pk(self) -> int:
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())