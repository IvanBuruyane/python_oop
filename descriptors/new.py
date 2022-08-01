class StackObj:

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.data


class Stack:

    def __init__(self, max_length: int) -> None:
        self.obj = []
        self.max_length = max_length
        self.top = None
        self.end = None

    def push(self, obj: StackObj) -> None:
        if self.get_stack_length() > self.max_length - 1:
            del self.obj[0]
            self.obj[0].prev = None
        self.obj.append(obj)

    def pop(self) -> None:
        if not self.get_stack_length():
            raise IndexError("Stack is empty")
        res = self.obj.pop(-1)
        res.prev = None
        if self.get_stack_length():
           self.obj[-1].next = None
        return res

    def show(self):
        if not self.get_stack_length():
            print("Stack is empty")
        for obj in reversed(self.obj):
            print(obj)

    def get_stack_length(self) -> int:
        return len(self.obj)



stack = Stack(3)
stack.push(StackObj("obj1"))
stack.push(StackObj("obj2"))
stack.push(StackObj("obj3"))
stack.push(StackObj("obj4"))
stack.show()
print()
print(f"deleted obj: {stack.pop()}")
stack.show()
stack.pop()
stack.pop()
stack.show()
stack.pop()