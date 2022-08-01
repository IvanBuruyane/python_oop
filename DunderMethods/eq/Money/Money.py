class Money:

    def __init__(self, volume: float = None, currency: str = None) -> None:
        self.should_be_float(volume)
        self.__volume = volume
        self.__cb = None
        self.__currency = currency

    @staticmethod
    def should_be_float(value) -> None:
        if type(value) not in (int, float):
            raise ValueError("Money volume should be float")

    def should_be_registered(self) -> None:
        if self.__cb is None:
            raise ValueError("Неизвестен курс валют.")

    @property
    def volume(self) -> float:
        return self.__volume

    @volume.setter
    def volume(self, value: float) -> None:
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb) -> None:
        self.__cb = cb

    def get_rub_volume(self) -> float:
        if self.__currency != "rub":
            dollar_volume: float = self.volume * self.cb.rates[self.__currency]
            rub_volume: float = dollar_volume * self.cb.rates["rub"]
        else:
            rub_volume = self.volume
        return rub_volume

    def __eq__(self, other):
        self.should_be_registered()
        other.should_be_registered()
        self_rub_volume, other_rub_volume = self.get_rub_volume(), other.get_rub_volume()
        return abs(self_rub_volume - other_rub_volume) <= 0.1

    def __gt__(self, other):
        self.should_be_registered()
        other.should_be_registered()
        self_rub_volume, other_rub_volume = self.get_rub_volume(), other.get_rub_volume()
        return self_rub_volume - other_rub_volume > 0.1

    def __ge__(self, other):
        self.should_be_registered()
        other.should_be_registered()
        self_rub_volume, other_rub_volume = self.get_rub_volume(), other.get_rub_volume()
        return self_rub_volume > other_rub_volume or self_rub_volume == other_rub_volume

    def __le__(self, other):
        self.should_be_registered()
        other.should_be_registered()
        self_rub_volume, other_rub_volume = self.get_rub_volume(), other.get_rub_volume()
        return self_rub_volume < other_rub_volume or self_rub_volume == other_rub_volume


class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: Money) -> None:
        money.cb = CentralBank


class MoneyD(Money):

    def __init__(self, volume: float = None) -> None:
        super().__init__(volume, "dollar")


class MoneyR(Money):

    def __init__(self, volume: float = None) -> None:
        super().__init__(volume, "rub")


class MoneyE(Money):

    def __init__(self, volume: float = None) -> None:
        super().__init__(volume, "euro")


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")