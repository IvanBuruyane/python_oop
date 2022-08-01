import math
from typing import Any


class TrackLine:

    def __init__(self, to_x: float, to_y: float, max_speed: int) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:

    def __init__(self, start_x: float, start_y: float) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.__tracks = []

    def add_track(self, tr: TrackLine) -> None:
        self.__tracks.append(tr)

    def get_tracks(self) -> tuple:
        return tuple(self.__tracks)

    def __len__(self):
        return int(self.__get_track_length())

    def __get_track_length(self) -> int:
        line_start_x: float = self.start_x
        line_start_y: float = self.start_y
        length: float = 0
        for line in self.__tracks:
            length += math.sqrt((line.to_x - line_start_x) ** 2 + (line.to_y - line_start_y) ** 2)
            line_start_x, line_start_y = line.to_x, line.to_y
        return length

    @staticmethod
    def __is_track(object: Any) -> None:
        if type(object) is not Track:
            raise ValueError(f"Comparing TrackLine with {type(object)} is forbidden")

    def __eq__(self, other) -> bool:
        self.__is_track(other)
        return len(self) == len(other)

    def __gt__(self, other) -> bool:
        self.__is_track(other)
        return len(self) > len(other)

track1, track1_point2, track1_point3 = Track(0, 0), TrackLine(2, 4, 100), TrackLine(5, -4, 100)
track1.add_track(track1_point2)
track1.add_track(track1_point3)
track2, track2_point2, track2_point3 = Track(0, 1), TrackLine(3, 2, 90), TrackLine(10, 8, 90)
track2.add_track(track2_point2)
track2.add_track(track2_point3)
res_eq = track1 == track2
print(res_eq)



