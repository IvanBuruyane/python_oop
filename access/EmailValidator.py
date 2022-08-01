import re
import random
from string import ascii_lowercase, digits


class EmailValidator:

    CHARS = ascii_lowercase + digits + "_" + "."

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.is_email_str(email):
            return False
        pattern = r"^(?!.*(\.)\1)[a-z0-9_.]{1,100}@(?=.{1,50}$)[a-z]+\.[a-z]+$"
        return re.fullmatch(pattern, email) is not None

    @classmethod
    def get_random_email(cls):
        first_part = random.randint(1, 100)
        return "".join(random.choices(population=cls.CHARS, k=first_part)) + "@gmail.com"

    @staticmethod
    def is_email_str(email):
        return isinstance(email, str)

print(EmailValidator.get_random_email())
print(EmailValidator.check_email("scc.lib@list.ru"))