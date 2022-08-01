class Item:

    def __init__(self, name: str, money: float) -> None:
        self.name = name
        self.money = money

    def __add__(self, other) -> float:
        if type(other) not in (Item, float, int):
            raise ValueError("Only Item object can be added")
        if type(other) is Item:
            summ: float = self.money + other.money
        elif type(other) in (float, int):
            summ = self.money + other
        return summ

    def __radd__(self, other) -> float:
        if type(other) not in (Item, float, int):
            raise ValueError("Only Item object can be added")
        return self + other


class Budget:

    def __init__(self) -> None:
        self.items = []

    def add_item(self, it) -> None:
        if type(it) is not Item:
            raise ValueError("Only Item objects can be added to the budget")
        self.items.append(it)

    def remove_item(self, indx: int) -> None:
        self.items.pop(indx)

    def get_items(self) -> list:
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)
