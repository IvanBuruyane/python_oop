class IterColumn:

    def __init__(self, lst: list, column: int) -> None:
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.__counter = 0
        self.__value = self.lst[self.__counter][self.column]
        return self

    def __next__(self):
        if self.__counter < len(self.lst):
            res = self.__value
            self.__counter += 1
            if self.__counter < len(self.lst):
                self.__value = self.lst[self.__counter][self.column]
            return res
        else:
            raise StopIteration