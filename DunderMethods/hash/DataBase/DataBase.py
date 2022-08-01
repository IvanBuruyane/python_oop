import sys


class Record:

    PK = 0

    def __init__(self, fio: str, descr: str, old: int) -> None:
        Record.PK += 1
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.PK

    def __hash__(self):
        return hash((self.fio, self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DataBase:

    def __init__(self, path: str) -> None:
        self.path = path
        self.dict_db = {}

    def write(self, record: Record) -> None:
        if self.dict_db.get(record) is None:
            self.dict_db[record] = [record]
        else:
            self.dict_db[record].append(record)

    def read(self, pk: int) -> Record:
        for key in self.dict_db:
            if pk == key.pk:
                return key
            for value in self.dict_db[key]:
                if pk == value.pk:
                    return value
        raise ValueError("There's no record with searched pk in the DataBase")


lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase("path")
[db.write(Record(*line.split(";"))) for line in lst_in]
[print(line) for line in db.dict_db]