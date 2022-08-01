from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        """Country name, str"""

    @property
    @abstractmethod
    def population(self):
        """Number of people, int > 0"""

    @property
    @abstractmethod
    def square(self):
        """Square of the country, float > 0"""

    @abstractmethod
    def get_info(self):
        """Return all information about the country"""


class Country(CountryInterface):

    def __init__(self, name: str, population: int, square: float) -> None:
        self.__name = name
        self.__population = population
        self.__square = square

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def population(self) -> int:
        return self.__population

    @population.setter
    def population(self, population: int) -> None:
        self.__population = population

    @property
    def square(self) -> float:
        return self.__square

    @square.setter
    def square(self, square: float) -> None:
        self.__square = square

    def get_info(self) -> str:
        return f"{self.name}: {self.square}, {self.population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000