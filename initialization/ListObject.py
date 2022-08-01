import sys


class ListObject:

    def __init__(self, data: str):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])
objects = [ListObject(lst_in[i]) for i in range(1, len(lst_in))]
head_obj.link(objects[0])
[objects[i].link(objects[i + 1]) for i in range(len(lst_in) - 2)]

print(head_obj)

