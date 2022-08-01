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

    def push(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            self.__objects[-1].next = obj
        self.__objects.append(obj)

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

    def check_index(self, indx) -> None:
        if type(indx) is not int or (indx < 0 or indx >= len(self.__objects)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int) -> StackObj:
        self.check_index(item)
        return self.__objects[item]

    def __setitem__(self, key: int, value: StackObj) -> None:
        self.check_index(key)
        value.next = self.__objects[key + 1] if key != len(self.__objects) - 1 else None
        self.__objects[key].value = None
        self.__objects[key] = value
        if not key:
            self.top = value
        else:
            self.__objects[key - 1].next = value



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
# res = st[3] # исключение IndexError


