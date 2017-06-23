graph = {'A': set(['B', 'C']),
      'B': set(['A', 'D', 'E', 'G']),
      'C': set(['A', 'F']),
      'D': set(['B']),
      'E': set(['B', 'F']),
      'F': set(['C', 'E', 'G']),
      'G': set(['B', 'F']),
      }

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for next in graph[vertex] - set(path):
                stack.append((next, path + [next]))


# print (list(dfs_path(graph, "A", "G"))) => ['A', 'B', 'E', 'F', 'G'] ==> the first run of the method
# print  (list(dfs_path(graph, "A", "G"))) => ['A', 'C', 'F', 'E', 'B', 'G'] ==> the second run of the method
# print  (list(dfs_path(graph, "A", "G"))) => ['A', 'C', 'F', 'G'] ==> the third run of the method
# each iteration of the method returns all possible paths until it runs back to the beginning of the cycle

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
          if next == goal:
            yield path + [next]
          else:
            stack.append((next, path + [next]))
