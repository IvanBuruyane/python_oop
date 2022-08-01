from typing import Any


def input_int_numbers():
    inp = input()
    spl = inp.split()
    for el in spl:
        if not is_integer(el):
            raise TypeError('все числа должны быть целыми')
    return tuple(map(int, spl))


def is_integer(value: Any) -> bool:
    if type(value) is int:
        return True
    if type(value) is str:
        try:
            int(value)
            dd = value.find(".")
            if dd == -1:
                return True
            else:
                return False
        except:
            return False
    else:
        return False



while True:
    try:
        res = input_int_numbers()
    except Exception as e:
        # print(e)
        continue
    else:
        print(" ".join(list(map(str, res))))
        break

# print(" ".join((1, 2, 4, 5)))