
class Territory:
    def __init__(self):
        self.name = ''
        self.color = 0
        self.neighbors = {}

    def set_color(self, c):
        self.color = c

    def set_name(self, n):
        self.name = n

    def add_neighbor(self, name, terr):
        self.neighbors[name] = terr

    def update_neighbors(self, graph):
        for k, terr in graph.terrirories.items():
            if k in self.neighbors.keys():
                self.neighbors[k] = terr


class Graph:
    def __init__(self, s):
        self.map = s
        self.get_graph()

    def get_graph(self):
        graph = {}
        splitted = self.map.split()
        for i, line in enumerate(splitted):
            for j, letter in enumerate(line):
                if i == 0:
                    if j == 0:
                        self.create_node(graph, letter)
                    else:
                        if letter == line[j - 1]:
                            continue
                        else:
                            self.create_node(graph, letter)
                            self.connect_territories(graph, letter, line[j - 1])
                            self.connect_territories(graph, line[j - 1], letter)
                else:
                    if j == 0:
                        if letter == splitted[i - 1][j]:
                            continue
                        else:
                            self.create_node(graph, letter)
                            self.connect_territories(graph, splitted[i - 1][j], letter)
                            self.connect_territories(graph, letter, splitted[i - 1][j])
                    else:
                        if letter != line[j - 1]:
                            self.create_node(graph, letter)
                            self.connect_territories(graph, line[j - 1], letter)
                            self.connect_territories(graph, letter, line[j - 1])

                        if letter != splitted[i - 1][j]:
                            self.create_node(graph, letter)
                            self.connect_territories(graph, splitted[i - 1][j], letter)
                            self.connect_territories(graph, letter, splitted[i - 1][j])
                        else:
                            continue
        self.graph = graph
        self.create_terr_list()

    @staticmethod
    def create_node(graph, node):
        if node not in list(graph.keys()):
            graph[node] = []

    @staticmethod
    def connect_territories(graph, territory, connected):
        if connected not in graph[territory]:
            graph[territory].append(connected)

    def create_terr_list(self):
        self.terrirories = {}
        for key in self.graph:
            terr = Territory()
            terr.set_name(key)
            for n in self.graph[key]:
                terr.add_neighbor(n, terr)
            self.terrirories[key] = terr


def color(s):
    graph = Graph(s)
    map = graph.graph
    color_set = [i for i in range(1, 5)]
    degrees = dict([(terr, len(n)) for terr, n in map.items()])
    degrees = dict(sorted(degrees.items(), key=lambda x:x[1], reverse=True))
    for color in color_set:
        for terr in degrees:
            territory = graph.terrirories[terr]
            neighbor_colors = [node.color for node in territory.neighbors.values()]
            if territory.color == 0 and color not in neighbor_colors:
                territory.set_color(color)
                for terr in graph.terrirories.values():
                    terr.update_neighbors(graph)
    colors = [terr.color for terr in graph.terrirories.values()]
    return max(colors)
