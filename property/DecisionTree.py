from typing import ClassVar, Type


class TreeObj:

    def __init__(self, indx: int, value: str = None) -> None:
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj) -> None:
        self.__right = obj

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj) -> None:
        self.__left = obj

class DecisionTree:

    NODES = []

    @classmethod
    def predict(cls, root: TreeObj, x: list):
        if x[0]:
            next_obj = root.left
            next_index = 1
        else:
            next_obj = root.right
            next_index = 2
        if x[next_index]:
            answer = next_obj.left.value
        else:
            answer = next_obj.right.value
        return answer

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj = None, left: bool = True):
        cls.NODES.append(obj)
        if node is not None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [0, 1, 0]
res = DecisionTree.predict(root, x)

print(res)
