from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека"""

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека"""


class StackObj:

    def __init__(self, data: str) -> None:
        self._data = data
        self._next = None
        self._prev = None


class Stack(StackInterface):

    def __init__(self):
        self._top = None
        self._end = None

    def push_back(self, obj: StackObj) -> None:
        if not self._top:
            self._top = obj
            self._end = obj
        else:
            self._end._next = obj
            obj._prev = self._end
            self._end = obj

    def pop_back(self):
        if not self._end:
            return None
        if not self._top._next:
            self._top = None
        res = self._end
        self._end = res._prev
        if self._end:
            self._end._next = None
        return res

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()
del_obj1 = st.pop_back()

print(st)