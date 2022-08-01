class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        self.length += 1

    def remove_obj(self):
        if self.head is None:
            raise RuntimeError("Linked list is empty")
        elif self.tail.get_prev() is None:
            self.tail = None
            self.head = None
        else:
            new_tail = self.tail.get_prev()
            self.tail.set_prev(None)
            new_tail.set_next(None)
            self.tail = new_tail
        self.length -= 1

    def get_data(self, obj=None, _list=[], ):
        if not _list:
            obj = self.head
        data = obj.get_data()
        _list.append(data)
        if obj.get_next() is not None:
            _list = self.get_data(obj.get_next(), _list)
        return _list

    def __len__(self):
        return self.length

    def __call__(self, indx, *args, **kwargs):
        obj = self.head
        for i in range(indx):
            obj = obj.get_next
        return obj.get_data




linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)

print(n)
print(s)


