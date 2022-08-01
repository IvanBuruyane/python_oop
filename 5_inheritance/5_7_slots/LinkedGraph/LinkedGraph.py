from copy import copy


class Vertex:

    def __init__(self) -> None:
        self._links: list = []

    @property
    def links(self) -> list:
        return self._links

    @staticmethod
    def link_in_links(link, links: list) -> bool:
        flag = False
        for l in links:
            if (l.v1 == link.v1 and l.v2 == link.v2) or (l.v1 == link.v2 and l.v2 == link.v1):
                flag = True
                break
        return flag

    @staticmethod
    def find_vertex_in_links(v, links: list):
        res = None
        for link in links:
            if v == link.v1 or v == link.v2:
                res = link
                break
        return res


class Link:

    def __init__(self, v1: Vertex, v2: Vertex, dist: float = 1) -> None:
        self._v1: Vertex = v1
        self._v2: Vertex = v2
        self._dist: float = dist
        v1.links.append(self)
        v2.links.append(self)

    def get_second_vertex(self, v1: Vertex) -> Vertex:
        res = self.v2 if v1 == self.v1 else self.v1
        return res

    @property
    def v1(self) -> Vertex:
        return self._v1

    @property
    def v2(self) -> Vertex:
        return self._v2

    @property
    def dist(self) -> float:
        return self._dist

    @dist.setter
    def dist(self, dist: float) -> None:
        self._dist = dist

    def __gt__(self, other) -> bool:
        return self._dist > other._dist

    def __str__(self) -> str:
        return f"{self.v1} - {self.v2}: {self.dist}"


class LinkedGraph:

    def __init__(self) -> None:
        self._links: list = []
        self._vertex: list = []

    @staticmethod
    def __get_vertexex_from_links(links: list) -> list:
        res = []
        for link in links:
            if link.v1 not in res:
                res.append(link.v1)
            if link.v2 not in res:
                res.append(link.v2)
        return res

    def add_vertex(self, v: Vertex) -> None:
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link) -> None:
        if not Vertex.link_in_links(link, self._links):
            self._links.append(link)
        if link.v1 not in self._vertex:
            self._vertex.append(link.v1)
        if link.v2 not in self._vertex:
            self._vertex.append(link.v2)

    def find_path(self, start_v: Vertex, stop_v: Vertex) -> tuple:
        # seen = []
        vertexes = {vertex: {"weight": float("inf"), "links": []} for vertex in self._vertex}
        left = list(vertexes.keys())
        vertexes[start_v]["weight"] = 0
        current = start_v
        while left:
            for link in current.links:
                v2 = link.get_second_vertex(current)
                if v2 not in left:
                    continue
                new_weight = vertexes[current]["weight"] + link.dist
                if new_weight < vertexes[v2]["weight"]:
                    vertexes[v2]["weight"] = new_weight
                    vertexes[v2]["links"] = copy(vertexes[current]["links"])
                    vertexes[v2]["links"].append(link)
            left.remove(current)
            current = min(vertexes, key=lambda x: vertexes[x]["weight"] if x in left else float("inf"))
        return self.__get_vertexex_from_links(vertexes[stop_v]["links"]), vertexes[stop_v]["links"]


class Station(Vertex):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.name}"


class LinkMetro(Link):

    def __init__(self, v1: Station, v2: Station, dist: float) -> None:
        super().__init__(v1, v2, dist)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
