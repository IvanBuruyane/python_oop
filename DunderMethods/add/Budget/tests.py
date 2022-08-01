import pytest

from Budget import Item, Budget

@pytest.fixture
def prepare_items():
    item1 = Item("Pen", 10.99)
    item2 = Item("Book", 101)
    item3 = Item("Gum", 12.1)
    item4 = Item("Paper", 150.99)
    return item1, item2, item3, item4

def test_add_2_items(prepare_items):
    item1, item2, item3, item4 = prepare_items
    assert item1 + item2 == 111.99

def test_add_4_items(prepare_items):
    item1, item2, item3, item4 = prepare_items
    assert round(item1 + item2 + item4 + item3, 2) == 275.08


def test_add_items_to_the_budget(prepare_items):
    item1, item2, item3, item4 = prepare_items
    b = Budget()
    b.add_item(item1)
    b.add_item(item2)
    assert len(b.get_items()) == 2


def test_remove_item_from_budget(prepare_items):
    item1, item2, item3, item4 = prepare_items
    b = Budget()
    b.add_item(item4)
    b.add_item(item1)
    b.remove_item(1)
    assert len(b.get_items()) == 1
    assert b.get_items()[0].money == item4.money
    assert b.get_items()[0].name == item4.name