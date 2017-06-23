class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph(object):
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices and vertex2 not in self.vertices:
            for key, value in self.vertices.items():
                if key == vertex1:
                    self.add_neighbor(vertex2)
                if key == vertex2:
                    self.add_neighbor(vertex1)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(self.vertices.keys()):
            print (key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))

    def bfs(self, vert):
        queue = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            queue.append(v)

        while len(queue) > 0:
            item = queue.pop()
            node_item = self.vertices[item]
            node_item.color = 'red'

            for v in node_item.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    queue.append(v)
                    if node_v.distance > node_item.distance + 1:
                        node_v.distance = node_item.distance + 1
