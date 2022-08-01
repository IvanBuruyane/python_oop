CURRENT_OS = 'linux'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:

    def __new__(cls, *args, **kwargs):
        title, path, exts = args[0], args[1], args[2]
        if CURRENT_OS == "windows":
            return cls.create_windows_filedialog(title, path, exts)
        elif CURRENT_OS == "linux":
            return cls.create_linux_filedialog(title, path, exts)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg)