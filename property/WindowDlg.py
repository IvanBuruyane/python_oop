class WindowDlg:

    @staticmethod
    def is_size_correct(size: int) -> bool:
        return isinstance(size, int) and 0 <= size <= 10000

    def __init__(self, title: str, width: int, height: int) -> None:
        self.__title = title
        self.__width = None
        self.__height = None
        if self.is_size_correct(width):
            self.__width = width
        if self.is_size_correct(height):
            self.__height = height

    def show(self) -> None:
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width):
        if self.is_size_correct(width):
            self.__width = width
            self.show()


    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height):
        if self.is_size_correct(height):
            self.__height = height
            self.show()
