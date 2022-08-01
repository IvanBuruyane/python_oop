class Test:

    def __init__(self, descr: str) -> None:
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr: str, ans_digit: float, max_error_digit: float = 0.01) -> None:
        super().__init__(descr)
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self) -> bool:
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)

try:
    tt = TestAnsDigit(descr, ans)
    print(tt.run())
except Exception as e:
    print(e)

