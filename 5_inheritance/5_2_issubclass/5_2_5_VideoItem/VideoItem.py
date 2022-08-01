class VideoItem:

    def __init__(self, title: str, descr: str, path: str) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    def __init__(self) -> None:
        self.__rating = 0

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, value: int) -> None:
        if type(value) is not int or not 0 <= value <= 5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
print(title)
print(descr)
v.rating.rating = 6