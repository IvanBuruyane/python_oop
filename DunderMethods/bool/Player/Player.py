import sys


class Player:

    def __init__(self, name: str, old: int, score: int) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __len__(self) -> bool:
        return int(self.score) > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*line.split(";")) for line in lst_in]
players_filtered = list(filter(bool, players))
print(players_filtered)