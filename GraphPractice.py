from queue import *

q = PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
	print q.get

class Vertex(object):
  def __init__(self, data):
    self.data = data
    self.neighbors = PriorityQueue()

    self.distance = sys.maxint
    self.color = 'black'

    self.discovery = 0
    self.finish = 0

  def add_neighbor(self, vertex, weight):
    if vertex.data not in [x[1] for x in self.neighbors.queue]:
    # if vertex.data not in self.neighbors:
      self.neighbors.put(weight, vertex.data)
      # self.neighbors.sort()

  def remove_neighbor(self, vertex):
    if vertex in self.neighbors:
      self.neighbors.pop(self.neighbors.index(vertex))

# class Edge(object):
#   def __init__(self, data):
#     self.weight = data


class Graph(object):
  vertices = {}

  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.data not in self.vertices:
      self.vertices[vertex.data] = vertex
      return True
    else:
      return False

  def add_edge(self, vertex1, vertex2, weight):
    if vertex1.data in self.vertices and vertex2.data in self.vertices:
      for key, value in self.vertices.items():
        if key == vertex1.data:
          value.add_neighbor(vertex2, weight)
        if key == vertex2.data:
          value.add_neighbor(vertex1, weight)
      return True
    else:
      return False

  def print_graph(self):
    # return self.vertices
      for key in sorted(self.vertices.keys()):
        print (key + ': ' + str(self.vertices[key].neighbors))

  def BFS(self, vertex):
    queue = list()
    vertex.distance = 0
    vertex.color = 'red'

    for v in vertex.neighbors:
      self.vertices[v].distance = vertex.distance + 1
      queue.append(v)

    while len(queue) > 0:
      item = queue.pop(0)
      node_item = self.vertices[item]
      node_item.color = 'red'

      for v in node_item.neighbors:
        node_v = self.vertices[v]
        if node_v.color == 'black':
          queue.append(v)
          if node_v.distance > node_item.distance + 1:
            node_v.distance = node_item.distance + 1

  def _DFS(self, vertex):
    global time
    vertex.color = 'red'
    vertex.discovery = time
    time += 1
    for v in vertex.neighbors:
      if self.vertices[v].color == 'black':
        self._DFS(self.vertices[v])
    vertex.color = 'blue'
    vertex.finish = time
    time += 1

  def dfs(self, vertex):
    global time
    time = 1
    self._DFS(vertex)

  def dijkstra(self, vertex):
    queue = list()
    vertex.distance = 0
    vertex.color = 'red'

    for v in vertex.neighbors:
      self.vertices[v].distance = vertex.distance + vertex.neighbors[v]
      queue.append(v)

    while len(queue) > 0:
      item = queue.pop(0)
      node_item = self.vertices[item]
      node_item.color = 'red'

      for v in node_item.neighbors:
        node_v = self.vertices[v]
        if node_v.color == 'black':
          queue.append(v)
          if node_v.distance > node_item.distance + vertex.neighbors[v]:
            node_v.distance = node_item.distance + vertex.neighbors[v]

g = Graph()
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex("E")

g.add_vertex(A)
g.add_vertex(B)
g.add_vertex(C)
g.add_vertex(D)
g.add_vertex(E)

g.add_edge(A,B,2)
g.add_edge(A,C,4)
g.add_edge(A,D,5)
g.add_edge(B,C,1)
g.add_edge(C,D,1)
g.add_edge(C,E,1)
g.add_edge(D,E,2)

g.dijkstra(A)
g.print_graph()
