from typing import Optional


class DigitRetrieve:

    def __call__(self, string: str, *args, **kwargs) -> Optional[int]:
        try:
            return int(string)
        except:
            return None

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)

