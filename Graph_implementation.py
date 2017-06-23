class Vertex(object):
  def __init__(self, data):
    self.data = data
    self.neighbors = list()

    self.distance = 99999
    self.color = 'black'

    self.discovery = 0
    self.finish = 0

  def add_neighbor(self, vertex):
    if vertex not in self.neighbors:
      self.neighbors.append(vertex)
      self.neighbors.sort()

  def remove_neighbor(self, vertex):
    if vertex in self.neighbors:
      self.neighbors.pop(self.neighbors.index(vertex))

class Graph(object):
  vertices = {}

  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.data not in self.vertices:
      self.vertices[vertex.data] = vertex
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


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.BFS(a)
g.print_graph()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
g.dfs(a)
g.print_graph()
