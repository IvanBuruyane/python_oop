class FileAcceptor:

    def __init__(self, *args) -> None:
        self.extentions = args

    def __call__(self, filename: str, *args, **kwargs):
        ext = filename.split(".")[-1]
        b = ext in self.extentions
        result = True if b else False
        return result

    def __add__(self, other):
        return FileAcceptor(*(self.extentions + other.extentions))


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", "adfhdaf.mxs"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
total_acceptor = acceptor_docs + acceptor_images
print(total_acceptor.extentions)
filenames = list(filter(total_acceptor, filenames))
print(filenames)
print('jpg' in ("jpg", "jpeg", "png"))