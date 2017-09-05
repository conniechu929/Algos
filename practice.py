def removeDup(string):
    temp_list = list(string)
    result = []
    for i in temp_list:
        if i not in result:
            result.append(i)
    return ''.join(result)

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visitied)
    return visited

def bfs(graph, start):


def dfs_path(graph, start, goal):


def bfs_path(graph, start, goal):
