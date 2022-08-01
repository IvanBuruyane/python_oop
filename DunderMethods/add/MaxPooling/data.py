import random
import json
from MaxPooling import MaxPooling

DATA = []


def random_matrix(n: int, m: int) -> list:
    return [[random.randint(-1000, 1000) for i in range(n)] for j in range(m)]



for i in range(20):
    random.seed(i)
    max_n = random.randint(4, 20)
    max_m = random.randint(4, 20)
    size = (random.randint(2, max_n // 2), random.randint(2, max_m // 2))
    step = (random.randint(2, max_n // 2), random.randint(2, max_m // 2))
    mp = MaxPooling(size, step)
    matrix = random_matrix(max_n, max_m)
    res = mp(matrix)
    DATA.append([matrix, size, step, res])


with open("data.json", "w", encoding='utf-8') as output:
    json.dump(DATA, output, ensure_ascii=False, indent=4)

print(DATA[4])
matrix = DATA[4]["matrix"]
size = DATA[4]["size"]
step = DATA[4]["step"]
ob = MaxPooling(size, step)
rr = ob(matrix)

