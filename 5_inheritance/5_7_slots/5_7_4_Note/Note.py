from typing import Any


class Note:

    def __init__(self, name: str, ton: int) -> None:
        self._name = name
        self._ton = ton

    def __str__(self) -> str:
        return f"{self._name} {self._ton}"

    @staticmethod
    def __is_note(note: str) -> None:
        if note not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')

    @staticmethod
    def __is_tone(ton: int) -> None:
        if ton not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

    def __setattr__(self, key: str, value: Any):
        if key == "_name":
            self.__is_note(value)
        elif key == "_ton":
            self.__is_tone(value)
        super().__setattr__(key, value)


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self._do = Note("до", 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)


    @staticmethod
    def __check_index(indx: int) -> None:
        if type(indx) is not int or not 0 <= indx <= 6:
            raise IndexError('недопустимый индекс')

    def __getitem__(self, item: int) -> None:
        self.__check_index(item)
        return getattr(self, list(self.__slots__)[item])

notes = Notes()

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -2
print(nota)
print(notes[3])
