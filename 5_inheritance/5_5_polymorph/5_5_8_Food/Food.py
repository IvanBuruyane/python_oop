class Food:

    def __init__(self, name: str, weight: float, calories: int) -> None:
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):

    def __init__(self, name: str, weight: float, calories: int, white: bool) -> None:
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):

    def __init__(self, name: str, weight: float, calories: int, dietary: bool) -> None:
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):

    def __init__(self, name: str, weight: float, calories: int, fish: str) -> None:
        super().__init__(name, weight, calories)
        self._fish = fish