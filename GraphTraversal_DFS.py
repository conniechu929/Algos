class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph(object):
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and Vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            for key, value in self.vertices.items():
                if key == vertex1:
                    value.add_neighbor(vertex2)
                if key == vertex2:
                    value.add_neighbor(vertex1)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print (key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].discovery))

    def _dfs(self, vertex):
        global time
        vertex.color = "red"
        vertex.discovery = time
        time += 1
        for vertex2 in vertex.neighbors:
            if self.vertices[vertex2].color == 'black':
                self._dfs(self.vertices[vertex2])
        vertex.color = "blue"
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)
