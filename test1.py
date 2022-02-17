def possible(graph, start, goal):
    paths = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in path:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    paths.append(new_path)
    print("possible paths =", paths)

def shortest(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in path:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    print("shortest path =", new_path)
                    return

graph = {'A':['B','D','H'], 'B':['A','C','D'], 'C':['B','D','F'], 'D':['A','B','C','E'], 'E':['D','F','H'], 'F':['C','E','G'], 'G':['F','H'], 'H':['A','E','G']}
possible(graph, 'A', 'H')
shortest(graph, 'A', 'H')
