from typing import List


class Translator:
    words = {}

    def add(self, eng: str, rus: str) -> None:
        if eng in self.words:
            self.words[eng].append(rus)
        else:
            self.words[eng] = [rus]

    def remove(self, eng: str) -> None:
        self.words.pop(eng)

    def translate(self, eng: str) -> List:
        return self.words[eng]


words = [
    ("tree", "дерево"),
    ("car", "машина"),
    ("car", "автомобиль"),
    ("leaf", "лист"),
    ("river", "река"),
    ("go", "идти"),
    ("go", "ехать"),
    ("go", "ходить"),
    ("milk", "молоко")
]

tr = Translator()
[tr.add(word[0], word[1]) for word in words]
tr.remove("car")
print(" ".join(tr.translate("go")))
