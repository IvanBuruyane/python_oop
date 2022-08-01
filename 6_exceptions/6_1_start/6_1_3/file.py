# считывание строки и разбиение ее по пробелам
lst_in = input().split()


def convert(value):
    try:
        res = int(value)
    except:
        try:
            res = float(value)
        except:
            res = value
    return res


lst_out = list(map(convert, lst_in))
print(lst_out)

