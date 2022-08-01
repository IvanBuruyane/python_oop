import re


class PhoneNumber:

    MASK = r"^[0-9]{11}$"

    def __init__(self, number: int, fio: str):
        if self.check_number(str(number)):
            self.number = number
        else:
            raise ValueError("Number should have XXXXXXXXXXX format, where X - digit")
        self.fio = fio

    @classmethod
    def check_number(cls, number):
        return re.fullmatch(cls.MASK, number) is not None


class PhoneBook:

    def __init__(self):
        self.numbers_list = []

    def add_phone(self, phone: PhoneNumber) -> None:
        self.numbers_list.append(phone)

    def remove_phone(self, indx: int) -> None:
        if not isinstance(indx, int):
            raise ValueError("Index should be integer")
        self.numbers_list.pop(indx)


    def get_phone_list(self) -> list:
        return self.numbers_list

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)