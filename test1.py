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

graph = {0:[1,2,3], 1:[0,2,3], 2:[0,1,3], 3:[0,1,2]}
possible(graph, 0, 3)
shortest(graph, 0, 3)
