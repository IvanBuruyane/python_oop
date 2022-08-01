lst = input().split()

try:
    _sum = sum(map(int, lst))
except:
    try:
        _sum = sum(map(float, lst))
    except:
        _sum = "".join(lst)
finally:
    print(_sum)

print(sum(["adfdaf", "dafdaf"]))