from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"
        match = re.fullmatch(pattern, number)
        return match is not None

    @staticmethod
    def check_name(name):
        pattern = r"^[A-Z0-9]+\s[A-Z0-9]+$"
        match = re.fullmatch(pattern, name)
        return match is not None
