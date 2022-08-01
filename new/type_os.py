TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, name, *args, **kwargs):
        _cls = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        _cls.name = name
        return _cls

dlg = Dialog("fadfefe")
print(dlg.name)