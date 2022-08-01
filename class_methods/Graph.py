from typing import List

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: List) -> None:
        self.data = data

    def draw(self) -> None:
        [print(el, end=" ") for el in self.data if el >= Graph.LIMIT_Y[0] and el <= Graph.LIMIT_Y[1]]

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()