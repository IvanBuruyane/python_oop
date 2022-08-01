from typing import Callable, Optional


class RenderDigit:

    def __call__(self, string: str, *args, **kwargs) -> Optional[int]:
        try:
            return int(string)
        except:
            return None


class InputValues:

    def __init__(self, render: Callable) -> None:
        self.__render = render

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> list:
            func_result = func()
            return list(map(self.__render, func_result.split(" ")))
        return wrapper

@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)