from copy import copy
import sys


class ShopItem:

    def __init__(self, name: str, weight: float, price: float) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


def split_string(string: str, *separators) -> list:
    new_string = string.strip()
    lst = new_string.split(separators[0])
    for i in range(1, len(separators)):
        new_lst = []
        for line in lst:
            new_lst.extend(line.strip().split(separators[i]))
        lst = new_lst
    return lst





lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for line in lst_in:
    spl = line.split(":")
    name, weight, price = spl[0], spl[1].strip().split()[0], spl[1].strip().split()[1]
    item = ShopItem(name, weight, price)
    if shop_items.get(item) is None:
        shop_items[item] = [item, 1]
    else:
        shop_items[item][1] += 1

print(shop_items)
