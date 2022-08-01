from typing import Any


class StackObj:

    def __init__(self, data: str) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj) -> None:
        if obj is None or isinstance(obj, StackObj):
            self.__next = obj


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.__objects = []

    def push_back(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            self.__objects[-1].next = obj
        self.__objects.append(obj)

    def push_front(self, obj: StackObj) -> None:
        obj.next = self.top
        self.top = obj
        self.insert_in_list(obj, self.__objects, 0)

    def pop(self) -> StackObj:
        if not self.__objects:
            raise RuntimeError("Stack is empty")
        elif len(self.__objects) == 1:
            pop_obj = self.__objects.pop(-1)
            self.top = None
        else:
            pop_obj = self.__objects.pop(-1)
            self.__objects[-1].next = None
        return pop_obj

    def get_data(self):
        return [obj.data for obj in self.__objects]

    def check_index(self, indx) -> None:
        if type(indx) is not int or (indx < 0 or indx >= len(self.__objects)):
            raise IndexError('неверный индекс')

    def __add__(self, other):
        if type(other) is not StackObj:
            raise ValueError("Adding non StackObj to the Stack is forbidden")
        self.push_back(other)
        return self

    def __radd__(self, other):
        if type(other) is not StackObj:
            raise ValueError("Adding non StackObj to the Stack is forbidden")
        return self + other

    def __mul__(self, other: list):
        if type(other) is not list:
            raise ValueError("Value should be list of strings")
        for el in other:
            self.push_back(StackObj(el))
        return self

    def __getitem__(self, item: int) -> StackObj:
        self.check_index(item)
        return self.__objects[item].data

    def __setitem__(self, key: int, value: str) -> None:
        self.check_index(key)
        self.__objects[key].data = value

    def __len__(self) -> int:
        return len(self.__objects)

    def __iter__(self):
        self.__indx = 0
        self.__iter_value = self.__objects[self.__indx]
        return self

    def __next__(self):
        if self.__indx < len(self.__objects):
            res = self.__iter_value
            self.__indx += 1
            if self.__indx < len(self.__objects):
                self.__iter_value = self.__objects[self.__indx]
            return res
        else:
            raise StopIteration

    @staticmethod
    def insert_in_list(obj: Any, lst: list, position: int) -> None:
        length: int = len(lst)
        if position > length or position < 0:
            raise IndexError
        if position == length:
            lst.append(obj)
        else:
            lst.append(None)
            for i in range(-1, -(length - position + 1), -1):
                lst[i] = lst[i - 1]
            lst[-(length - position + 1)] = obj





st = Stack()
st.push_back(StackObj("obj1"))
st.push_back(StackObj("obj2"))
st.push_back(StackObj("obj3"))
st.push_front(StackObj("obj1_1"))
st[1] = "eafef"
print(st[1])


