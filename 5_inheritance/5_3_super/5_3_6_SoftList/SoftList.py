from typing import Any


class SoftList(list):

    def __init__(self, iter_value) -> None:
        super().__init__(iter_value)

    def __getitem__(self, item) -> Any:
        if not -len(self) <= item < len(self):
            return False
        return super().__getitem__(item)

sl = SoftList("python")
print(sl)
print(sl[-7])
