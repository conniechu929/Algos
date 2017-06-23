graph = {'A': set(['B', 'C']),
      'B': set(['A', 'D', 'E', 'G']),
      'C': set(['A', 'F']),
      'D': set(['B']),
      'E': set(['B', 'F']),
      'F': set(['C', 'E', 'G']),
      'G': set(['B', 'F']),
      }

def DFS_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

graph = { 1: [2, 3, 5], 2: [1], 3: [1], 4: [2], 5: [2] }
cycle = list(DFS_path(graph, "A", "G"))
print "THE AMOUNT OF CYCLES OF PATHS:", len(cycle)
