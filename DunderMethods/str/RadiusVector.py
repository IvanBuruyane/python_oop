import math


class RadiusVector:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__coords = [0 for i in range(args[0])]
        else:
            self.__coords = list(args)

    def set_coords(self, *args) -> None:
        lower_lengs = min(len(args), len(self.__coords))
        for i in range(lower_lengs):
            self.__coords[i] = args[i]

    def get_coords(self) -> tuple:
        return tuple(self.__coords)

    def __len__(self) -> int:
        return len(self.__coords)

    def __abs__(self):
        sum = 0
        for coord in self.__coords:
            sum += coord * coord
        return math.sqrt(sum)

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords())
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)



