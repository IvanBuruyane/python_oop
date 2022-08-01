# считывание строки и разбиение ее по пробелам
lst_in = input().split()


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

print(sum(map(int, filter(is_int, lst_in))))



