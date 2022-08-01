class Body:

    def __init__(self, name: str, ro: float, volume: float) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def get_weight(obj) -> float:
        if type(obj) is Body:
            weight = obj.ro * obj.volume
        elif type(obj) in (int, float):
            weight = obj
        return weight

    def __eq__(self, other):
        return self.get_weight(self) == self.get_weight(other)

    def __gt__(self, other):
        return self.get_weight(self) > self.get_weight(other)

    def __lt__(self, other):
        return self.get_weight(self) < self.get_weight(other)



body1, body2, body3 = Body('body1', 100, 12), Body("body2", 110, 11), Body("body3", 30, 40)



print(body2 > body1)  # True, если масса тела body1 больше массы тела body2
print(body1 == body3) # True, если масса тела body1 равна массе тела body2
print(body1 < 1300)     # True, если масса тела body1 меньше 10
print(body2 == 1210)


