class TriangleListIterator:

    def __init__(self, lst: list) -> None:
        self.lst = lst

    def __iter__(self):
        self.__i = 0
        self.__j = 0
        self.__lenght = len(self.lst)
        self.__value = self.lst[self.__i][self.__j]
        return self

    def __next__(self):
        if self.__i >= self.__lenght:
            raise StopIteration
        res = self.__value
        self.__j += 1
        if self.__j < self.__i + 1:
            self.__value = self.lst[self.__i][self.__j]
        else:
            self.__i += 1
            if self.__i < self.__lenght:
                self.__j = 0
                self.__value = self.lst[self.__i][self.__j]
        return res




lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
#
# it_iter = iter(it)
# x = next(it_iter)
