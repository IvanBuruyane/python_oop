class SingletonFive:

    count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.count <= 4:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, name):
        self.name = name
        SingletonFive.count += 1

objs = [SingletonFive(str(n)) for n in range(10)]
[print(id(obj)) for obj in objs]