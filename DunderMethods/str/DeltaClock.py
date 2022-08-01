class Clock:

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:

    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def number_zero_first(self, number: int) -> str:
        if 0 <= number <= 9:
            return f"0{number}"
        else:
            return str(number)

    def __len__(self) -> int:
        return max(self.clock1.get_time() - self.clock2.get_time(), 0)

    def __str__(self) -> str:
        diff: int = len(self)
        if diff <= 0:
            hh: str = self.number_zero_first(0)
            mm: str = self.number_zero_first(0)
            ss: str = self.number_zero_first(0)
        else:
            hh = self.number_zero_first(diff // 3600)
            mm = self.number_zero_first(diff % 3600 // 60)
            ss = self.number_zero_first(diff % 60)
        return f"{hh}: {mm}: {ss}"

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
print(len(dt))