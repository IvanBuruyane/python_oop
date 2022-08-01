from __future__ import annotations

from typing import Any
import copy


class NewList:

    def __init__(self, lst=None) -> None:
        self.lst = lst[:] if lst and type(lst) == list else []

    def get_list(self) -> list:
        return self.lst

    def __sub__(self, other: NewList):
        self.is_list(other)
        original_list: list = copy.copy(self.lst)
        other_lst = other.lst if isinstance(other, NewList) else other
        for el in other_lst:
            self.remove_value_from_list(original_list, el)
        return NewList(original_list)

    def __rsub__(self, other: list):
        self.is_list(other)
        return NewList(other) - self

    @staticmethod
    def remove_value_from_list(lst: list, value: Any) -> list:
        length = len(lst)
        i = 0
        while i < length:
            if type(lst[i]) == type(value) and lst[i] == value:
                del lst[i]
                break
            i += 1
        return lst

    @staticmethod
    def is_list(value: Any) -> None:
        if not isinstance(value, (list, NewList)):
            raise ValueError("Subtracted value is not a list")



lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
print(lst1.get_list())
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list())
print((NewList([1, 3, 5]) - []).get_list())