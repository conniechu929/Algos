class Edge:
  def __init__(self, vert1, vert2):
    self.x = vert1
    self.y = vert2

class Graph:
  graph = []

  def __init__(self, num_vertices):
    self.vertices = [i for i in range(num_vertices)]
    self.tree = []

  def add_edges(self, num_edges):
    for i in range(num_edges):
      a = int(raw_input("Starting vertex: "))
      b = int(raw_input("Ending vertex: "))
      if a in self.vertices and b in self.vertices:
        self.graph.append(Edge(a,b))

  def find_tree(self):
    for i in range(len(self.graph)):
      if len(self.tree) == len(self.vertices)-1:
        return self.tree
        print 'tree is full'
      a = self.graph[i].x
      b = self.graph[i].y
      print "A IN FIND TREE:", a
      print "B IN FIND TREE:", b
      if self.vertices[a] != self.vertices[b]:
        self.tree.append(self.graph[i])
        print "BUILDING TREE:", self.tree
        old_vertex, new_vertex = self.vertices[b], self.vertices[a]
        for j in range(len(self.vertices)):
          if self.vertices[j] == old_vertex:
            self.vertices[j] = new_vertex
    print 'end of function'
    return self.tree

  def show_tree(self):
    for i in self.tree:
      print "START:", i.x
      print "END:", i.y

graph = Graph(5)
print graph.vertices
graph.add_edges(6)
print ''
print 'graph:'
print graph.graph
print ''
graph.find_tree()
print graph.tree
graph.show_tree()

  
