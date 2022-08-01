class Book:

    def __init__(self, title: str = "", author: str = "", pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        keys = {
            "title": str,
            "author": str,
            "pages": int,
            "year": int
        }
        if key in keys:
            if type(value) != keys[key]:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
print(book.year)

