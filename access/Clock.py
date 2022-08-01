class Clock:

    def __init__(self, time: int = 0) -> None:
        self.__time = time

    @staticmethod
    def __check_time(time):
        return isinstance(time, int) and 0 <= time < 100000

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time
        else:
            raise ValueError("Time should be int in [0, 100000)")

    def get_time(self):
        return self.__time

clock = Clock()
clock.set_time(4530)
print(clock.get_time())