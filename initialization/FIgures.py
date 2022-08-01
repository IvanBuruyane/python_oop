import random


class Line:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect(Line):

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse(Line):

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
for i in range(217):
    cords = {
        "a": random.randint(-1000, 1000),
        "b": random.randint(-1000, 1000),
        "c": random.randint(-1000, 1000),
        "d": random.randint(-1000, 1000),
    }
    fig = random.choice([Line, Rect, Ellipse])(**cords)
    if isinstance(fig, Line):
        fig.sp = (0, 0)
        fig.ep = (0, 0)
    elements.append(fig)



[print(el.sp, el.ep, type(el)) for el in elements]
