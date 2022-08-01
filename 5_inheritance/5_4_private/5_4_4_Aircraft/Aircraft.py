from typing import Any


class Aircraft:

    def __init__(self, model: str, mass: float, speed: float, top: float) -> None:
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def is_string(arg: Any) -> None:
        if type(arg) is not str:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def is_positive_number(arg: Any) -> None:
        if type(arg) not in (int, float) or arg <= 0:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def is_positive_int(arg: Any) -> None:
        if type(arg) is not int or arg <= 0:
            raise TypeError('неверный тип аргумента')


    @staticmethod
    def is_dict(arg: Any) -> None:
        if type(arg) is not dict:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        if key == "_model":
            self.is_string(value)
        elif key in ("_mass", "_speed", "_top"):
            self.is_positive_number(value)
        super().__setattr__(key, value)



class PassengerAircraft(Aircraft):

    def __init__(self, model: str, mass: float, speed: float, top: float, chairs: int) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == "_chairs":
            self.is_positive_int(value)
        super().__setattr__(key, value)


class WarPlane(Aircraft):

    def __init__(self, model: str, mass: float, speed: float, top: float, weapons: dict) -> None:
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key == "_weapons":
            self.is_dict(value)
        super().__setattr__(key, value)

planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]