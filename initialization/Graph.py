from typing import List


class Graph:

    def __init__(self, data: List[int]) -> None:
        self.data = data
        self.is_show = True

    def set_data(self, data: List[int]) -> None:
        self.data = data

    def show_table(self) -> None:
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            [print(self.data[i], end=" ") for i in range(len(self.data) - 1)]
            print(self.data[-1])

    def show_graph(self) -> None:
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных:", end=" ")
            self.show_table()

    def show_bar(self) -> None:
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print("Столбчатая диаграмма:", end=" ")
            self.show_table()

    def set_show(self, fl_show) -> None:
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
