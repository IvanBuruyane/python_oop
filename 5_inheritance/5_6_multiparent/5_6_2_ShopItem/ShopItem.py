class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:

    def __str__(self) -> str:
        r = ""
        for arg in self.__dict__:
            r = r + f"{arg}: {self.__dict__[arg]}\n"
        r = r[:-1]
        return r


class ShopUserView:

    def __str__(self) -> str:
        r = ""
        for arg in self.__dict__:
            if arg != "_id":
                r = r + f"{arg}: {self.__dict__[arg]}\n"
        r = r[:-1]
        return r


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

book = Book("Python ООП", "Балакирев", 2022)
print(book)
print("afaf")