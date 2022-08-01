class InputDigits:

    def __call__(self, *args, **kwargs) -> list:
        return list(map(int, input().split(" ")))

input_dg = InputDigits()
res = input_dg()
print(res)