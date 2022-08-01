class ImageFileAcceptor:

    def __init__(self, extensions: tuple) -> None:
        self.__extensions = extensions

    def __call__(self, filename: str, *args, **kwargs) -> bool:
        for ext in self.__extensions:
            if filename.endswith("." + ext):
                return True
        return False

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]