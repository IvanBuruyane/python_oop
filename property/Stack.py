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

    def pop_back(self) -> StackObj:
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




h = StackObj('5')
print(h._StackObj__data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
print(st.get_data()) # 1 2 3
st = st + StackObj('4')
st += StackObj('5')
print(st.get_data()) # 1 2 3 4 5
st = st * [str(i) for i in range(6, 9)]
print(st.get_data())
st *= [str(i) for i in range(9, 12)]
print(st.get_data()) # 1 2 3 4 5 6 7 8 9 10 11 12