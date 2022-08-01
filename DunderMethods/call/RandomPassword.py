import random


class RandomPassword:

    def __init__(self, psw_chars: str, min_length: int, max_length: int) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs) -> str:
        return "".join(random.sample(self.psw_chars, random.randint(self.min_length, self.max_length)))

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]
print(lst_pass)

