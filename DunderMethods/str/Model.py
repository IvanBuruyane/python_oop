class Model:

    def __init__(self) -> None:
        self.row: dict = {}

    def query(self, **kwargs) -> None:
        self.row = kwargs

    def __str__(self) -> str:
        if not self.row:
            return "Model"
        else:
            end_str = "Model:"
            for key in self.row:
                end_str += f" {key} = {self.row[key]},"
            return end_str[:-1]

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)