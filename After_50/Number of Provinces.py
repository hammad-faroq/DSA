#graph (BFS)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in range(len(graph)):
            if neighbor not in visited and graph[node][neighbor]==1:
                visited.add(neighbor)
                queue.append(neighbor)


def bfs_full(graph):
    visited = set()
    k=0
    for node in range(len(graph)):
        if node not in visited:
            bfs(graph, node, visited)   # Run BFS for this component  # optional - separation between components
            k+=1
    return k
